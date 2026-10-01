# YH Downloads

Public repo that holds the downloads for apps I've built. Built files only (APK, exe),
attached to Releases with one release per app. No source code goes in here, cause each
app's code stays in its own private repo.

## How to work on this

[General working rules live in `~/.claude/CLAUDE.md` and the AI Behaviour Augments
output style. Only rules specific to this project go here.]

- **The downloads page is `README.md`**, a table with one row per app. Why it's not a
  website: [`doc/live-design-choices/downloads-page.md`](doc/live-design-choices/downloads-page.md).
- **Uploading a build** is covered in [`doc/uploading-a-build.md`](doc/uploading-a-build.md).
  It's written for a Claude working in one of the app repos. Follow it for every upload.
- **Design choices** go in [`doc/live-design-choices/`](doc/live-design-choices/README.md),
  one file per feature. Keep the reasoning there, not here.
- **Tasks past the nearest 3-4** go in [`doc/backlog.md`](doc/backlog.md). Same for a
  task that's too deep to carry here. When a task leaves `Next`, pull the top backlog
  item up.
- **Reference material** lives in [`doc/reference/`](doc/reference/README.md). Check it
  before designing or building anything that has a target to match.
- **Where each feature lives** is in [`doc/feature-map.md`](doc/feature-map.md). Check it
  before building anything that adds UI, and update it in the same change.

## Next

[The nearest 3-4 tasks. Everything further off is in [`doc/backlog.md`](doc/backlog.md).]
