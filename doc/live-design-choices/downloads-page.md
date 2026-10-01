# Downloads page

**What it is:** the page that lists every app and its download link. It's the repo's
`README.md`, a table with one row per app.

## Where the page lives

Decided 1 Oct 2026.

| Option | What it is |
|---|---|
| README only | The text file GitHub shows on the repo's front page. |
| Website with a data file | GitHub Pages site, apps listed in one JSON file. |
| Website that reads Releases | GitHub Pages site that asks GitHub for the release list when someone opens it. |

**Picked: README only.** I wanted the page kept simple.

**What it costs:** plain look. Headings, a table and links, no real design.

**Rejected:**
- Website with a data file. Every upload would need a commit and push to keep the
  version on the page right.
- Website that reads Releases. Nothing to keep in sync, but it's a page to design and
  build first, and it shows empty if GitHub's release list doesn't load for a visitor.

## No version number on the page

The row for an app has its name, one line on what it does, and the link. The version
lives in the release's title and notes.

**Why:** the link never changes, so if the row has no version in it, an update needs
no commit here. The row only changes when an app is added, renamed or removed.

**What it costs:** you can't see the current version from the page. You have to open
the release.
