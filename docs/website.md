# Website Specification

Status: first-pass portfolio design and scope approved by Jacob in chat on 2026-10-10; implementation requires local review and separate release approval.

This document is the source of truth for the website. Record approved process decisions in [plan.md](plan.md). The first pass replaces the temporary holding page.

## Purpose and audience

A personal portfolio for Beth Meyerson Sterkel, a mosaic and ceramic artist in Woodland Park, Colorado. Visitors can explore her work, learn about her materials and process, read her biography, and contact her about inquiries, commissions, or collaborations.

## Approved visual direction

A warm, contemporary gallery with ivory backgrounds, charcoal text, restrained terracotta accents, large serif headings, clean sans-serif body text, and generous spacing. Photographs of Beth's actual work lead the composition. The homepage introduction features the Mexican Tile Sun Table photograph. Responsive galleries use three columns on large screens, two on medium screens, and one on narrow screens. Image details preserve each complete artwork rather than cropping it. Subtle hover effects respect reduced-motion preferences.

## Shared structure and behavior

- Public brand: “Beth’s Mosaics.”
- Header: linked brand, Portfolio, Bio, Contact, and a prominent Contact Me link. Portfolio points to `index.html`, Bio to `bio/index.html`, and Contact to `contact/index.html`, with paths relative to the current page. Indicate the current page.
- Mobile: an accessible Menu button opens navigation. Escape closes it and restores focus. Navigation remains usable when JavaScript is disabled.
- Include a skip link to the main content and visible keyboard focus styles.
- Footer: Contact Me, `bethemeyerson@gmail.com` linked to `mailto:bethemeyerson@gmail.com`, `707-972-3040` linked to `tel:+17079723040`, Woodland Park, Colorado, page links, and “© 2026 Beth’s Mosaics.”
- Artwork pages have an image enlargement button, added only when JavaScript and native dialogs are available. The dialog displays the full image, has a named Close button, closes with Escape, and restores focus to its trigger. A click outside the dialog also closes it.
- All page content and navigation work without JavaScript; only menu enhancement and enlargement need JavaScript.
- All internal links, CSS, scripts, and images use relative URLs and work under the GitHub Pages `/bethsmosaics/` subpath.
- Publishable HTML, CSS, JavaScript, images, and fonts live only in `src/`. Pages require no build step or server-side service.
- Use optimized local WebP versions of the approved Wix photographs with responsive sizes where useful, meaningful alternative text, intrinsic dimensions, and lazy loading below the first screen. Use local fonts with system fallbacks.
- Retain the existing content, project details, titles, and biography. Omit Wix branding, project setup instructions, the placeholder `info@mysite.com` link, and the incorrect future copyright year. Do not add prices, availability claims, testimonials, or unverified content.

## Portfolio homepage

- **URL/file:** `/`, `src/index.html`.
- **Page title:** Beth’s Mosaics | Portfolio.
- **Description:** Mosaic and ceramic art by Beth Meyerson Sterkel in Woodland Park, Colorado. Explore colorful tables, wall hangings, and repurposed creations.
- **Sections, in order:**
  1. `portfolio-introduction`: artist name; heading “My Portfolio”; exact introduction “Welcome to my portfolio. Here you’ll find a selection of my work. Explore my projects to learn more about what I do.”; feature photograph linked to the Mexican Tile Sun Table page; an “Explore the work” link to `#portfolio` and a “Meet the artist” link to the Bio page.
  2. `portfolio`: nine linked artwork images with their titles and existing project types, in the order in the table below. A visible “Mosaics” heading introduces the work.
  3. `process`: heading “My Process”; exact paragraph “Mosaics are intricate works that bring color and personality to spaces. My creations are made with found and re-purposed materials, giving new life to previously loved items. My art is inspired by the beauty of Colorado, the Southwest, and Mexico.”; the existing materials photograph; three ordered photographic steps: “Step 1:” / “Finding furniture , frames, and tiles to re-purpose.”; “Step 2:” / “Preparing a design. Cutting and gluing tiles.”; “Step 3:” / “Grouting”. Use the associated process photographs below.
  4. Shared footer.

## Bio

- **URL/file:** `/bio/`, `src/bio/index.html`.
- **Page title:** Meet the Artist | Beth’s Mosaics.
- **Description:** Meet Beth Meyerson Sterkel, a Colorado mosaic and ceramic artist inspired by Talavera tiles, found materials, and repurposed furniture.
- **Section:** `artist-biography`, heading “Meet the Artist”; portrait and the exact biography below; “www.themountainartists.org” links to the existing source destination `http://www.themountainartists.org`; a Contact Me link.
- **Layout:** portrait and biography side by side on desktop, stacked on mobile. Shared header and footer.

Beth Meyerson Sterkel is a mosaic and ceramic artist currently living with her husband Mark, dog Skye, and cat Jasper in Woodland Park, Colorado. While Beth has enjoyed hand-building with clay for decades, she learned how to create mosaics art with colorful Mexican Talavera ceramic tiles while living in Bucerias, Mexico. Her pieces use a combination of Mexican ceramic tiles, found re-purposed tiles, and self-made clay tiles. As a devotee of recycling and re-purposing, Beth scours thrift stores and estate sales for the frames and bases.

Beth Meyerson Sterkel also teaches mosaics and is an active member of the non-profit, Mountain Artists.

## Contact

- **URL/file:** `/contact/`, `src/contact/index.html`.
- **Page title:** Contact | Beth’s Mosaics.
- **Description:** Contact Beth Meyerson Sterkel in Woodland Park, Colorado for mosaic inquiries, commissions, or collaborations.
- **Section:** `contact-details`, heading “Get in Touch”, subheading “We'd Love to Connect”.
- **Exact inquiry copy:** “For inquiries, commissions, or collaborations, please reach out via email or phone. I look forward to discussing your mosaic ideas and visions!”
- Display linked email and phone from the shared footer, labeled Email Beth and Call Beth, plus Woodland Park, Colorado. Include a Portfolio link.
- The first pass replaces the Wix contact form with direct email and phone links. There is no form, submission service, or simulated success message.
- Shared header and footer.

## Artwork pages

Each page is `src/portfolio/<slug>/index.html`, available at `/portfolio/<slug>/`. Use the project's exact title as its H1 and `<title>` prefix, followed by “ | Beth’s Mosaics”. Description: “<title>, a mosaic creation by Beth Meyerson Sterkel. View the artwork and contact Beth to learn more.”

Section order: `artwork-details` with Back to portfolio link, project type, title, full photograph, Project type and Location metadata, Contact Me link, and image enlargement control; `project-navigation` with Previous Project and Next Project links; shared footer. Previous/next follow the homepage order without wrapping; the first omits previous and the last omits next. “Studio (See Contact Section)” links to the Contact page; other locations remain source text, with no claim of current availability.

| Order | Title | Slug / image name | Project type | Location |
| --- | --- | --- | --- | --- |
| 1 | Mexican Tile Sun Table | `mexican-tile-sun-table` | Antique Pie Table | Studio (See Contact Section) |
| 2 | Dancing Women Table | `dancing-women-table` | Table | Studio (See Contact Section) |
| 3 | Talavera Tile Night Stand | `talavera-tile-night-stand` | Night Stand | The Marketplace, Woodland Park, Colorado |
| 4 | Deer In The Trees Wall Hanging | `deer-in-the-trees-wall-hanging` | Wall Hanging | Studio (See Contact Section) |
| 5 | Potted Plant Holder | `potted-plant-holder` | Plant Holder | Studio (See Contact Section) |
| 6 | Wooden Birds Wall Hanging | `wooden-birds-wall-hanging` | Wall Hanging | Studio (See Contact Section) |
| 7 | Mountain Scene Wall Hanging | `mountain-scene-wall-hanging` | Wall Hanging | Studio (See Contact Section) |
| 8 | Black Bear Wall Hanging | `black-bear-wall-hanging` | Wall Hanging | Pike's Peak Boutique, Cascade, Colorado |
| 9 | Tree of Life Table | `tree-of-life-table` | Table | Studio (See Contact Section) |

## Image references and provenance

Fetched from the public Wix site supplied by Jacob, `https://www.bethsmosaics.com/`, on 2026-10-10. Preserve the photographs as the artwork source. Files are `assets/images/<name>.webp`; artwork and process photographs also have `<name>-small.webp` for responsive loading. Do not upscale the original portrait. Image enlargement uses the larger local image.

| Image name | Alternative text | Original source |
| --- | --- | --- |
| `mexican-tile-sun-table` | Colorful Talavera sun mosaic in an ornate round wooden table. | https://static.wixstatic.com/media/0ae6c4_dc68c2da15e74185a88ac587fba7a238~mv2.jpg |
| `dancing-women-table` | Round mosaic table with dancing women beneath a sun and mountain landscape. | https://static.wixstatic.com/media/0ae6c4_4d3bedceb8404d699e709cdf414e969f~mv2.jpg |
| `talavera-tile-night-stand` | Square night stand with blue, yellow, and orange Talavera tiles. | https://static.wixstatic.com/media/0ae6c4_b215f0ee618d42a68c0d84eadf6e5d46~mv2.jpg |
| `deer-in-the-trees-wall-hanging` | Blue and white ceramic tile wall hanging depicting deer among trees. | https://static.wixstatic.com/media/0ae6c4_32396dc3f5984b9287bd8264743f4bc0~mv2.jpg |
| `potted-plant-holder` | Red ceramic tile plant holder with a decorative bird tile. | https://static.wixstatic.com/media/0ae6c4_f028e4f0b98343a0bf2ce7abd9044ccc~mv2.jpg |
| `wooden-birds-wall-hanging` | Two patterned ceramic birds on a pale blue mosaic in a wooden frame. | https://static.wixstatic.com/media/0ae6c4_0f87af6935dc479aa06cb9caf37bb93f~mv2.jpg |
| `mountain-scene-wall-hanging` | Mountain landscape tile displayed in an octagonal wooden frame. | https://static.wixstatic.com/media/0ae6c4_205e96739514437ea6950140707dff34~mv2.jpg |
| `black-bear-wall-hanging` | Black bear and forest silhouettes on an orange tile wall hanging. | https://static.wixstatic.com/media/0ae6c4_7f4a44245e994a4a8a59566237d78697~mv2.jpg |
| `tree-of-life-table` | Round wooden table with a colorful tree of life mosaic. | https://static.wixstatic.com/media/0ae6c4_34866836dae641f6b0353494b197c1b7~mv2.jpg |
| `beth-meyerson-sterkel` | Beth Meyerson Sterkel sitting outdoors with her dog. | https://static.wixstatic.com/media/0ae6c4_8973e07cee0e4b00bf5c78eef22fb039~mv2.png |
| `process-materials` | Reclaimed wooden table and tray with ceramic pieces ready to be repurposed. | https://static.wixstatic.com/media/0ae6c4_06b1ef7b92214b57962d0e337eddfe37~mv2.jpg |
| `process-find` | Found furniture and colorful ceramic tiles gathered for a mosaic. | https://static.wixstatic.com/media/0ae6c4_0368d6893c1d488c9cf8b6c806a6ba51~mv2.jpg |
| `process-design` | A tree mosaic design with cut ceramic tiles being arranged in a frame. | https://static.wixstatic.com/media/0ae6c4_3ff2dc3c849a464685213774b8afe857~mv2.jpg |
| `process-grout` | Completed tree mosaic with grout between the colorful tile pieces. | https://static.wixstatic.com/media/0ae6c4_0d857d20dc5c4a6095d525085c6779d8~mv2.jpg |

## UI labels

Routine controls use the labels specified above plus “Menu”, “Close”, “View full image”, and “Back to portfolio”. Gallery item links use the exact artwork title. Decorative icons have no additional accessible name.

## Implementation checks

- Compare all 12 pages, section order, exact copy, project metadata, and images with this specification.
- Validate every local destination, asset, fragment, and image alternative text.
- Exercise mobile navigation, Escape, focus restoration, image enlargement, and previous/next links in a real browser.
- Check desktop and mobile layouts, 320-pixel screens, image loading, reduced motion, and JavaScript-disabled browsing.
- Check nested page URLs under the `/bethsmosaics/` subpath.
- Provide a local preview and representative screenshots before requesting release approval.
- Keep documentation and tooling outside the published artifact.
