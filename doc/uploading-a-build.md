# Uploading a build

For a Claude working in one of the app repos. This is how you get a built file from
that repo onto this one, so it can be downloaded.

You don't need this repo cloned to upload. Every command below takes
`--repo hwatprogramming/YH-Downloads` and runs from anywhere.

## Rules

- **This repo is public.** Anything uploaded can be downloaded by anyone straight away.
  Ask before you upload, every time.
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
5. Add the app to the list in this repo's `README.md`: name, one line on what it does,
   and the download link. Make the file if it isn't there yet. This is the one step
   that needs this repo cloned. It sits next to the app repos, at `../YH-Downloads`.

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
