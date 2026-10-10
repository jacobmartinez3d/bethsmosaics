# Website Specification

Status: temporary homepage copy approved; the full portfolio content and design remain to be planned.

This document is the source of truth for the website. Propose changes here for human review before translating them into `src/`. Record approved process decisions in [plan.md](plan.md).

## Purpose and audience

Purpose: a personal/portfolio website for Mom.

The temporary site uses the public name “Beth’s Mosaics.” Intended visitors and the full portfolio's goals still need to be discussed.

## Shared site structure

The temporary site has a single homepage without navigation, header, footer, images, or interactions. Use a plain, readable, centered heading that wraps on small screens. This holding page does not establish the final site's visual design.

## Pages

### Temporary homepage

- **Page name:** Home.
- **URL:** `/`, relative to the website root (currently `/bethsmosaics/` on GitHub Pages).
- **Purpose:** confirm hosting is working while the full website is developed.
- **Page title:** Beth’s Mosaics.
- **Description:** Beth’s Mosaics — Coming soon.
- **Section ID:** holding-message.
- **Exact visible heading:** Beth’s Mosaics — Coming soon.
- **Other content, images, links, and interactions:** none.

Jacob selected this exact temporary copy in chat and requested a working hosted site before further development. Future portfolio pages and changes follow the review workflow in `plan.md`.

Use the following format for future proposed pages. Replace guidance with approved details rather than publishing it as content.

### Page specification format

- **Page name:** human-readable name.
- **URL:** intended URL relative to the website root.
- **Purpose:** what the visitor should learn or do.
- **Page title and description:** browser title and search description.
- **Sections, in order:** give each section a stable descriptive ID, heading, exact text, links, image references and alternative text, and intended interactions.
- **Layout and visual guidance:** plain-language instructions as needed.

Use image paths relative to `src/`, such as `assets/images/portrait.jpg`. Distinguish exact website copy from instructions for the agent. For links and interactions, describe both the visible label and destination or result.

## Implementation checks

- Every implemented page and section corresponds to approved content here.
- Text matches the approved copy; agents do not invent missing copy.
- Navigation, links, images, and interactions work on desktop and mobile.
- Shared elements are consistent across pages.
- URLs and asset paths work under the GitHub Pages repository subpath.
