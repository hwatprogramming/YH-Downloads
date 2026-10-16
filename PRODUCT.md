# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: plain static HTML and CSS, no build step. A catalogue page plus one page
per app, since 2026-10-14. GitHub Pages serves the files from this repo as they are. I
said "you pick" on 2026-10-13. Claude picked this cause every app's page has its own
theme, which a shared template would fight, and cause I can preview a page by opening
the file.

## Users

Three kinds of visitor, all confirmed 2026-10-13:

- **Me.** Getting my own apps onto my own phone and PC.
- **People I know.** Friends, family or colleagues I send the link to.
- **Anyone.** Strangers who land on it and don't know me or the apps.

## Product Purpose

A catalogue of the apps I've built, each ready to download. The catalogue page shows
every app with its name, one line and a download button. Each app also has its own
page with what it does, its download links, a picture of it, and how to set it up and
use it. [Was "one long page" till 2026-10-14. Why it changed is in
`doc/live-design-choices/downloads-page.md`.]

Done means the site is live and the first app is on it.

## Positioning

- Each app's page takes its theme from the app it's for. The catalogue and the header
  have the site's own theme, so they read as separate from any one app.
- Built files only. Each app's source code stays in its own private repo.
- A download link never changes. An update replaces the file behind the same link.

## Operating Context

- The files are GitHub Release assets on `hwatprogramming/YH-Downloads`, one release per
  app. Link shape:
  `https://github.com/hwatprogramming/YH-Downloads/releases/download/<tag>/<file name>`.
  The rules are in [`doc/uploading-a-build.md`](doc/uploading-a-build.md).
- Files are APKs (Android) and exes (Windows). An APK from here installs outside the
  Play Store.
- Claude uploads each build and designs each app's section when I ask. I opted out of
  adding apps by myself for this repo.
- This repo is public. Nothing private goes on the page or in the repo.

## Capabilities and Constraints

- An app's page has the app's name, what it does, its download links and a picture of
  the app.
- Under that, every app's page has the same parts: Setup, How to use it, What it's used
  for, What it isn't, and an FAQ. Setup and the FAQ are left out when an app has none.
  My ask, 2026-10-14.
- First app: YT Music Downloader. Android APK, Android 10 and up, arm64 phones only.
- YT Music Downloader 1.0 is uploaded, release-signed, as release `yt-music-downloader`.
  The download links work. Since 2026-10-16.
- An app's page shows the version its button downloads, and the version's date,
  beside the button, so people can tell they have the latest. My ask, 2026-10-16. Each
  update edits that line on the page.
- YT Music Downloader's page shows three real screenshots of the app: the Download
  tab, History and Help. Decided 2026-10-16.

## Brand Commitments

- The page is called "YH Downloads".
- Each section gets its own theme, based on the project it's built on. My words,
  2026-10-13. [Sections became app pages 2026-10-14.]
- The header and the catalogue get a theme of their own, different from every app's,
  so the site doesn't read as one app's landing page. My ask, 2026-10-14. It's dark,
  my preference the same day. Professional and only slightly stylised: warm charcoal,
  Figtree, and a champagne-gold title (`#E6C88E`), close to YT Music Downloader's gold
  but not the same. No pink and no Bagel Fat One there. Each app's card and button on
  the catalogue wear that app's own colours.
- YT Music Downloader's icon is a dark download arrow with sound bars beside it, on a
  gold tile. Gold `#EDBB4E`, dark `#16202C`. The app is named "YT Music Downloader" on
  the phone since 2026-10-14. It was "Music Downloader" before that.
- YT Music Downloader's page wears the app's own look, Liner Notes, since 2026-10-16:
  navy `#0F151D`, warm off-white text, one gold, Barlow Condensed for the name and the
  section headings (my call 2026-10-16), Roboto for the rest, hairlines. It's in the app
  repo's `DESIGN.md`.

## Evidence on Hand

- YT Music Downloader's icon as a vector:
  `../Mobile-Youtube-Music-Downloader/app/src/main/res/drawable/ic_launcher_foreground.xml`.
- Screenshots of version 1.0 on the phone:
  `../Mobile-Youtube-Music-Downloader/.impeccable/review/after-fixes/`. They show the
  phone's status bar with the carrier name, so the page's copies have it cut off. Those
  copies are in `.impeccable/mocks/app-page/src/assets/`. History's songs below Smells
  Like Teen Spirit are real downloads and are blanked there. Older shots, from when it
  was still called Music Downloader, are in the app repo's
  `doc/reference/app-before-redesign/`.
- My own phone screenshots from 16 Oct: sharing and pasting in YT Music, the
  big-playlist notification, and installing 1.0 off the live site (Play Protect,
  Install, App installed). Cropped copies are in `yt-music-downloader/assets/`, with
  the status bar, album covers, other apps' icons and the link's share code left out.
- The facts in its section's Setup, How to use it, What it isn't and FAQ come from the
  app repo's `doc/design-brief.md`, `doc/live-design-choices/` and
  `doc/reference/target-device.md`, checked 2026-10-14. They were brought up to 1.0
  from its `doc/for-yh-downloads.md` and its Help text (`help_faq` in
  `app/src/main/res/values/strings.xml`), 2026-10-16.
- Why I built YT Music Downloader, in my words:
  `../Mobile-Youtube-Music-Downloader/doc/repo-journal.md`.
- Nothing else. No user counts, reviews or ratings exist, so none go on the page.

## Product Principles

1. Every section gets the visitor to the file. The download is never far from where
   they're looking.
2. A stranger can tell what an app does from one plain line.
3. Each section belongs to its app: its name, its picture, its theme.
4. Links don't break. An update replaces the file behind the same link, and the page
   only changes its version line. [Was "an update never needs an edit to the page"
   till 2026-10-16, when the version went on the page.]
5. Only what's true and public goes on the page.
