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
- **On phones the card has one left edge**, my call 16 Oct, cause the old card felt
  asymmetrical. The icon sits next to the app's name, and the line, the facts, the
  button and the link all start at the card's left edge under them. The button runs
  the card's full width. Desktop keeps icon, text and buttons in one row.
  - Four phone layouts were drawn as real screenshots
    (`.playwright-cli/fix-mocks/card-layouts.png`, not committed): **A** as it was,
    text right of the icon but the button back at the card's edge. **B** button and
    link moved right to line up with the text. **C** icon with the name, the rest at
    the card's edge. **D** everything centred. **Picked C, with the button stretched
    across.** I didn't say why not B or D. The tradeoffs shown with them: B leaves the
    icon alone in its column, and D is about 75px taller with centred text that's
    slower to read.
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
  - **Left out of YT Music Downloader's FAQ, for good:** "Is this legal?" It's the
    most common question for this kind of app, but the honest answer is that
    YouTube's terms don't allow downloading. My call 16 Oct: skip it. Don't
    re-suggest it.
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
- **Look from the app.** Barlow Condensed for the name and the section headings,
  Roboto for the rest. [Said "name only" until 16 Oct, but the page always used it for
  the headings too. My call 16 Oct: name and headings.] Also
  hairlines, the gold pill button. The riso grain, sun, dots, tilts and cut-paper
  button are gone.
- **Three real screenshots in a stack:** the Download tab, History and Help, my ask.
  The one showing is in front and the other two peek out behind it. Tabs over it, like
  the app's, bring one to the front, and so does clicking one that peeks out.
  - **Front one in the centre, one peeking out each side**, my ask 16 Oct. The picked
    one swaps places with the centre one. Before, both peeked out on the left, and the
    tabs moving instead (picked tab always in the middle) was tried and dropped the
    same day. The tabs stay in one order and the gold line moves.
  - **Tabs go Help, Download, History**, Download picked on load, my ask 16 Oct. The
    side phones start in the same order, so each tab is over its own screen until the
    first swap.
  - They're the app repo's `.impeccable/review/after-fixes/` shots, version 1.0, with
    the status bar (carrier and time) cut off.
  - **History is cut after Smells Like Teen Spirit.** Road Trip Mix and Nirvana are
    test songs, my call. The songs below them are my real downloads, so they're
    blanked out, and the screen keeps the app's tab bar at the bottom.
  - **The Up next songs are test songs too**, my word 16 Oct, so step 3's picture
    stays as it is.
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
  - **Setup follows the real install**, from my screenshots installing 1.0 off the
    live site, 16 Oct. Six steps, each with its screen: the file in Downloads, Open
    with Package installer, Play Protect's "App blocked to protect your device" with
    More details then Install anyway, Install, App installed, then the notifications
    prompt. The FAQ's "Why does my phone warn me" answer names Play Protect now too.
    - Cropped like the others. Open with keeps only Package installer, not the other
      apps' icons. The Downloads list drops the "(1)" copy from downloading twice.
    - Before that, Setup had four steps and only the notifications prompt as a
      picture.
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

### Finish review, 16 Oct

Impeccable's finish review said "fix" on both pages: small fixes, no redesign. I took
all 11 after seeing each as a before and after picture, and a second round scored every
one resolved, both pages "ship". The full list is in
[`finish-review.md`](../finish-review.md). The ones that change how the site looks or
works:

- **Step screens on phones open inside the step you tapped**, under its text, with a
  grey "Tap a step to see its screen." under Setup and How to use it. Before, the
  screen showed below the last step and nothing said steps could be tapped. Wider
  screens keep the screen beside the steps.
- **A "YH" tab icon**, in champagne on charcoal, on every page. Not the music app's
  icon, so the site doesn't look like it belongs to that one app.
- **Fonts live on the site**, in `assets/fonts/` with their licences, about 86 KB. Before,
  they came from Google, and if that failed the titles went to Arial.
- **The phone cut-off I saw was the name in its stand-in font on a slow first load.**
  The stand-in is now shrunk to Barlow's width, and the name is a bit smaller on
  phones (15vw, 59px letters at 390px instead of 64px). Checked on my phone.
- **The catalogue card says "64-bit phones"**, like the app page does.
- **Not fixed, on purpose:** the app page's File fact breaks as "yt-music-" /
  "downloader.apk" on phones. The name is wider than its column, so it has to break
  somewhere. [Fixed 26 Oct after all: on phones File gets a whole row. See "Finish
  review of the new parts, 26 Oct".]

The design system, written from the finished pages, is in [`DESIGN.md`](../../DESIGN.md).

### The Windows version, on the same page

Decided 26 Oct 2026. The app's Windows version (`../Desktop-Youtube-Music-Downloader`)
goes on YT Music Downloader's page beside the Android one, my call 23 Oct in that repo.
Built into `index.html` and `yt-music-downloader/index.html` 26 Oct, from the two
OK'd mockups.

- **How the build differs from the mockups** [Claude's calls while building]:
  - The Android version is the live page as it was, so its FAQ keeps the live answers
    in full. The mockup had shortened three of them.
  - The live page's alt text, `aria-controls`, section ids and arrow keys on tabs are
    kept. The mockup had dropped them. Windows sections get `-windows` ids.
  - Which version shows first is set in the page's head, before anything draws, so a
    PC never sees the Android version flash. `?os=windows` or `?os=android` on the
    link picks one.
  - The two-button card layout only applies to a card with class `two`, so a later
    app with one download keeps the one-button layout.
- **Window shots are from 1.0.0**, taken 26 Oct from the installed app, songs saved to
  `D:\Songs` so no username shows. The folder window and the closing prompt were
  retaken too: the old ones showed a temp folder path and the old text size icon.
- **Picture notes** on the 13 new pictures, like the 16 Oct ones: "Real screenshot of
  YT Music Downloader 1.0.0 or Windows on the owner's PC, cropped for this page, Oct
  2026. Not generated." The two with blurred parts add "with private parts blurred".
  `play-it.png` uses the phone wording.

- **The catalogue card gets two buttons**, one for the APK and one for Windows. My ask
  26 Oct. Mockup in `.impeccable/mocks/both-platforms/src/catalogue.html`, picture
  `catalogue-two-buttons.png` beside `src/`. OK'd 26 Oct ("great").
  - **Two gold buttons side by side, each with its version under it**, my pick over
    one gold button plus a quieter second one.
  - **Smaller than the one-button card's**, my ask, so two fit beside the text: 44px
    tall, 15px words. On phones they stay side by side, with the words in two lines
    next to the arrow, "Download for" small over the platform. Drawn first: stacked at
    full width (the 16 Oct one-left-edge layout), or side by side cut to "Android" and
    "Windows". I asked for smaller buttons with the words pushed left instead.
  - **On desktop they're up and down**, my ask: the same width, each with its version
    to its right, then "Setup, how to use it, FAQ". Side by side was drawn first, then
    up and down with the version under each, and I asked for it on the right. The phone
    stays side by side, "mobile one is fine".
  - **The two buttons' middle lines up with the card's middle**, my ask. The link under
    them put the buttons high, so on desktop "Setup, how to use it, FAQ" moved under
    the card's text on the left, like on the phone. The card is 204px tall, from 187.
    - First tried: the link kept under the buttons, with an empty space its height
      above them. That made the card 220px, and I said it had too much padding on top.
  - **20px between the two buttons on desktop**, from 12px, my ask. "Looks good alr"
    otherwise, 26 Oct.
  - **On phones "Setup, how to use it, FAQ" is centred** under the buttons, my ask 26
    Oct. The rest of the phone card keeps one left edge.
  - The line under the card's text says what each needs: "Android 10 and up, 64-bit
    phones · Windows 10 and 11, 64-bit". The file names came off the card. They're on
    the app's page.
- **Picked: Tabs.** An "Android phone / Windows PC" switch under the app's line, and the
  whole page follows it: facts, the button with its version, file details, screens,
  Setup, How to use it, What it's for and the FAQ. A Windows PC opens on Windows,
  everyone else on Android. The switch shows again where the details start. I didn't
  say why over Merged.
  - Mockup in
    [`.impeccable/mocks/both-platforms/src/tabs.html`](../../.impeccable/mocks/both-platforms/src/tabs.html).
    `sheet.png` beside `src/` has both directions side by side.
  - Tradeoff shown with it: each visitor reads only their version, so wording stays
    short, and the Android tab is the live page as it is. The cost is two versions of
    every section to keep up to date.
  - **"Share from YT Music" says "(Android only)"**, my ask, in plain grey after the
    tab's name, with 40px before "Paste a link". On narrow phones it drops under the
    name. Small spaced capitals were tried first, and I said plain works better.
    "Android only" rather than "mobile only", cause iPhone isn't supported.
  - **"Paste a link" comes first and opens by default**, my call once Share got its
    label. The live page has Share first.
- **"Play it" gets a screen**, from a friend 26 Oct: it was the only step in How to use
  it you couldn't tap. It's Tip Toe by HYBS in HONOR Music, the phone's own player,
  showing the title, artist and cover the app filled in. Taken over USB, with the
  status bar (carrier, time) and the gesture bar cut off. In the mockup's
  `src/assets/play-it.png`.
  - **A note for phones with no music player**, my ask. Not every phone has one, and on
    some the music app is YT Music. Under "Play it": "No music player? See the FAQ",
    which opens a new FAQ answer: check if the phone's own player was uninstalled or
    turned off, or install a music player from the Play Store. My two suggestions.
  - **On the Windows tab, "Play it" shows two pictures**, one under the other, both my
    screenshots from 26 Oct: Galaxy Express by D Gerrard playing in Windows' Media
    Player, then Media Player's music library with its artist and album. The other
    songs in the library are blurred, cause they're my real ones. In the mockup's
    `src/assets/win-play-now.png` and `win-play-library.png`.
  - **"Play it" has its own Android phone / Windows PC switch**, my ask, above its
    pictures, so either player can be seen from either tab. It starts on the tab
    you're on, swaps only the pictures and caption, and shows only while Play it does.
    Small text tabs in the app's style. Claude first put it under the step's text, and
    I said above the pictures is better.
  - **A Windows FAQ answer for Media Player's library**, my OK 26 Oct: "Why don't my
    songs show in Media Player's library?" The library only lists the folders it
    watches, Music unless you add more. The answer says the app starts on Music, and
    to use Add folder for any other folder. "Not in Media Player? See the FAQ" under
    the Windows "Play it" links to it, like the Android one.
    - The desktop app started on Downloads till 26 Oct. Seeing this, I moved it to
      Music, and the "Folder not found" picker too. Rebuilt the installer the same day.
      [In the desktop repo's `folder-window.md`.]
- **Windows Setup follows the real install**, from my screenshots installing the 26 Oct
  build off the release link: "Windows protected your PC" then More info and Run
  anyway (the guessed step was right), the installer's Next, Next, then Finish with
  Run ticked, and the app open. Five steps.
  - The Install it screen had my Windows username in the folder path, blurred. The
    "Installation Complete" screen has it too, in its file log, so it's left out.
  - The two SmartScreen screens have their empty teal middle cut out, so the step
    isn't two tall blocks.
  - The browser didn't warn about the download, so there's no screen for that.
  - The new empty app window also replaced the 25 Oct one in How to use it's "Paste it
    in the app".
- **Rejected:**
  - **Merged.** One page for both: two buttons, one table of both files, wording like
    "On a phone… On a PC…", and Setup with its own switch. Sentences got longer, and on
    phones the second button and the table pushed the screens down.
  - **A page each.** I leaned tabs or merged and dropped it, 26 Oct.
- **The installer goes in the APK's release**, my call 26 Oct: `yt-music-downloader`
  holds both files, the APK and `yt-music-downloader-setup.exe`. The release's title
  names both versions, like "YT Music Downloader · Android 1.0 · Windows 1.0.0".
  - **Rejected: a release of its own** (`yt-music-downloader-windows`). Each version
    would have had its own title, so updating one never touched the other, but it broke
    "one release per app".

### Finish review of the new parts, 26 Oct

Impeccable's finish review of the Windows version and the two-button card said "fix" on
both pages. I took all 7 after seeing each as a before and after picture, and a second
round scored every one resolved, both pages "ship". The list is in
[`finish-review.md`](../finish-review.md), "Second review, 26 Oct". What changed on
screen:

- **What it's for's two lists sit side by side only from 1100 wide.** Below that, "Made
  for" sits above "Not", like on phones. Between 760 and about 990 the notes ran into
  the other list, and up to about 830 the page scrolled sideways.
- **From 760 to 919 wide, the version and date go on one line under the button.** The
  phone pictures covered them at 760.
- **The Windows window pictures are 280px wide from 760 to 1279**, from 300, so the
  switch's labels fit on one line. They never wrap now.
- **On phones the File credit gets a whole row**, so the file name doesn't break.
  "Installs from" sits alone on the last row.
- **Windows Setup step 1's file name never breaks.**
- **Catalogue, 760 to 899 wide: each version goes under its button**, which gives the
  card's text about 100px more. From 900 up it's still the version on the right.
- **Catalogue, under 760 wide: the two buttons stop at 440px together**, about 215px
  each. This answers my 16 Oct question about capping the button.

### Picking an older version, not built yet

From my journal 26 Oct: people can choose which version to install on an app's page,
the catalogue keeps showing only the latest, and a changelog would be nice. Every app
with more than one version gets it.

- **Picked: A, a menu beside the button**, 26 Oct. The version line next to the
  download button becomes a menu. Pick a version and the button gets that one. Each
  version in the menu has its date and what changed under it, and the newest says
  "Latest". It follows the Android phone / Windows PC switch.
  - Mockups: `.impeccable/mocks/version-picker/src/` (built from the live page by
    `make-mocks.py` beside it), picture `sheet.png`. Versions 1.1 and 1.2 in them are
    made up.
  - Tradeoff shown with it: everything's in one spot and the page doesn't grow, but
    what changed is hidden till you open the menu, and the open menu covers the
    details under it.
- **Not picked:**
  - **B, a Versions section after the FAQ**, set like the FAQ, with a download per
    version and "Older versions and what changed" under the button. First screen
    barely changes and the changes are always readable, but older versions are a
    scroll away.
  - **C, "All versions and what changed" under the button**, opening a list right
    there. One tap away, but it pushes the details and the pictures down while open.
- **Old files are kept as copies in the app's one release**, my pick 26 Oct. The
  fixed name (`yt-music-downloader.apk`, `yt-music-downloader-setup.exe`) is always the
  newest, for the download button and the catalogue, so their links never change.
  Next to it, every version gets a copy with its number in the name
  (`yt-music-downloader-1.1.apk`, `yt-music-downloader-setup-1.0.1.exe`), for the menu.
  Each update uploads the new file twice. So the newest file is stored twice, and I'm
  fine with that: "I don't think people will be seeing the page anyways" (GitHub's
  releases page).
  - Drawn before picking, as GitHub's releases page after a few made-up updates:
    `.playwright-cli/old-files/keeping-old-files.png` (not committed).
  - **Rejected:**
    - **A release per version.** Each version gets its own GitHub page, which works as
      a changelog there, but it breaks "one release per app" and adds a page every
      update.
    - **One "older versions" release per app.** Nothing stored twice, but two
      releases per app and an extra step every update.
    - **Renaming the old file instead of copying.** One file per version, but it needs
      a less common GitHub command. Not worth it for a page people won't look at.
    - **Numbers only, no fixed name.** Fewest files, but every update has to change the
      button's link on the app page, the catalogue and the README, and a saved link
      gets an old version.
  - Today's 1.0 and 1.0.0 files have no numbered copy yet. They need one when the
    picker gets built, before the next update overwrites them.
- **How the rule sticks: all three together**, my pick 26 Oct.
  - **A list of versions per app**, like `yt-music-downloader/versions.json`: number,
    date and what changed for each version, per platform. The menu and the version
    beside the button are drawn from it, so an update adds one entry and both follow.
    If the entry gets skipped, the whole page shows the old version, so it's plainly
    behind instead of half updated.
  - **A step in `doc/uploading-a-build.md`**: upload a numbered copy too, and add the
    entry to the list.
  - **A check script**, `check-versions.bat`: compares the files on GitHub with the
    lists and says what's missing. Claude runs it at the end of every upload, in
    "Check it worked", and I can double-click it. Not run by GitHub on every push,
    which would be one more thing to set up.
  - Drawn before picking: `.playwright-cli/enforce/making-the-rule-stick.png` (not
    committed). Each way on its own was the option: the step alone is easy to skip
    without anyone noticing, and the script alone only helps when it's run.

## No version number on the page

The row for an app has its name, one line on what it does, and the link. The version
lives in the release's title and notes.

**Why:** the link never changes, so if the row has no version in it, an update needs
no commit here. The row only changes when an app is added, renamed or removed.

**What it costs:** you can't see the current version from the page. You have to open
the release.
