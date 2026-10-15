# Downloads page

**What it is:** the site that lists every app and its download link, live since 16 Oct
2026 at <https://hwatprogramming.github.io/YH-Downloads/>. `index.html` is the
catalogue, and each app has its own page, `yt-music-downloader/index.html` for the
first. The repo's `README.md` still has a table with one row per app, as the repo's
front page on GitHub.

[It was only the README till 16 Oct. How to add an app or update one is in
[`uploading-a-build.md`](../uploading-a-build.md).]

## Moving to a website

Decided 13 Oct 2026. Built and live 16 Oct 2026, from the two picked mockups. The
mockups stay in `.impeccable/mocks/` as the record. The site's own files are the ones
to edit now.

- **The catalogue has only real apps.** The two made-up placeholder apps from the
  mockup came out. Under YT Music Downloader's card sits a dashed empty slot saying
  "And more apps to come…", my ask 16 Oct.
- **Links between pages point at `index.html` itself**, not the folder, so a page
  opened straight from the disk still links to the other one. GitHub Pages would turn
  a folder link into its page, but a file on disk shows the folder instead.

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

### A catalogue page, plus a page per app

Decided 14 Oct 2026. Replaces "one long page" above.

**Picked:** the home page is a catalogue of every app, with its name, one line and
download button. Each app also gets its own page, which is the full layout the Two-Ink
Riso mockup has now. The header and catalogue get a theme of their own, so they read
apart from any one app.

**Why:** with the five parts in, the page felt like a landing page for YT Music
Downloader, not a catalogue of my apps. The details were spread over so much area that
the site felt dedicated to that one app.

**What it costs:** one more HTML file per app, still plain HTML that Claude adds. A
visitor taps once more to reach an app's details. The download button sits on the
catalogue too, so downloading doesn't take an extra tap.

**Rejected:**
- **One page with shorter sections.** The five parts would fold into "More about this
  app". It keeps one file, but it's still a long scroll once there are many apps, and
  the details stay hidden till opened.
- **Keep the full sections and add a catalogue header.** Least change, but each
  section would still feel like a landing page for its app.

#### How the catalogue's look got picked

All on 14 Oct. Mockups and their desktop and phone pictures are in
[`.impeccable/mocks/catalogue/`](../../.impeccable/mocks/catalogue/), with the HTML in
`src/` there. Impeccable's seed key for this round is `0d64e648`. Two of the three
apps in every mockup are made-up placeholders, marked as such.

**Round 1: three ideas.** First drawn light (blue, green mat, white), then dark when I
said "i prefer a dark theme". Their dark is a neutral near-black, so it reads apart
from YT Music Downloader's navy.

| Mockup | File | What it is |
|---|---|---|
| Card catalogue | `card-catalogue` | A dark drawer of charcoal index cards, in blue and red. Each app is a card with a tab, and pulling a tab brings that card to the front. |
| Press sheet | `press-sheet` | One uncut print sheet, white ink on black, on a black cutting mat. A strip of colour samples along the top is the catalogue, and each app is a panel with crop marks. |
| Contents page | `contents-page` | A zine's contents page in white and pink on black. A big title, then a tight list of apps with their download buttons. |

**Picked the Contents page idea**: a big title, then a tight list of apps, each with
its download button. "i like contents page idea but i want it in a differnt style".
Card catalogue and Press sheet are out.

**What its style had to be**, my words: no pink and not that font (Bagel Fat One).
"something more professional as a one look fits all type of thing for the contents
itself, its fine for it to be slighty stylised." Still dark.

**Round 2: three styles of the Contents page.**

| Style | File | What it is |
|---|---|---|
| Index | `contents-index` | Black and warm white, no accent. A wide, heavy typeface (Archivo) does the styling. White buttons. |
| Shelf | `contents-shelf` | Each app in a soft rounded panel with a big icon, one calm blue for buttons and links. Bricolage Grotesque. |
| Manifest | `contents-manifest` | A spec sheet: on desktop the apps line up in columns (app, what it does, runs on, file, download). File names in a code face. Schibsted Grotesk. |

**Round 3: "something softer?"**

| Style | File | What it is |
|---|---|---|
| Warm | `soft-warm` | Warm charcoal, oat text, round panels with no outlines, pill buttons. Figtree. |
| Cloud | `soft-cloud` | Dusky blue-grey, every app in one rounded group like a phone's settings list, pastel periwinkle pill buttons. Nunito. |
| Quiet | `soft-quiet` | Muted warm greys, no boxes or lines, just space between apps, gentle tinted buttons. Onest. |

**Picked: Warm, with two changes.** In `soft-warm.html`.

- **The title is a champagne gold, `#E6C88E`.** My words: "i just like gold but shouldnt
  be too similar, need to be distinct from YT downloader". It's paler and less
  saturated than YT Music Downloader's `#EDBB4E`.
- **Each app's card and button wear that app's own colours.** YT Music Downloader's
  card is its navy with a gold button. This replaced "an app's own colours only show
  in its icon" from round 2. The page around the cards (title, type, layout, spacing)
  stays one shared look.
- **The app page's header is in this look too.** On YT Music Downloader's page the
  old riso bar is gone. The header is a warm charcoal band with "YH Downloads" in
  champagne, then "All apps", the chip of the app you're on in its own colours, and
  "Support me". The app's name is the page's main heading. [Support me is parked
  since 16 Oct, see below, so the header has only the two chips for now.]
  - **Only All apps and the app you're on**, my ask 16 Oct. It had a chip for every
    app, which scrolled sideways on phones. Other apps are one tap away on All apps.
  - **Support me**, my ask 16 Oct: an outlined champagne button with a heart, last in
    the header. It opens the Support me page, see below. On phones it sat beside
    "YH Downloads", and the two chips got the second row, so nothing scrolled.
  - **It sticks to the top** while you scroll, my ask. On a phone it's two rows, so it
    takes about an eighth of the screen. Claude offered a one-row phone version. Not
    answered.
- **A Support me page**, my ask 16 Oct: "a simple donation page that links to
  ko-fi". In the site's own look, like the catalogue, in
  [`.impeccable/mocks/catalogue/src/support.html`](../../.impeccable/mocks/catalogue/src/support.html).
  A big champagne "Support me", one line saying every app is free and that you can
  support me on Ko-fi if one helps, a "Support me on Ko-fi" button, and a note that
  Ko-fi takes the payment. Ko-fi is a site where people send small payments to
  creators, so nothing on this site handles money.
  - **Parked 16 Oct**, my call: I can't get into my Ko-fi account right now. The
    page's mockup stays, and the Support me button came off the header. Picking it
    back up is in [`backlog.md`](../backlog.md).
- **Out:** Cloud and Quiet, and everything from rounds 1 and 2.

### What I've settled

- **Who opens it:** me, people I know, and anyone who lands on it.
- **What an app's page does first:** shows the app off, like a small landing page
  for that app. The download comes with it, not before it.
- **The only hard rule, in my words:** "Nothing looks wrong, as long as I have a
  download link and I know what I'm downloading."
- **First app:** YT Music Downloader. It was called Music Downloader on the phone till
  2026-10-14, and the earlier notes here use that name.
- **The same parts on every app's page**, my ask 2026-10-14. Under the app's name, line,
  download button and picture come Setup, How to use it, What it's used for, What it
  isn't, and an FAQ. Setup and the FAQ are left out when an app has none.
  - **Left out of YT Music Downloader's FAQ:** "Is this legal?" It's the most common
    question for this kind of app, but the honest answer is that YouTube's terms don't
    allow downloading, so whether it goes on a public page is my call. Not asked yet.
- **Built with plain HTML and CSS.** No build step: the catalogue page plus one page
  per app since 14 Oct. I said "you pick" and Claude picked it.
  - Every app's page has its own theme, and a shared template would fight that.
  - I can preview a page by opening the file.
  - **Rejected: Jekyll.** It's a site builder GitHub Pages runs for you, where each
    app would be a small text file and a template makes the page. You can't preview
    it by opening a file, and the template fights the per-app themes.
- **Claude adds each app's page and its catalogue entry.** I opted out of adding apps
  by myself for this repo. [`repo-journal.md`, 13 Oct.]

The product facts are in [`PRODUCT.md`](../../PRODUCT.md), which Impeccable reads.

### Not settled

- [Version numbers on the site: settled 16 Oct, see "Version beside the button"
  under YT Music Downloader's page below.]

### YT Music Downloader's page, in the app's new look

Decided 16 Oct 2026. Replaces the Two-Ink Riso page in "Picking the look" below.

**Why it changed:** I finished the app's own redesign, Liner Notes. Each song is set
like album credits, the name is in tall condensed capitals with a gold "YT", and the
app is navy with one gold. The Riso page's font, cream ink and print effects came
from the app's old look. [The app's look is in
`../Mobile-Youtube-Music-Downloader/DESIGN.md`, and what the page had wrong is in its
`doc/for-yh-downloads.md`.]

**Picked: the Riso page's layout, in the app's new look.** My words: "what i like
about the old one is that its neat, presents the important stuff clearly then goes on
to provide more details." It's in
[`.impeccable/mocks/app-page/src/yt-music-downloader.html`](../../.impeccable/mocks/app-page/src/yt-music-downloader.html),
with pictures `yt-music-downloader-desktop.png` and `yt-music-downloader-phone.png`
beside `src/`.

- **Layout kept from Riso.** The big two-line name, the line, three facts and the
  download button, with the picture on the right. Then Setup next to How to use it,
  What it's used for next to What it isn't, and the FAQ, one question open at a time.
- **Look from the app.** Barlow Condensed for the name only, Roboto for the rest,
  hairlines, the gold pill button. The riso grain, sun, dots, tilts and cut-paper
  button are gone.
- **Three real screenshots in a stack:** the Download tab, History and Help, my ask.
  The one showing is in front and the other two peek out behind it. Tabs over it, like
  the app's, bring one to the front, and so does clicking one that peeks out.
  - They're the app repo's `.impeccable/review/after-fixes/` shots, version 1.0, with
    the status bar (carrier and time) cut off.
  - **History is cut after Smells Like Teen Spirit.** Road Trip Mix and Nirvana are
    test songs, my call. The songs below them are my real downloads, so they're
    blanked out, and the screen keeps the app's tab bar at the bottom.
- **A credits block under the button:** File, Size, Runs on, Installs from, in the
  app's small spaced capitals. It fills the space under the button. I'd said the page
  felt "too spread apart".
- **One 1200px column**, with the header lined up to it. Full width felt spread apart,
  and so did 1040px.
- **The details are short and titled**, my ask, cause they felt wordy. Every step has a
  short title in white and a few grey words under it, so the titles alone tell the
  story. Steps sit on numbered rings joined by a thin line.
- **What it's used for and What it isn't are one section, "What it's for"**, my ask, so
  they don't read as two. "Made for" and "Not" sit side by side on one panel, in the
  navy of the app's Help pop-up, with a tick or a cross in a small disc. Most items
  are only a few words. It replaced a gold slab for What it isn't, cause the app keeps
  gold for what you tap.
- **Section headings in the name's lettering**, my ask: Barlow Condensed capitals. The
  app itself keeps Barlow for its name only, but the page doesn't have to.
- **A sound wave between the groups of sections**, my ask for highlights cause
  everything under the first screen was the same dark blue. It sits at the top of the
  details, above What it's for and above the FAQ. Its gold part is how much has
  "played": a third, two thirds, then all of it by the FAQ. In browsers that can, the
  gold fills in as you scroll it into view. It started as a thin line, my ask, then
  became the wave.
- **The real screen for a step, beside the steps**, my ask to fill the space with
  proper content. The step whose picture shows has a gold ring. On phones the picture
  sits under the steps.
  - **Setup:** the phone's "Allow YT Music Downloader to send you notifications?"
    prompt, for step 4.
  - **How to use it has the app's two ways in as tabs**, my ask: Share from YT Music,
    and Paste a link. A tab swaps the first two steps (share and pick the app, or copy
    the link and paste it in the app). The rest is the same both ways: "Big playlist?
    Say yes" (over 20 songs, it asks on the notification first), Let it run, Play it.
    Pointing at or tapping a step shows its screen.
  - Most are screenshots I took 16 Oct. They're cropped so the status bar (carrier,
    time), the Nevermind album cover, other apps' icons (WhatsApp, Messenger,
    Instagram, Facebook) and my other notifications stay off the page. They're saved
    as PNG from the pixels only, so the phone's photo data doesn't come along.
  - **The pasted link's share code is painted out.** It ended in `&si=…`, YouTube's
    share code that can tie a link back to my account, so the picture shows only
    `…watch?v=ljUtuoFt-8c`.
  - Unused for now: YT Music's now-playing screen, its song menu, the Trending 20
    Singapore playlist page, and Android's notification settings with the Allow
    notifications switch.
  - First tried: the app's "Notifications are off" card beside Setup. The real
    prompt shows the step better.
- **What it's for as credits lines:** the item, dots across, a short note at the end,
  like the credits on an album. It fills the width without adding sentences. On narrow
  phones the note sits under the item instead. "Sharing from YT Music, no need to open
  the app" was added so both sides have five.
- **The page ends on "Back to top"**, a gold text button like the app's, my ask. It
  replaced a second Download for Android button there.
- **Content brought up to version 1.0** from the app's note: the button is "Update
  download engine (yt-dlp)", the FAQ says which links work and that private ones
  don't, Setup says big playlists ask first, and the size is about 67 MB.
- **Version beside the button**, my ask 16 Oct, "so that we know its the latest one":
  "Version 1.0" and its date, 15 Oct 2026. Under the button on phones, beside it from
  tablets up. The app's Help shows the version too, so people can check theirs.
  - **What it costs:** every update now edits the page and needs a commit. The README
    page left versions out to avoid exactly that, see "No version number on the page"
    at the end. The site does it the other way.

**Rejected:**
- **Three fresh directions** in the app's look, drawn first, side by side in
  [`.impeccable/mocks/app-page/compare.png`](../../.impeccable/mocks/app-page/compare.png).
  I preferred the old layout.
  - **Album back cover.** A tracklist indexes the page, with the download as track A1.
  - **App screen.** The page is the app's Download tab, bigger, with a made-up queue
    running on it and the app's tabs at the bottom.
  - **Tags before and after.** One song saved two ways, with only the video's name and
    with its credits.
- **One screenshot with tabs to switch it.** Built first, but it left empty space
  between the text and the picture.
- **History uncut.** It shows my real downloads.

### Picking the look

[Replaced 16 Oct 2026 by "YT Music Downloader's page, in the app's new look" above.
Kept as the record of how the layout came about.]

**Two-Ink Riso became YT Music Downloader's app page**, 14 Oct. I said "i really like
this" and asked for changes to it, then it became the app page when the catalogue
split off. Changes so far, all in `challenger-risograph.html`. Current pictures of it
are `challenger-risograph-desktop.png` and `challenger-risograph-phone.png` in
[`.impeccable/mocks/decision/`](../../.impeccable/mocks/decision/). The other pictures
there are the first round, before any changes.

- **Renamed to YT Music Downloader.** The first line of the title went from 300px to
  230px so "YT Music" fits, and the text under it moved up to close the gap. The file
  name follows the upload guide's rule: `yt-music-downloader.apk`.
- **The five parts above** are under the first screen, in the section's two inks.
  Steps are numbered, What it isn't is a dark slab, and the FAQ opens one question at
  a time.
- **Dark instead of cream**, my ask 2026-10-14. I wanted Inside the Icon's colours
  "but in reverse, more dark then yellow". The page is now its dark navy `#0F151D`,
  with gold `#EDBB4E` and its cream text `#F3E3B5` as the two inks. Gold carries the
  title, the sun, the download button and the What it isn't slab. The cream version
  is kept as `challenger-risograph-light.html`.
- **Works on phones and tablets**, my ask 2026-10-14. Most visitors download an APK
  on the phone it's for, so the phone layout counts most.
  - **Phone:** everything in one column. The download button still shows on the first
    screen of a 390px-wide phone. The picture comes after it, with the sun and dots
    behind it.
  - **Tablet, 760px and up:** the picture moves up beside the text. From 900px the
    five parts go two by two.
  - **Desktop, 1100px and up:** unchanged. Below 1100px the hand-placed desktop
    layout runs out of room, so that's where it switches.
- **Header:** the riso bar it had is gone. It has the catalogue's Warm header now,
  see "How the catalogue's look got picked".

What came before:

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
