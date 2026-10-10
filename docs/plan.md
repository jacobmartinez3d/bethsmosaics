# Website Development and Publishing Plan

## Approved decisions

- Build a personal/portfolio website for Mom.
- Host on GitHub Pages under Jacob's GitHub account initially.
- Prefer free hosting, excluding domain registration and agent operating costs.
- Default to a public repository for GitHub Free; confirm visibility during remote setup.
- Maintain the site through a Buzz community: chat requests drive agent-managed code, Git history, and publishing.
- Keep ready-to-publish HTML, CSS, JavaScript, and assets in `src/`.
- Keep this decision record in `docs/plan.md`.
- Use `docs/website.md` as the authoritative specification for pages, URLs, section order, exact text, image references, and intended behavior.
- Review specification changes before implementation.
- Review implemented changes locally before release; screenshots may supplement browser review.
- Explicit chat approval of the implemented result authorizes merging its pull request. GitHub Actions then publishes `src/` from `main`.
- Use atomic, Conventional Commits. Each commit represents one coherent change, including its related specification and documentation. The initial repository scaffold is one setup change: `chore: initialize website development scaffold`.
- Jacob explicitly authorized creating and pushing the initial scaffold commit to `origin/main`. This authorization covers the initial setup, not future releases.

## Change workflow

1. Discuss the requested change in chat.
2. Propose the corresponding Markdown specification changes and wait for approval.
3. Update the approved specification and implement it on a feature branch.
4. Validate the result and open a pull request with a concise summary and verification evidence.
5. Provide a local browser preview and screenshots when helpful.
6. Wait for explicit chat approval of that implementation before merging.
7. Merge the approved pull request and verify the GitHub Pages deployment and live site.

Material revisions after release approval require renewed approval. Technical fixes that preserve the specified site can leave `docs/website.md` unchanged, but still require implementation review and release approval. Approval applies to the reviewed change, not future changes.

## Validation and recovery

- Compare pages, section order, text, and behavior with the specification.
- Check links, asset loading, interactions, and desktop/mobile layouts.
- Use relative links that work under a GitHub Pages repository subpath.
- Verify the live site after deployment; documentation must remain outside the published artifact.
- Recover from a bad release by reverting the affected Git change and republishing. Obtain explicit approval for the revert release through the same review workflow.

## Repository setup implementation

- [x] Record approved decisions and add a website specification template without inventing site content.
- [x] Create `src/assets/css/`, `src/assets/js/`, and `src/assets/images/` with Git placeholders.
- [x] Document local preview, repository setup, publishing, and agent responsibilities.
- [x] Add a GitHub Actions workflow that checks pull requests and publishes only `src/` on `main`.
- [x] Initialize the Git repository and connect `git@github.com:jacobmartinez3d/bethsmosaics.git` as `origin` under Jacob's account.
- [x] Rename the initial branch from `master` to `main`.
- Initial scaffold release is authorized: commit as `chore: initialize website development scaffold` and push to `origin/main`. Verify local and remote commit hashes after pushing.
- [ ] Enable GitHub Pages with GitHub Actions as its publishing source; restrict the `github-pages` environment to `main`.
- [ ] Configure branch rules for `main` to require pull requests and the `Check site` status check where available. Agents must still obtain chat approval before merging.
- [ ] Approve the initial website specification and implement the homepage.
- [ ] Approve the first release, merge, and verify the live site.

## Current boundaries

The GitHub repository is `jacobmartinez3d/bethsmosaics`. The initial website content, design, and domain have not been decided. No homepage is created until its specification is approved. The deployment workflow deliberately skips publishing while `src/index.html` is absent.

Jacob initialized Git, configured `origin`, and renamed the initial branch to `main`. Git writes previously failed inside the sandbox; updated permissions now allow approved Git operations through sandbox escalation. The initial scaffold commit and push are explicitly authorized. No homepage is present, so pushing the scaffold does not publish a website.
