# Finish review of the live site

Impeccable's finish review of the two live pages, 16 Oct 2026. Each page got a fresh
reviewer. Both said **fix**: the look matches what I picked, nothing gets redesigned,
just small fixes. **All 11 applied 16 Oct, my call**, after seeing each as a before and
after picture.

**Second round, 16 Oct: both pages "ship".** A fresh reviewer per page scored that
page's fixes from new screenshots and the page files. Every fix came back resolved,
and neither found anything the fixes broke.
- Catalogue: #1, #2, #3, #8, #9, #10 resolved. My new phone card layout breaks nothing.
- App page: #4, #5, #6, #7, #8, #10, #11 resolved. Their one caveat, that #11 was only
  shown in a Chromium screenshot, is covered: I checked it on my phone the same day.
- "Ship" here covers the scored fixes, not a fresh full review of either page.
- #2, #5, #6, #8 and #10 can't show in a screenshot, so the reviewers scored those from
  the page files.
- New screenshots are over the old ones in `.impeccable/review/`, plus
  `yt-music-downloader/mobile-slow-name.png`, the name with Barlow blocked, for #11.

[Direction contracts the reviewers checked against: `.impeccable/surfaces/index-html.md`
and `.impeccable/surfaces/yt-music-downloader-index-html.md`, written 16 Oct from what
shipped. Screenshots they looked at: `.impeccable/review/catalogue/` and
`.impeccable/review/yt-music-downloader/`, 1440 and 390 wide.]

## What both reviewers said to keep

- **Catalogue:** how quiet it is. One big champagne title, one navy and gold card, the
  dashed slot. Add nothing else while fixing.
- **App page:** the first screen as it is: the big name with the gold "YT", the stack of
  real screens, the gold button with version and date. And gold only on what you tap
  and on progress.
- The detector's two warnings stay ignored, and both reviewers agreed: Roboto is the
  app's font, and the FAQ "cramped padding" is a false alarm from its thin top line.

## Small fixes you'd barely notice

[**All six applied 16 Oct**, after Claude showed each as a before and after picture
(`.playwright-cli/fix-mocks/fixes-1-to-6.png`, not committed). #2 is catalogue only,
cause the app page already sets its scrollbar colours.]
[The app page's File fact breaks the same way as #1, "yt-music-" / "downloader.apk".
Left as is: the name is 167px and its column is 159px on a 390px phone, so it has to
break somewhere.]

| # | Page | What's wrong | Fix |
|---|---|---|---|
| 1 | Catalogue | On phones the file name breaks as "yt-" / "music-downloader.apk" | Wrap it in `<span class="file">` with `white-space:nowrap`, line 88 |
| 2 | Catalogue | Scrollbar shows light grey on the dark page (short window, zoomed text) | Add `color-scheme:dark` to `:root`, line 15 |
| 3 | Catalogue | "And more apps to come…" starts about 7px right of the icon above it (3.5px on phones) | `.soon` `padding-left:18.5px`, and `22.5px` from 760px up |
| 4 | App page | On phones the credits break "64-" / "bit phones" | Write `64&#8209;bit`, a hyphen that can't break |
| 5 | App page | Tapping anything on Android flashes a square blue box, even over the round gold button | `*{-webkit-tap-highlight-color:transparent}`, and give steps their own tap look, e.g. `.steps li[data-shot]:active::before{border-color:var(--ink)}` |
| 6 | App page | A screen reader reads out every caption as the mouse moves down the steps | Remove `aria-live="polite"` from both `figure.cut` |

## Changes you'd see, my call

[**All five applied 16 Oct** (pictures: `.playwright-cli/fix-mocks/fixes-7-to-11.png`, not
committed). How each was done:
- #7: on phones the step's `figure.cut` moves into the tapped step and back out above
  560px. The grey hint line is phones only.
- #8: `assets/favicon.svg`, the letters drawn as shapes, cause a tab icon can't load a font.
- #10: the font files and their licences are in `assets/fonts/`, about 86 KB. Neither page
  asks Google for anything now.
- #11: the stand-in font is sized at 67%, measured with Roboto on the PC. On the PC the
  stand-in name comes out 309px against Barlow's 310px at 390 wide. Checked on my
  phone 16 Oct, looks good.]

| # | Page | What it is | Tradeoff |
|---|---|---|---|
| 7 | App page | On phones 5 of the 6 Setup screens are hard to find, Play Protect included. A tapped step's screen shows below step 6, and nothing says steps can be tapped. Fix: on phones (under 560px), `show(step)` moves the `figure.cut` into the tapped step, with `.steps li > .cut{grid-column:2; margin:10px 0 4px}`, and a grey line "Tap a step to see its screen." under Setup and How to use it, phones only | Phones are where most people install. It changes how steps behave there |
| 8 | Both | No tab icon (favicon), so browsers show a blank one. Fix: `assets/favicon.svg`, "YH" in `#E6C88E` on `#1B1917`, not the app's icon, so the site doesn't read as that app's | One new small file, and a new bit of design to judge |
| 9 | Catalogue | The card says "Android 10 and up" and not that it needs a 64-bit phone, which the app page does say. Fix: "Android 10 and up, 64-bit phones" | Longer line, but true |
| 10 | Both | Fonts load from Google's servers. If that fails, the big title falls back to Arial. Fix: put the font files in `assets/fonts/` and load them with `@font-face` | Rarely fails. Costs font files in the repo |
| 11 | App page | The likely phone cut-off, see below. Fix: `.name` to `font-size:min(15vw,116px)`, plus a fallback font sized to match: `@font-face{font-family:"Barlow Fallback"; src:local("Roboto"),local("Arial"); size-adjust:70%}` (tune the 70% so the fallback word is no wider), then `font-family:'Barlow Condensed','Barlow Fallback',sans-serif` | Name gets slightly smaller on phones |

## My open questions, with the reviewer's view

- **The phone cut-off I saw on the old Riso page.** Best guess: "DOWNLOADER". At 390px
  it's 337px wide in a 350px column. On a slow first load the phone briefly draws it in
  a wider fallback font, about 440px, which gets cut off, then it snaps back when Barlow
  arrives. That's why it happened once and couldn't be reproduced. Android's text-size
  setting can push it over too. Fix is #11.
- **Sticky header on one row on phones.** It won't fit: one row needs 451px, a 390px
  phone has 358px. Dropping All apps fits with 0px to spare, which breaks with any text
  size change. Dropping "YH Downloads" loses the champagne title. Reviewer's view: keep
  two rows. If it bugs me, unstick it on phones only,
  `@media (max-width:759px){.site{position:static}}`, since Back to top gets you back.

## Also part of the finish

- **Picture notes on the 15 screenshots** in `yt-music-downloader/assets/`. Impeccable
  wants each picture to say where it came from. The note is one text line inside the
  PNG, and the pixels stay the same. **Done 16 Oct**, wording OK'd by me: "Real
  screenshot of YT Music Downloader 1.0 or Android on the owner's phone, cropped for
  this page, Oct 2026. Not generated." Pixels checked unchanged on all 15, and
  Impeccable's scan finds none missing. Command, for new screenshots:
  `~/.claude/skills/impeccable/scripts/impeccable embed-prompt <file> --prompt "<wording>"`.
- **Stale line in `PRODUCT.md`**, line 62: "No release is uploaded yet, so no download
  link works yet." Fix it when `DESIGN.md` gets written.
- **One idea, not a fix:** the thin line between step rings could fill gold up to the
  step you're on, like the wave does.

## What's left after I pick

1. ~~Apply the picked fixes.~~ Done 16 Oct.
2. ~~Retake the same four screenshots per page into `.impeccable/review/`, with reduced
   motion on so the waves show their gold.~~ Done 16 Oct. Playwright can't open
   `file://`, so serve the folder first (`python -m http.server`).
3. ~~A fresh reviewer scores each fix resolved, partial or unresolved.~~ Done 16 Oct,
   both "ship", see the top.
4. ~~Impeccable's documenter writes `DESIGN.md` and `.impeccable/design.json` from the
   built pages.~~ Done 16 Oct. Its notes on things it left as found: the app page types
   the Warm header's colours out again, cause there's no shared stylesheet, so they
   could drift from the catalogue's. `PRODUCT.md` said Barlow is for the name only,
   but the page uses it for section headings too. My call 16 Oct: name and headings,
   so the docs got fixed, not the page.
5. ~~Update `live-design-choices/downloads-page.md` with what changed~~ Done 16 Oct, then
   commit and push.

# Second review, 26 Oct: the Windows version and the two-button card

Same way as 16 Oct, for the parts added 26 Oct: the Android phone / Windows PC switch
and everything it swaps on YT Music Downloader's page, How to use it's changes (Paste
first, "(Android only)", Play it's pictures and small switch, See the FAQ), and the
catalogue's two-button card. A fresh reviewer per page. Both said **fix**. **All 7
applied 26 Oct, my call**, after one sheet of before and after pictures
(`.playwright-cli/fix-mocks-2610/fixes-1-to-7.png`, not committed). Second round, same
reviewers: every fix resolved, **both pages "ship"**, for the fixes scored, not a fresh
full review.

[Before the review, the two surface briefs in `.impeccable/surfaces/` were brought up
to date for these parts, cause the reviewers check against them. Screenshots in
`.impeccable/review/`: both versions at 1440, 760 and 390 (`windows-*` for Windows),
the tall ones cut into `parts/`, the states the full pages don't show (`state-*`), and
each fix as built in `fixes-2610/`.]
[The reviewers had no screenshot between 900 and 1099 wide, so Claude measured every
20px from 760 to 1100 before and after. The ranges below are from that.]
[The detector found nothing to fix: only notes that some colours and font sizes aren't
in `DESIGN.md` yet.]

## Small fixes you'd barely notice

| # | Page | What was wrong | Fix |
|---|---|---|---|
| 1 | App page, both | 760 to 919 wide: the phone pictures covered the version and date at 760, and up to 919 they wrapped to 3 or 4 lines | Version and date on one line under the button at those widths |
| 2 | App page, Windows | 760 to about 780: the switch's labels broke into "Android / phone", "Windows / PC" | Window pictures 280px from 760 to 1279 (were 300), and the labels never wrap |
| 3 | App page, Windows | Setup step 1 broke "yt-music-downloader-" / "setup.exe" on desktop | The file name never breaks (`.whole`) |

## Changes you'd see, my call

| # | Page | What was wrong | Fix | Tradeoff |
|---|---|---|---|---|
| 4 | App page, both | 760 to about 990: What it's for's notes ran under the other list's crosses, and up to about 830 the page scrolled sideways. Bigger than the known "760 sideways scroll" | The two lists side by side only from 1100. Below that, "Made for" over "Not" | Taller panel on tablets |
| 5 | App page, both | On phones the file name broke in the File credit | File gets a whole row on phones | One more row, "Installs from" alone at the end |
| 6 | Catalogue | 760 to 899: the card's text in a 181px column, name on 2 lines, the line on 5, card 332px tall | Each version under its button at those widths. Card 250px at 760 | Not "version on the right" at those widths |
| 7 | Catalogue | 560 to 759: each button up to 340px wide, mostly empty gold | The two buttons stop at 440px together, about 215px each | Empty navy beside them |

**Found by me after the review, fixed 26 Oct:** on the Windows version there was a gap
and an extra line between the switch and the facts. The rule that pulls the facts up
under the switch only matched the list right after it, which is the hidden Android one.
Both reviewers missed it. Now `.os ~ .facts`, so it matches either list.

Also done, nothing on screen: the catalogue brief had Impeccable's short seed key in it,
which shouldn't be there. It now says that round's full seed reference wasn't kept.

## Left open

- **Catalogue card height jumps at 900 wide**, from the second round. 204px at 880 to
  899, 250px at 900 to 999, then 204px again. You only see it while resizing. Optional
  fix: run fix 6 up to 999 instead of 899. Not answered yet.
- At 760 the Windows File credit still breaks into two lines, cause fix 5 is phones
  only. The reviewer let it be: two lines, down from three.
- One idea from the app page's reviewer, not a fix: the Windows "Play it" library
  picture is too small to read on desktop. A click to enlarge would help.
