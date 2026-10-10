# Website Specification

Status: awaiting initial content and design approval. This template does not authorize website implementation.

This document is the source of truth for the website. Propose changes here for human review before translating them into `src/`. Record approved process decisions in [plan.md](plan.md).

## Purpose and audience

Purpose: a personal/portfolio website for Mom.

Her preferred public name, intended visitors, and what visitors should do still need to be discussed.

## Shared site structure

Define approved navigation, header, footer, shared text, visual direction, and accessibility requirements here before implementation.

## Pages

No pages or sections have been approved yet. Use the following format for each proposed page. Replace guidance with approved details rather than publishing it as content.

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
