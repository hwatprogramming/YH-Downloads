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

- **The Windows version on YT Music Downloader's page.** Tabs picked 26 Oct, see
  [`downloads-page.md`](doc/live-design-choices/downloads-page.md), "The Windows
  version, on the same page". The installer goes in the APK's release,
  `yt-music-downloader`, as `yt-music-downloader-setup.exe`. Uploaded 26 Oct (the
  03:25 build), with the title "YT Music Downloader · Android 1.0 · Windows 1.0.0".
  **Built and pushed 26 Oct**, from the OK'd mockups in
  `.impeccable/mocks/both-platforms/src/`, with fresh 1.0.0 window shots (old and new
  side by side in `win-shots-1.0.0.png` beside `src/`, OK'd). README row has both
  files. How the build differs from the mockups is in `downloads-page.md`.
  - **Impeccable's finish for the new parts: done 26 Oct, both pages "ship".** All 7
    review fixes, my pick, plus the Windows gap under the switch I spotted after. The
    surface briefs and `DESIGN.md` cover the new parts. Details in
    [`doc/finish-review.md`](doc/finish-review.md), "Second review, 26 Oct". Pushed 26
    Oct.
  - **Open, my call:** the catalogue card jumps from 204px to 250px tall at 900 wide
    (only seen while resizing). Optional fix: versions under the buttons up to 999
    instead of 899.
  - **Left, mine:** delete the empty `D:\Songs` folder. Claude's safety check blocked it.
  - **Windows 1.1.0 is up, 2026-11-10**, after the version picker below. The release
    title is "YT Music Downloader · Android 1.0 · Windows 1.1.0". 1.1.0 asks before a
    playlist over 30 new songs, and has Pause / Cancel. 1.0.0 (the 26 Oct 18:41
    rebuild) stays downloadable as `yt-music-downloader-setup-1.0.0.exe`, in the menu.
    The Downloading picture is retaken from 1.1.0 and "Let it run" fixed, both OK'd and
    pushed 10 Nov.
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
- **Old canvas directions.** The three at
  <https://claude.ai/artifact/GyEG127fHrS5bLCeDf1BgY> are still in "To evaluate". Riso
  and Warm replaced them, so ask before moving them to "Past". Back up from the backlog
  2026-11-10.
  - [`.impeccable/questions/` (old picking-page state) and `.playwright-cli/` (Claude's
    check screenshots and logs) are in `.gitignore` since 2026-10-16, cause this repo is
    public.]
- Further off, in [`doc/backlog.md`](doc/backlog.md): the Support me page, parked till
  I can get into Ko-fi.

[Version picker: done 2026-11-10, A, the menu beside the button. Each app's versions
are in `<tag>/versions.js`, the update steps (here and in my global `CLAUDE.md`) add
a numbered copy and run `check-versions.bat`. Android gets the menu at its second
version, nothing to do for that. Details in
[`downloads-page.md`](doc/live-design-choices/downloads-page.md), "Picking an older
version".]
