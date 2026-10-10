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

The homepage and site content have not been approved or implemented. Empty asset folders contain `.gitkeep` files solely to preserve their structure in Git; remove those placeholders as real assets are added.

## Development

Start with [the website specification](docs/website.md) and follow [the approved workflow](docs/plan.md). Review the specification before implementation, then review the rendered result before authorizing release.

Use atomic, Conventional Commits: one coherent change per commit, with messages such as `feat(gallery): add approved mosaic gallery`, `fix(navigation): correct portfolio link`, or `docs: update website specification`. Include related specification and documentation updates with their implementation. The initial scaffold uses `chore: initialize website development scaffold`.

Once a homepage exists, preview locally:

```sh
python3 -m http.server 8000 --directory src
```

Open `http://localhost:8000`. Stop the server with Ctrl+C. Until `src/index.html` exists, this shows a directory listing rather than a website.

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

Until `src/index.html` exists, the check reports that the site awaits implementation and skips deployment. Once it exists, the workflow requires a nonempty homepage before uploading it. This readiness check does not replace content, link, interaction, or visual review.

After deployment, check the Actions result and open the published URL to verify the site. Hosted pull-request previews are not part of the initial setup.

For recovery, prepare a revert of the affected change, validate it, obtain release approval, and merge it so Actions republishes the restored version.
