# Uploading a build

For a Claude working in one of the app repos. This is how you get a built file from
that repo onto this one, so it can be downloaded.

You don't need this repo cloned to upload. Every command below takes
`--repo hwatprogramming/YH-Downloads` and runs from anywhere.

## Rules

- **This repo is public.** Anything uploaded can be downloaded by anyone straight away.
  Ask before you upload, every time. One yes covers the upload and the downloads page
  commit that goes with it, so don't ask twice.
- **Built files only.** APK, exe, zip of a built app. Never source code, keystores,
  signing keys, `.env` files or anything with a password or token in it.
- **Upload to Releases, never commit a build into the repo.** Git keeps every old
  version forever and blocks files over 100 MB. Releases take up to 2 GB per file and
  a replaced file is really gone.
- **Upload the build you'd install yourself.** The release build, not a debug one.

## How it's laid out

One release per app. The release never changes its tag, and the file never changes
its name. You replace the file when there's a new version.

| Thing | Rule | Example |
|---|---|---|
| Tag | App name, lowercase, dashes | `yt-music` |
| File name | Same as the tag, no version number in it | `yt-music.apk` |
| Title | App name plus version | `YT Music v1.2` |
| Notes | Version, date, what changed in a line or two | |

The version goes in the title and notes, not in the tag or the file name. If it went
in either of those, the download link would change with every update and every link
pointing at it would break.

**An app with two versions**, like YT Music Downloader's Android and Windows ones, keeps
both files in its one release. The second file gets a word after the tag that says what
it is, like `yt-music-downloader-setup.exe` for the Windows installer. The title names
both versions, like `YT Music Downloader · Android 1.0 · Windows 1.0.0`, and the notes
have a line per version. Updating one version edits its part of the title and notes and
leaves the other's alone. [Decided 2026-10-26, see
[`downloads-page.md`](live-design-choices/downloads-page.md).]

Download link for any app, which stays the same across updates:

```
https://github.com/hwatprogramming/YH-Downloads/releases/download/<tag>/<file name>
```

## First upload of an app

1. Build the app in its own repo.
2. Copy or rename the built file to the fixed name, e.g. `yt-music.apk`.
3. Check the tag isn't taken:
   ```
   gh release list --repo hwatprogramming/YH-Downloads
   ```
4. Create the release with the file attached:
   ```
   gh release create yt-music "path/to/yt-music.apk" --repo hwatprogramming/YH-Downloads --title "YT Music v1.0" --notes "v1.0, 2026-10-01. First upload."
   ```
5. Add the app to the site and the README, then commit and push. See the next section.

## Adding a new app to the site

The downloads page is a GitHub Pages site, live since 2026-10-16 at
<https://hwatprogramming.github.io/YH-Downloads/>. GitHub serves this repo's files as
they are. This is the step that needs this repo cloned. It sits next to the app repos,
at `../YH-Downloads`. If the folder isn't there, clone it there first.

- `index.html` is the catalogue: a card per app, in that app's own colours.
- Each app has its own page at `<tag>/index.html`, with its pictures in
  `<tag>/assets/`. It's themed on the app, and every app's page has the same parts.
  See [`downloads-page.md`](live-design-choices/downloads-page.md) and `PRODUCT.md`.
- Links between pages point at `index.html` itself, not the folder, so a page still
  works when it's opened straight from the disk.

1. Get the latest copy:
   ```
   git -C ../YH-Downloads pull
   ```
2. Design the app's page with the user, with Impeccable. Mockups go in
   `.impeccable/mocks/`, and the picked one becomes `<tag>/index.html`.
3. Add its card to `index.html`, with its version, and its chip to the header of
   each app page.
4. Add one row to the table in `README.md`, the repo's front page on GitHub. Name, one
   plain line on what it does, and the download link. No version in the row.
5. Commit and push. The site updates by itself a minute or so after the push.

## The version on the site

Each app's page shows its version and date beside the download button, and its card
on the catalogue shows the version. The user asked for it 2026-10-16, so people can
tell they have the latest. So an update does need a commit, see below.

## Updating an app that's already here

1. Build, then rename the file to the same fixed name as before.
2. Replace the file. `--clobber` means overwrite the one with the same name:
   ```
   gh release upload yt-music "path/to/yt-music.apk" --repo hwatprogramming/YH-Downloads --clobber
   ```
3. Update the title and notes so the version shown is right:
   ```
   gh release edit yt-music --repo hwatprogramming/YH-Downloads --title "YT Music v1.1" --notes "v1.1, 2026-10-08. Playlists."
   ```

4. Update the version on the site: the "Version X · date" line beside the button on
   the app's page, and "Version X" on its card in `index.html`. Commit and push.
   - An app with two versions has one of each per version. On YT Music Downloader's
     page the Windows line sits in the `data-for="windows"` block, and on the card
     it's the one under "Download for Windows". Change only the version you uploaded.

The link stays the same, so nothing else changes. The README row has no version, so
it stays as it is.

## Check it worked

```
gh release view yt-music --repo hwatprogramming/YH-Downloads
```

Look for the file under assets, with the size you expect. Then give the user the
download link.

## If something goes wrong

- **"Repository is empty"**: releases need at least one commit pushed to this repo.
- **"release not found" on upload**: the app has no release yet. Use the first-upload steps.
- **Upload fails with a name clash**: you left out `--clobber`.
- **`gh` isn't logged in**: run `gh auth status`. It needs to be the `hwatprogramming` account.
- **Wrong file went up**: `gh release delete-asset <tag> <file name> --repo hwatprogramming/YH-Downloads`,
  then upload the right one.
