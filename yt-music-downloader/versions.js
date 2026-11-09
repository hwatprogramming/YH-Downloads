// YT Music Downloader's versions, one list per platform, newest first.
//
// The page draws the version beside each download button from this list. With more
// than one version in a list, that version becomes a menu of all of them.
//
// On every update, add the new version at the top of its list:
//   version  the number, as the app shows it
//   date     the version's date, year-month-day, same as the release notes
//   changed  what changed, in a line or two
//   file     its numbered copy in the release, like yt-music-downloader-1.1.apk
//   size     as the page shows it, like About 67 MB
//
// check-versions.bat (in the repo's top folder) checks every file here is on GitHub.
// Keep the part after the = sign plain JSON: double quotes, no comma after the last one.
window.versions = {
  "android": [
    {
      "version": "1.0",
      "date": "2026-10-15",
      "changed": "First version.",
      "file": "yt-music-downloader-1.0.apk",
      "size": "About 67 MB"
    }
  ],
  "windows": [
    {
      "version": "1.1.0",
      "date": "2026-11-09",
      "changed": "Asks before a playlist over 30 new songs. Pause and Cancel on each playlist and song.",
      "file": "yt-music-downloader-setup-1.1.0.exe",
      "size": "About 81 MB"
    },
    {
      "version": "1.0.0",
      "date": "2026-10-26",
      "changed": "First version.",
      "file": "yt-music-downloader-setup-1.0.0.exe",
      "size": "About 75 MB"
    }
  ]
};
