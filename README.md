# Mom's Website

A personal/portfolio website maintained through chat, with GitHub Pages hosting.

## Structure

```text
src/                    Ready-to-publish website files
  assets/css/           Styles
  assets/js/            Browser scripts
  assets/images/        Images
docs/plan.md            Approved decisions and workflow
docs/website.md         Authoritative website specification
AGENTS.md               Instructions for agents
.github/workflows/      GitHub Actions checks and publishing
```

The portfolio includes Portfolio, Bio, Classes & Shows, and Contact pages, plus Beth’s mosaic process. Artwork photographs open a responsive lightbox with full-size images, photo navigation, and accessible keyboard controls. There are no individual detail pages or artwork locations; the nine former artwork URLs redirect to the gallery. It reuses photographs and content from the original Wix site. The site uses plain HTML, CSS, JavaScript, local fonts, and optimized local images; no installation or build step is needed to preview or publish it.

## Development

Start with [the website specification](docs/website.md) and follow [the approved workflow](docs/plan.md). Review the specification before implementation, then review the rendered result before authorizing release.

Use atomic, Conventional Commits: one coherent change per commit, with messages such as `feat(gallery): add approved mosaic gallery`, `fix(navigation): correct portfolio link`, or `docs: update website specification`. Include related specification and documentation updates with their implementation. The initial scaffold uses `chore: initialize website development scaffold`.

Preview locally:

```sh
python3 -m http.server 8000 --directory src
```

Open `http://localhost:8000`. Stop the server with Ctrl+C.

Run the standard-library validation:

```sh
python3 tools/check_site.py
```

It checks four content pages and nine legacy redirects, local links and fragments, contact destinations, image references and alternative text, and the publishable directory boundary. GitHub pull requests run this check too.

Optional real-browser checks require Chrome and the Python `playwright` package. These are development tools; they are never part of the published site:

```sh
python3 -m venv /tmp/beth-site-qa
/tmp/beth-site-qa/bin/pip install playwright
/tmp/beth-site-qa/bin/python tools/check_browser.py
```

The browser suite serves only `src/` on a temporary local port under `/bethsmosaics/`, testing repository-subpath hosting, widths from 320 to 1440 pixels, mobile navigation, lightbox navigation/dismissal, viewport fit and keyboard focus, direct-image fallback, legacy redirects, Classes & Shows contact navigation, reduced motion, image loading, and JavaScript-disabled browsing. Set `BETH_CHROME` to a Chrome executable path when it is not on `PATH`.

The source pages are ready-to-publish files. To edit content, update the approved specification and the corresponding HTML together. Shared presentation and behavior live in `src/assets/css/site.css` and `src/assets/js/site.js`. For class/show announcements, supply Beth’s event title, date/time, venue, description, and optional information link through chat. No events are invented; the Classes & Shows page directs visitors to contact Beth until details are supplied. Font licenses are included in `src/assets/fonts/`; photograph provenance is recorded in `docs/website.md`.

## GitHub setup

Jacob has initialized Git on `main` and connected `git@github.com:jacobmartinez3d/bethsmosaics.git` as `origin`. Use a public repository for free GitHub Pages unless an eligible paid plan is chosen for private-repository hosting.

Git metadata writes may require sandbox escalation in this workspace. Updated session permissions allow approved Git operations; the initial scaffold commit and push are authorized. Future merges and releases still follow the chat approval workflow.

After reviewing and approving the initial setup for publication:

1. Commit and push the approved setup to the repository.
2. In **Settings → Pages**, select **GitHub Actions** as the publishing source.
3. Restrict the `github-pages` deployment environment to `main`.
4. Configure branch rules for `main` to require pull requests and the `Check site` status check where available.

Agents need explicit chat approval to merge a reviewed implementation. GitHub does not interpret chat approval; the agent follows this policy in `AGENTS.md`. Branch checks complement that policy.

## Publishing

Pull requests run `Check site` without publishing. Pushes to `main` affecting `src/` or the Pages workflow run checks and publish only `src/`. Manual workflow runs are limited to publishing from `main` and require release approval too. There is no build step or additional hosting service.

Until `src/index.html` exists, the check reports that the site awaits implementation and skips deployment. Once it exists, the workflow requires a nonempty homepage and runs the static site validator before uploading it. Automated checks supplement content, interaction, and visual review.

After deployment, check the Actions result and open the published URL to verify the site. Hosted pull-request previews are not part of the initial setup.

For recovery, prepare a revert of the affected change, validate it, obtain release approval, and merge it so Actions republishes the restored version.
