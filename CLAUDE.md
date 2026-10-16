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

[Finished 2026-10-16: Impeccable's finish, both pages "ship". All 11 review fixes, a
new phone card, picture notes in the 15 screenshots, a second review round with every
fix resolved, and [`DESIGN.md`](DESIGN.md) written from the live pages. Details in
[`doc/finish-review.md`](doc/finish-review.md). Barlow Condensed is for the name and
the section headings, my call the same day.]

[Stopped here 16 Oct, my call. By the done line from 13 Oct (page live in that layout,
first app on it) the site is done. Nothing below blocks that.]

- **Tick the repo journal's goals, mine to do.** Both are met. Goal 1 still says "one
  long page, a section per app", but it became a catalogue page plus a page per app on
  14 Oct. Claude offered to log that change with `log` and reword the goal. Not
  answered yet.
- **Open question on YT Music Downloader's page:** whether the sticky header goes to one
  row on phones. Reviewer: it can't fit, so keep two rows, or unstick it on phones only.
  Their view is in [`doc/finish-review.md`](doc/finish-review.md).
  [The phone cut-off I saw: it was "DOWNLOADER" in the stand-in font on a slow first
  load. Fixed by review fix #11, checked on my phone 16 Oct.]
  [The FAQ's "Is this legal?" is left out for good, my call 2026-10-16.]
- **Two small layout things Claude found 16 Oct, not picked yet:**
  - At exactly 760px wide, two notes in What it's for's "Not" list ("your music app
    plays them", "songs stay on your phone") poke past the screen edge, so the page
    scrolls sideways. It was there before the fixes.
  - With the new phone card, the download button runs the card's full width up to
    759px, so on a small tablet it's about 690px wide. Cap it there? Not answered.
- **Leftovers:** `.impeccable/questions/` (old picking-page state) and
  `.playwright-cli/` (Claude's check screenshots and logs) are in `.gitignore` since
  2026-10-16, cause this repo is public. The three canvas directions at
  <https://claude.ai/artifact/GyEG127fHrS5bLCeDf1BgY> are still in "To evaluate".
  Riso and Warm replaced them, so ask before moving them to "Past".
- Further off, in [`doc/backlog.md`](doc/backlog.md): the Support me page, parked till
  I can get into Ko-fi.
