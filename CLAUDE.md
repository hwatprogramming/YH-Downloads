# YH Downloads

Public repo that holds the downloads for apps I've built. Built files only (APK, exe),
attached to Releases with one release per app. No source code goes in here, cause each
app's code stays in its own private repo.

## How to work on this

[General working rules live in `~/.claude/CLAUDE.md` and the AI Behaviour Augments
output style. Only rules specific to this project go here.]

- **The downloads page is `README.md` for now**, a table with one row per app. It's
  moving to a GitHub Pages site, my call 2026-10-13: a catalogue page plus a page per
  app, my call 2026-10-14. The site isn't built yet. The decisions are in
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

- **Design the site with Impeccable.** It's moving from `README.md` to a GitHub Pages
  site, my call 2026-10-13: a catalogue page plus a page per app, since 2026-10-14.
  Plain HTML and CSS. Product facts are in [`PRODUCT.md`](PRODUCT.md), and every
  decision with its reasoning is in
  [`downloads-page.md`](doc/live-design-choices/downloads-page.md). Where it stands:
  - **Catalogue page, picked:** Warm,
    `.impeccable/mocks/catalogue/src/soft-warm.html`. Warm charcoal, Figtree, a
    champagne-gold title, and each app's card and button in that app's own colours.
  - **YT Music Downloader's page:** the Two-Ink Riso mockup, dark,
    `.impeccable/mocks/decision/src/challenger-risograph.html`. It has the five parts
    every app page gets, phone and tablet layouts, and the Warm header with a chip per
    app, sticky.
  - **Waiting on me:** I'm redesigning YT Music Downloader's own look (font, UI and so
    on) in `../Mobile-Youtube-Music-Downloader`. When I say it's done, read the new
    design from that repo, then update its page here, its card and chip on the
    catalogue, and PRODUCT.md's lines on its icon and colours.
  - **Open:** the FAQ's "Is this legal?", left out till I decide. A phone cut-off I saw
    that Claude couldn't reproduce. Whether the sticky header goes to one row on
    phones.
  - **Leftovers:** `.impeccable/questions/` (old picking-page state) and
    `.playwright-cli/` (Claude's check screenshots and logs) aren't committed, cause
    this repo is public. The three canvas directions at
    <https://claude.ai/artifact/GyEG127fHrS5bLCeDf1BgY> are still in "To evaluate".
    Riso and Warm replaced them, so ask before moving them to "Past".
- **Build the picked look and turn GitHub Pages on.** The catalogue and YT Music
  Downloader's page, from the mockups. Pages is off as of 2026-10-13.
  `downloads-page.md` and `uploading-a-build.md` still describe the README page, so
  update both in the same change.
- **Upload YT Music Downloader and put it on the site.** It's the first app.
  Its repo is `../Mobile-Youtube-Music-Downloader`. Tag and file name are
  `yt-music-downloader`, by the upload guide's rule.
