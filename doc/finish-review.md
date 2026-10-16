# Finish review of the live site

Impeccable's finish review of the two live pages, 16 Oct 2026. Each page got a fresh
reviewer. Both said **fix**: the look matches what I picked, nothing gets redesigned,
just small fixes. **All 11 applied 16 Oct, my call**, after seeing each as a before and
after picture.

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
  stand-in name comes out 309px against Barlow's 310px at 390 wide. Still to check on a
  phone.]

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
  PNG, and the pixels stay the same (tested on a copy). Wording Claude proposed for all
  of them, not yet OK'd: "Real screenshot of YT Music Downloader 1.0 or Android on the
  owner's phone, cropped for this page, Oct 2026. Not generated." Command:
  `impeccable embed-prompt <file> --prompt "<wording>"`.
- **Stale line in `PRODUCT.md`**, line 62: "No release is uploaded yet, so no download
  link works yet." Fix it when `DESIGN.md` gets written.
- **One idea, not a fix:** the thin line between step rings could fill gold up to the
  step you're on, like the wave does.

## What's left after I pick

1. Apply the picked fixes.
2. Retake the same four screenshots per page into `.impeccable/review/`, with reduced
   motion on so the waves show their gold. Playwright can't open `file://`, so serve the
   folder first (`python -m http.server`).
3. A fresh reviewer scores each fix resolved, partial or unresolved. This session's
   reviewers don't carry over.
4. Impeccable's documenter writes `DESIGN.md` and `.impeccable/design.json` from the
   built pages.
5. Update `live-design-choices/downloads-page.md` with what changed, then commit and push.
