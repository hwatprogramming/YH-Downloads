# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: plain static HTML and CSS, one page, no build step. GitHub Pages serves the
files from this repo as they are. I said "you pick" on 2026-10-13. Claude picked this
cause every app's section has its own theme, which a shared template would fight, and
cause I can preview the page by opening the file.

## Users

Three kinds of visitor, all confirmed 2026-10-13:

- **Me.** Getting my own apps onto my own phone and PC.
- **People I know.** Friends, family or colleagues I send the link to.
- **Anyone.** Strangers who land on it and don't know me or the apps.

## Product Purpose

One long page of the apps I've built, each ready to download. Every app has its own
section with what the app does, its download links and a picture of it.

Done means the page is live and the first app is on it.

## Positioning

- Each section takes its theme from the app it's for, so the page changes look as you
  scroll from one app to the next.
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

- A section has the app's name, what it does, its download links and a picture of the app.
- First app: Music Downloader. Android APK, Android 10 and up, arm64 phones only.
- No release is uploaded yet, so no download link works yet.
- **Undecided:** whether the page shows version numbers. The README page left them out
  so an update needs no commit. Not confirmed for the website.
- **Undecided:** which picture of Music Downloader goes on the page.

## Brand Commitments

- The page is called "YH Downloads".
- Each section gets its own theme, based on the project it's built on. My words,
  2026-10-13.
- Music Downloader's icon is a dark download arrow with sound bars beside it, on a gold
  tile. Gold `#EDBB4E`, dark `#16202C`. The app is named "Music Downloader" on the phone.

## Evidence on Hand

- Music Downloader's icon as a vector:
  `../Mobile-Youtube-Music-Downloader/app/src/main/res/drawable/ic_launcher_foreground.xml`.
- Screenshots of Music Downloader on the phone:
  `../Mobile-Youtube-Music-Downloader/doc/reference/app-before-redesign/`. Song names in
  them are made up. They show the phone's status bar with the carrier name.
- Why I built Music Downloader, in my words:
  `../Mobile-Youtube-Music-Downloader/doc/repo-journal.md`.
- Nothing else. No user counts, reviews or ratings exist, so none go on the page.

## Product Principles

1. Every section gets the visitor to the file. The download is never far from where
   they're looking.
2. A stranger can tell what an app does from one plain line.
3. Each section belongs to its app: its name, its picture, its theme.
4. Links don't break. An update never needs an edit to the page.
5. Only what's true and public goes on the page.
