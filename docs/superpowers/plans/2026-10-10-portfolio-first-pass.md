# Portfolio First Pass Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan. The repository's approved workflow permits specification updates and implementation after chat approval; proceed to local review without additional planning approval gates.

**Goal:** Replace the holding page with the approved contemporary mosaic portfolio and provide a tested local preview.

**Architecture:** Twelve static HTML pages share local CSS, fonts, and a small progressive-enhancement script. Every page contains its content and navigation without a build step or JavaScript dependency. Browser-only enhancements handle the mobile menu and full-image dialog.

**Tech Stack:** HTML, CSS, vanilla JavaScript, local WebP photographs, Python link validation and browser QA.

**Spec:** `docs/website.md`.

## Global Constraints

- Publishable HTML, CSS, JavaScript, images, and fonts live only in `src/`. Pages require no build step or server-side service.
- All internal links, CSS, scripts, and images use relative URLs and work under the GitHub Pages `/bethsmosaics/` subpath.
- Retain the existing content, project details, titles, and biography.
- The first pass replaces the Wix contact form with direct email and phone links.
- Work on `feat/portfolio-first-pass`; release needs a reviewed implementation and explicit chat approval.

## Review Focus

- Nested URLs must resolve navigation and assets under a repository subpath.
- At 320px, long titles and contact details must wrap without horizontal overflow.
- JavaScript-disabled visitors must reach every page and contact destination.
- Escape and closing a dialog/menu must restore focus without trapping the user.
- Wide artwork images must remain complete on detail pages; lazy images must load after scrolling.

### Task 1: Static portfolio and responsive presentation

**Files:** Modify `docs/website.md`, `docs/plan.md`, `src/index.html`, `src/assets/css/site.css`, `README.md`; create `src/bio/index.html`, `src/contact/index.html`, nine `src/portfolio/<slug>/index.html` pages, local images/fonts and license, and `tools/check_site.py`.

**Interfaces:** Every page has `#main`, `.site-header`, `.site-nav`, and relative navigation. Artwork images have intrinsic sizes and optional `data-enlarge`; headings, types, locations, and image mappings come from the approved specification.

- [x] Add meaningful validation for navigable pages, relative link/fragment resolution, images and alt text, unique document IDs, contact URLs, and exclusion of documentation from `src/`.
- [x] Run `python3 tools/check_site.py`; confirm failure because the approved portfolio pages and navigation do not yet exist.
- [x] Optimize source photographs and use local fonts with fallbacks and a license.
- [x] Write all static pages and shared responsive styles from the approved specification. Update the README for the first pass and validation commands.
- [x] Run `python3 tools/check_site.py`; require all pages and destinations to pass.

### Task 2: Accessible progressive enhancements

**Files:** Create `src/assets/js/site.js` and `tools/check_browser.py`; update shared HTML/CSS as necessary.

**Interfaces:** Menu trigger uses `aria-controls="site-navigation"` and `aria-expanded`. Image controls are added only for `data-enlarge` images with native dialog support. Dialog restores focus on close. CSS uses `.js` only after enhancement initializes.

- [x] Add browser tests that open the mobile menu, use Escape, enlarge an artwork, close with Escape/backdrop/button, and verify focus restoration.
- [x] Serve `src/` and run the behavior tests against the static pages; confirm failure because enhancements are absent.
- [x] Implement menu state and dialog enhancements without hiding usable static navigation or adding dead controls for JavaScript-disabled visitors.
- [x] Run browser checks at desktop/mobile widths, 320px, reduced motion, and JavaScript disabled; verify subpath pages, lazy images, whole artwork display, and no browser errors or failed local assets.

### Task 3: Reviewable delivery

**Files:** Update `docs/plan.md` with evidence and progress. Screenshots stay under `/tmp/`.

- [x] Inspect desktop/mobile screenshots and compare implementation against `docs/website.md`.
- [x] Perform independent whole-change code review and resolve material findings.
- [x] Run `python3 tools/check_site.py`, browser QA, and `git diff --check`; record results.
- [ ] Verify local Git identity; commit this coherent first-pass change using Conventional Commits. Verify recorded author and committer.
- [ ] Push the feature branch and create a reviewable pull request if available; otherwise provide the exact branch and pull-request creation URL.
- [ ] Keep the local preview available and hand it over for implementation review. Do not merge or publish before explicit release approval.

## Execution record

- Started from `4bf1107`; user approved design in chat.
- Feature branch created after Git metadata required sandbox escalation.
- Original Wix content and photographs collected under `/tmp/`; temporary browser and image tools installed under `/tmp/beth-site-qa`.
- Ruling: use the requested feature branch in the existing checkout and implement inline under the repository's approved workflow. No additional handoff approvals are required before the local review.

- Task 1: complete. Static validator first failed for the eleven missing pages and absent navigation/contact destinations, then passed for all twelve implemented pages.
- Task 2: complete. Menu and image-dialog tests first failed against the static pages, then passed after enhancements were implemented. Full suite: six passing tests.
- Ruling: viewport media-query events are asynchronous, so the test waits for the observable navigation state. A native modal dialog permits Tab focus to the browser chrome; the test verifies the Close control starts focused and focus returns to the trigger on closing, without overriding native keyboard behavior.
- Final review: independent reviewer found no material defects; corrected minor current-section semantics and the stale instruction. Static validation, all six browser tests, and whitespace checks passed after corrections.
- Review limits: email and telephone delivery, additional browser engines/screen-reader combinations, and production deployment are not exercised. These do not prevent the requested local review.
