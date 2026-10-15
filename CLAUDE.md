# YH Downloads

Public repo that holds the downloads for apps I've built. Built files only (APK, exe),
attached to Releases with one release per app. No source code goes in here, cause each
app's code stays in its own private repo.

## How to work on this

[General working rules live in `~/.claude/CLAUDE.md` and the AI Behaviour Augments
output style. Only rules specific to this project go here.]

- **The downloads page is a GitHub Pages site**, live since 2026-10-16 at
  <https://hwatprogramming.github.io/YH-Downloads/>. `index.html` is the catalogue,
  and each app has its own page, like `yt-music-downloader/index.html`. Edit those
  files, not the mockups in `.impeccable/mocks/`, which are the record. `README.md`
  keeps a table row per app as the repo's front page. The decisions are in
  [`doc/live-design-choices/downloads-page.md`](doc/live-design-choices/downloads-page.md).
- **Uploading a build** is covered in [`doc/uploading-a-build.md`](doc/uploading-a-build.md).
  It's written for a Claude working in one of the app repos. Follow it for every upload.
- **Design choices** go in [`doc/live-design-choices/`](doc/live-design-choices/README.md),
  one file per feature. Keep the reasoning there, not here.
- **Tasks past the nearest 3-4** go in [`doc/backlog.md`](doc/backlog.md). Same for a
  task that's too deep to carry here. When a task leaves `Next`, pull the top backlog
  item up.
- **Reference material** lives in [`doc/reference/`](doc/reference/README.md). Check it
  before designing or building anything that has a target to match.

## Next

[The nearest 3-4 tasks. Everything further off is in [`doc/backlog.md`](doc/backlog.md).]

[Shipped 2026-10-16: the site is live, and YT Music Downloader 1.0 is uploaded,
release-signed, as release `yt-music-downloader`. The catalogue is the Warm mockup,
and the app page is the Riso layout in the app's Liner Notes look. All in
[`downloads-page.md`](doc/live-design-choices/downloads-page.md).]

- **Pick fixes from Impeccable's finish review, then finish it,** next session. The
  review ran 2026-10-16 and both pages came back "fix": small fixes, no redesign.
  Nothing changed yet. The 11 fixes, the picture-note wording waiting for my OK, and
  the steps left after I pick (retake screenshots, a fresh reviewer scores the fixes,
  `DESIGN.md`, update `downloads-page.md`, commit and push) are all in
  [`doc/finish-review.md`](doc/finish-review.md).
  - Direction contracts for both pages got written for the review, from what shipped,
    in `.impeccable/surfaces/`.
- **Open questions on YT Music Downloader's page**, the reviewer's view on both is in
  [`doc/finish-review.md`](doc/finish-review.md):
  - Whether the sticky header goes to one row on phones. Reviewer: it can't fit.
  - A phone cut-off I saw on the old Riso page. Reviewer's best guess: "DOWNLOADER" in
    the fallback font on a slow first load.
  [The FAQ's "Is this legal?" is left out for good, my call 2026-10-16.]
- **Leftovers:** `.impeccable/questions/` (old picking-page state) and
  `.playwright-cli/` (Claude's check screenshots and logs) are in `.gitignore` since
  2026-10-16, cause this repo is public. The three canvas directions at
  <https://claude.ai/artifact/GyEG127fHrS5bLCeDf1BgY> are still in "To evaluate".
  Riso and Warm replaced them, so ask before moving them to "Past".
- Further off, in [`doc/backlog.md`](doc/backlog.md): the Support me page, parked till
  I can get into Ko-fi.
