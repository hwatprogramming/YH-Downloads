# Downloads page

**What it is:** the page that lists every app and its download link. It's the repo's
`README.md`, a table with one row per app.

[That's still true today. On 13 Oct 2026 I decided to move it to a website, see
"Moving to a website" below. The site isn't built yet.]

## Moving to a website

Decided 13 Oct 2026. Not built, so `README.md` is still the page.

**Picked: a GitHub Pages website.** GitHub Pages is GitHub's free hosting. It turns
files in this repo into a site at `hwatprogramming.github.io/YH-Downloads`. This
replaces "README only" below.

**Why:** I want one long page with a section per app. Each section has the app's
details, its download links and a picture of the app, and gets its own theme, based
on the project it's built on. A README has a plain look and no real design, which was
the cost I listed for it on 1 Oct. [My entries are in
[`repo-journal.md`](../repo-journal.md), 13 Oct.]

**What it costs:** there's a page to design and build before anything shows. That's
the reason I rejected a website on 1 Oct.

### What I've settled

- **Who opens it:** me, people I know, and anyone who lands on it.
- **What a section does first:** shows the app off, like a small landing page for
  that app. The download comes with it, not before it.
- **The only hard rule, in my words:** "Nothing looks wrong, as long as I have a
  download link and I know what I'm downloading."
- **First app:** Music Downloader.
- **Built with plain HTML and CSS.** One page, no build step. I said "you pick" and
  Claude picked it.
  - Every app's section has its own theme, and a shared template would fight that.
  - I can preview the page by opening the file.
  - **Rejected: Jekyll.** It's a site builder GitHub Pages runs for you, where each
    app would be a small text file and a template makes the page. You can't preview
    it by opening a file, and the template fights the per-app themes.
- **Claude adds each app's section.** I opted out of adding apps by myself for this
  repo. [`repo-journal.md`, 13 Oct.]

The product facts are in [`PRODUCT.md`](../../PRODUCT.md), which Impeccable reads.

### Not settled

- **The look.** See "Picking the look".
- **Version numbers on the site.** The README leaves them out so an update needs no
  commit. I haven't said if the site does the same.
- **Which picture of Music Downloader goes on the page.**

### Picking the look

Nothing is picked yet.

- **Three directions on a design canvas**, drawn first, still in "To evaluate":
  <https://claude.ai/artifact/GyEG127fHrS5bLCeDf1BgY>. A · Bands, gold from the icon.
  B · Bands, dark from the app's screen. C · Cards, gold from the icon. After seeing
  them I asked to use Impeccable.
- **Impeccable** is a design skill. It asks about the product, deals a few
  directions, and checks the page once it's built.
  - Its direction cards had words and a layout sketch but no pictures, cause there
    was no image generation in that session. I said "i need actual mockups before i
    decide", so Claude built each main card as a real page.
- **Five mockups** of the page's first screen, with Music Downloader as the app, at
  desktop size. Pictures are in
  [`.impeccable/mocks/decision/`](../../.impeccable/mocks/decision/). Their HTML is
  in `src/` there. Open one in a browser to see it full size.

| Mockup | File | What it is |
|---|---|---|
| The Cartridge Rack | `assigned` | Each app is a game cartridge. The download button is its slot. |
| Inside the Icon | `model-pick` | The section is the app's icon blown up. The line under the arrow is the download button. |
| Two-Ink Riso | `challenger-risograph` | Looks printed, in the app's two colours, slightly out of line on rough paper. |
| Session Title Card | `challenger-title-card` | The app's colour floods the screen and its name is set huge. |
| The category standard | `canon` | The usual app page: name, one line, button, phone beside it. |

- The mockups have no phone layout yet, and their download button points at a
  release that doesn't exist yet.
- Session Title Card and The category standard show the full app screen, which has a
  failed download with a raw error on it.
- Four of them have a strip of the apps across the top. I never asked for one.

Decided 1 Oct 2026.

| Option | What it is |
|---|---|
| README only | The text file GitHub shows on the repo's front page. |
| Website with a data file | GitHub Pages site, apps listed in one JSON file. |
| Website that reads Releases | GitHub Pages site that asks GitHub for the release list when someone opens it. |

**Picked: README only.** I wanted the page kept simple. [Replaced 13 Oct 2026 by
"Moving to a website" above.]

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
