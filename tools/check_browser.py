#!/usr/bin/env python3
"""Exercise the real site in Chrome, including a GitHub Pages-style prefix.

Requires the optional Python playwright package and a local Chrome installation.
Run directly, or pass SiteBrowserTests.test_mobile_menu_escape_and_resize to
exercise a single behavior.
"""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import shutil
import threading
import unittest

from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[1] / "src"
PAGE_PATHS = [str(path.relative_to(ROOT)) for path in sorted(ROOT.rglob("*.html"))]
LEGACY_PROJECTS = [
    "portfolio/mexican-tile-sun-table/index.html",
    "portfolio/dancing-women-table/index.html",
    "portfolio/talavera-tile-night-stand/index.html",
    "portfolio/deer-in-the-trees-wall-hanging/index.html",
    "portfolio/potted-plant-holder/index.html",
    "portfolio/wooden-birds-wall-hanging/index.html",
    "portfolio/mountain-scene-wall-hanging/index.html",
    "portfolio/black-bear-wall-hanging/index.html",
    "portfolio/tree-of-life-table/index.html",
]


class PrefixHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/bethsmosaics/"):
            self.path = self.path[len("/bethsmosaics"):]
            super().do_GET()
        else:
            self.send_error(404)

    def log_message(self, *_):
        pass


class SiteBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), partial(PrefixHandler, directory=str(ROOT)))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}/bethsmosaics/"
        cls.playwright = sync_playwright().start()
        executable = os.environ.get("BETH_CHROME") or shutil.which("google-chrome") or shutil.which("chromium")
        cls.browser = cls.playwright.chromium.launch(executable_path=executable, headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        self.context = self.browser.new_context(viewport={"width": 390, "height": 844})
        self.page = self.context.new_page()
        self.page.set_default_timeout(4000)

    def tearDown(self):
        self.context.close()

    def goto(self, path="index.html"):
        response = self.page.goto(self.base + path)
        self.assertEqual(response.status, 200)
        if path in LEGACY_PROJECTS:
            expect(self.page).to_have_url(self.base + "index.html#portfolio")
        self.page.evaluate("document.fonts.ready")

    def test_mobile_menu_escape_and_resize(self):
        # Catches a missing menu toggle, wrong expanded state, lost focus,
        # and navigation left hidden after switching to desktop.
        self.goto()
        menu = self.page.get_by_role("button", name="Menu", exact=True)
        self.assertTrue(menu.is_visible(), "The mobile menu needs a visible, working toggle")
        navigation = self.page.get_by_role("navigation", name="Main navigation")
        self.assertFalse(navigation.is_visible())
        menu.click()
        self.assertEqual(menu.get_attribute("aria-expanded"), "true")
        self.assertTrue(navigation.is_visible())
        navigation.get_by_role("link", name="Bio", exact=True).focus()
        self.page.keyboard.press("Escape")
        self.assertFalse(navigation.is_visible())
        self.assertTrue(menu.evaluate("el => document.activeElement === el"))
        menu.click()
        menu.click()
        self.assertFalse(navigation.is_visible())
        self.page.set_viewport_size({"width": 1440, "height": 960})
        expect(navigation).to_be_visible()
        self.assertFalse(menu.is_visible())
        self.page.set_viewport_size({"width": 390, "height": 844})
        menu.click()
        navigation.get_by_role("link", name="Bio", exact=True).click()
        self.assertTrue(self.page.url.endswith("/bio/index.html"))

    def test_gallery_images_do_not_open_details(self):
        # Catches accidentally retained artwork links or enlargement controls.
        self.goto()
        self.assertEqual(self.page.locator(".artwork-grid img").count(), 9)
        self.assertEqual(self.page.locator(".artwork-grid a, .hero-art a").count(), 0)
        self.page.locator(".artwork-grid img").first.click()
        self.assertEqual(self.page.url, self.base + "index.html")
        self.assertEqual(self.page.get_by_role("dialog").count(), 0)
        self.assertEqual(self.page.locator("#process img").count(), 4)
        self.assertEqual(self.page.locator(".process-steps li").count(), 3)

    def test_old_artwork_urls_return_to_gallery(self):
        # Catches missed legacy pages, broken relative redirects, and exposed
        # artwork metadata when following bookmarks under repository hosting.
        for path in LEGACY_PROJECTS:
            with self.subTest(page=path):
                self.goto(path)
                self.assertEqual(self.page.locator(".project-meta, .project-navigation").count(), 0)
                self.assertEqual(self.page.locator(".artwork-grid img").count(), 9)

    def test_classes_and_shows_navigation_and_contact(self):
        # Catches a missing events destination in the mobile navigation or
        # a stranded visitor trying to ask Beth for event information.
        self.goto()
        self.page.get_by_role("button", name="Menu", exact=True).click()
        events_link = self.page.get_by_role("navigation", name="Main navigation").get_by_role("link", name="Classes & Shows", exact=True)
        self.assertEqual(events_link.count(), 1, "Classes & Shows needs a navigation destination")
        events_link.click()
        expect(self.page).to_have_url(self.base + "classes-and-shows/index.html")
        expect(self.page.get_by_role("heading", level=1)).to_have_text("Classes & Shows")
        self.page.locator("main").get_by_role("link", name="Contact Me").click()
        expect(self.page).to_have_url(self.base + "contact/index.html")
        self.assertEqual(self.page.get_by_role("link", name="Email Beth").get_attribute("href"), "mailto:bethemeyerson@gmail.com")

    def test_all_pages_load_without_overflow_or_broken_assets(self):
        # Catches bad nested asset paths, narrow-screen overflow, failed lazy
        # images, and runtime errors on every publishable page.
        errors = []
        self.page.on("pageerror", lambda error: errors.append(str(error)))
        self.page.on("requestfailed", lambda request: errors.append(request.url + " " + str(request.failure)))
        self.page.on("response", lambda response: errors.append(f"HTTP {response.status}: {response.url}") if response.status >= 400 else None)
        for width in (320, 768, 1440):
            self.page.set_viewport_size({"width": width, "height": 960})
            for path in PAGE_PATHS:
                with self.subTest(width=width, page=path):
                    self.goto(path)
                    self.assertTrue(self.page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"), "Horizontal overflow")
                    self.assertEqual(self.page.locator("h1").count(), 1)
                    for image in self.page.locator("main img").all():
                        image.scroll_into_view_if_needed()
                        image.evaluate("el => el.decode()")
                        self.assertTrue(image.evaluate("el => el.naturalWidth > 0"))
                    self.assertTrue(self.page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"))
        self.assertEqual(errors, [])

    def test_javascript_disabled_navigation_and_contact(self):
        # Catches progressive-enhancement regressions that strand visitors.
        context = self.browser.new_context(java_script_enabled=False, viewport={"width": 320, "height": 800})
        try:
            page = context.new_page()
            for path in ("index.html", "bio/index.html", "classes-and-shows/index.html", "contact/index.html", *LEGACY_PROJECTS):
                response = page.goto(self.base + path)
                self.assertEqual(response.status, 200)
                if path in LEGACY_PROJECTS:
                    expect(page).to_have_url(self.base + "index.html#portfolio")
                self.assertTrue(page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"))
                navigation = page.get_by_role("navigation", name="Main navigation")
                self.assertTrue(navigation.is_visible())
                self.assertTrue(navigation.get_by_role("link", name="Contact", exact=True).is_visible())
                self.assertTrue(navigation.get_by_role("link", name="Classes & Shows", exact=True).is_visible())
                self.assertEqual(page.get_by_role("button", name="View full image", exact=True).count(), 0)
                self.assertEqual(page.locator('a[href="mailto:bethemeyerson@gmail.com"]').count() > 0, True)
            page.goto(self.base + "index.html")
            page.get_by_role("navigation", name="Main navigation").get_by_role("link", name="Contact", exact=True).click()
            self.assertTrue(page.url.endswith("/contact/index.html"))
        finally:
            context.close()

    def test_gallery_whole_image_and_skip_link(self):
        # Catches cropped artwork now that there is no separate detail view,
        # and inaccessible main-content shortcuts.
        self.goto()
        self.assertEqual(self.page.locator(".artwork-grid img").last.evaluate("el => getComputedStyle(el).objectFit"), "contain")
        self.page.keyboard.press("Tab")
        self.assertEqual(self.page.locator(":focus").inner_text(), "Skip to content")
        self.page.keyboard.press("Enter")
        self.assertTrue(self.page.locator("#main").evaluate("el => document.activeElement === el"))

    def test_reduced_motion_and_grid_breakpoints(self):
        self.page.emulate_media(reduced_motion="reduce")
        self.goto()
        self.assertEqual(self.page.evaluate("getComputedStyle(document.documentElement).scrollBehavior"), "auto")
        self.assertEqual(self.page.locator(".hero-art img").evaluate("el => getComputedStyle(el).transitionDuration"), "0s")
        for width, columns in [(390, 1), (768, 2), (1440, 3)]:
            self.page.set_viewport_size({"width": width, "height": 960})
            self.assertEqual(self.page.locator(".artwork-grid").evaluate("el => getComputedStyle(el).gridTemplateColumns.split(' ').length"), columns)


if __name__ == "__main__":
    unittest.main(verbosity=2)
