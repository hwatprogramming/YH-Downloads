---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Catalogue

Scope: the site's home page, `index.html`, the list of every app. Mode: Operate. The
visitor succeeds when they find an app and get its file, or open its page.

- Audience: me, people I send the link to, strangers who land on it.
- Job: see what apps there are, tell what each does from one line, then download from
  the card or open the app's page.
- Content: real apps only. Name, one line, version, what it runs on (and 64-bit when the
  app needs it). A one-download card also has the file name. No user counts, reviews or
  ratings exist, so none appear.
- An app with an Android and a Windows version gets two buttons on its card (class
  `two`), one per file, each with its version. YT Music Downloader is the first.
- Constraints: the site's own look, apart from every app's. Each app's card wears that
  app's colours. Dark. Download links never change. Fonts come from the site itself
  (`assets/fonts/`), never another server. Tab icon: "YH" in champagne on charcoal.
- Memorable moment: each app arrives as a block of its own colour on one shared warm
  charcoal page.
- Unresolved: nothing on this page. The Support me page is parked in `doc/backlog.md`.

Written 2026-10-16 from what shipped, before the finish review. The build went straight
from the picked mockup to the site with no contract on record. Updated the same day after
the review fixes and the user's new phone card layout (one left edge, full-width button).
Updated 2026-10-26 for the two-button card, built from the OK'd mockup
`.impeccable/mocks/both-platforms/src/catalogue.html`, before its finish review.

## Direction contract

THESIS: a zine's contents page, made soft. A big title, then a tight list where each app
is one rounded card carrying its own download button. It refuses the app-store grid of
icon tiles with ratings, and it refuses reading as any one app's landing page.

OWN-WORLD: warm charcoal ground `#1B1917`, oat text `#EEE7DD`, muted `#ADA397`, a
champagne-gold title `#E6C88E`. Figtree everywhere, 750 for the title. Round panels
(28 to 32px) with no outlines and a soft drop shadow, pill buttons. Each card takes its
app's own card and button colours while the page around it stays one look. A dashed
empty slot says more apps are coming.

STORY: the visitor reads "YH Downloads" and one line, sees each app as its own coloured
card, tells what it does from one line, and downloads from the card or opens its page.

FIRST VIEWPORT: champagne title top left, up to 104px, one muted line under it at about
36ch. Below it the cards span the 1080px column: 80px icon left, name at 27px, the line,
a version line; from 760px the download pill and "Setup, how to use it, FAQ" stack on
the right. On phones (under 760px) the card has one left edge: the 60px icon sits beside
the name, and the line, the version line, a full-width download pill and the link all
start at the card's left edge under them. The dashed slot's text lines up with the icon
at every width. The first app's download button is inside the first viewport at 390px
and at 1440px.

TWO-BUTTON CARD: two gold pills in the app's colours, smaller than the one-button card's
(44px tall, 15px words), each "Download for Android" / "Download for Windows" with its
version. The line under the card's text says what each runs on: "Android 10 and up,
64-bit phones · Windows 10 and 11, 64-bit". No file names on this card. From 760px the
two buttons are up and down at the right, the same width, 20px apart, each with its
version to its right, and their middle lines up with the card's middle. "Setup, how to
use it, FAQ" moves under the card's text on the left. The card is 204px tall. On phones
the two buttons sit side by side, sharing the width, each with "Download for" small over
the platform, left, next to the arrow, and its version centred under it. "Setup, how to
use it, FAQ" is centred under them. The rest of the phone card keeps one left edge.

FORM: the Contents page (round 1's pick) restyled as Warm (round 3, `soft-warm`). That
round's full seed reference wasn't kept. Changed from the mockup: champagne title, cards in each app's colours,
placeholder apps out, dashed slot in.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
