# YH Downloads

Public repo that holds the downloads for apps I've built. Built files only (APK, exe),
attached to Releases with one release per app. No source code goes in here, cause each
app's code stays in its own private repo.

## How to work on this

[General working rules live in `~/.claude/CLAUDE.md` and the AI Behaviour Augments
output style. Only rules specific to this project go here.]

- **The downloads page is `README.md` for now**, a table with one row per app. It's
  moving to a GitHub Pages website, my call 2026-10-13, and the site isn't built yet.
  Both decisions are in
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
- **Where each feature lives** is in [`doc/feature-map.md`](doc/feature-map.md). Check it
  before building anything that adds UI, and update it in the same change.

## Next

[The nearest 3-4 tasks. Everything further off is in [`doc/backlog.md`](doc/backlog.md).]

- **Design the page with Impeccable.** The page is moving from `README.md` to a GitHub
  Pages website, my call 2026-10-13. Plain HTML and CSS, Claude's pick after I said "you
  pick". Product facts are in [`PRODUCT.md`](PRODUCT.md). Each app's section gets its
  own theme, taken from that app. Where it stands: `PRODUCT.md` is written. Five mockups
  of the page's first screen are in `.impeccable/mocks/decision/` (pictures, with their
  HTML in `src/`), and I haven't picked one yet. The names are The Cartridge Rack,
  Inside the Icon, Two-Ink Riso, Session Title Card and The category standard.
  Impeccable's seed key for this direction round is `f28573c3`. What each mockup is,
  and what's settled so far, is in
  [`downloads-page.md`](doc/live-design-choices/downloads-page.md), "Moving to a website".
  [Open: a "re-roll, safer" click came through from Impeccable's picking page and I
  haven't said if I meant it. `.impeccable/questions/` is leftover state from that
  page, and it's not committed.]
  [Three earlier directions are on a design canvas, still in "To evaluate" and not
  picked: <https://claude.ai/artifact/GyEG127fHrS5bLCeDf1BgY>. I asked for Impeccable
  after seeing them.]
- **Build the picked look and turn GitHub Pages on.** Pages is off as of 2026-10-13.
  `downloads-page.md` and `uploading-a-build.md` still describe the README page, so
  update both in the same change.
- **Upload Music Downloader and put its section on the page.** It's the first app. Its
  repo is `../Mobile-Youtube-Music-Downloader`.
