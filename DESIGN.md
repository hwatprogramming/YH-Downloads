---
name: YH Downloads
description: Apps I've built, ready to download. The site's own look, "Warm", which each app's page sets beside its app's own look.
colors:
  title-champagne: "#E6C88E"
  charcoal-ground: "#1B1917"
  oat-text: "#EEE7DD"
  muted-taupe: "#ADA397"
  card-ink: "#F1ECE4"
  dashed-umber: "#4A443D"
typography:
  display:
    fontFamily: "Figtree, sans-serif"
    fontSize: "min(13vw, 104px)"
    fontWeight: 750
    lineHeight: 1
    letterSpacing: "-0.035em"
  wordmark:
    fontFamily: "Figtree, sans-serif"
    fontSize: "21px"
    fontWeight: 750
    lineHeight: 1
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Figtree, sans-serif"
    fontSize: "27px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  lead:
    fontFamily: "Figtree, sans-serif"
    fontSize: "21px"
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: "Figtree, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Figtree, sans-serif"
    fontSize: "16px"
    fontWeight: 700
  meta:
    fontFamily: "Figtree, sans-serif"
    fontSize: "14px"
    fontWeight: 400
rounded:
  focus: "6px"
  chip-icon: "10px"
  icon: "16px"
  icon-wide: "22px"
  card: "28px"
  card-wide: "32px"
  pill: "999px"
spacing:
  gutter: "16px"
  gutter-wide: "40px"
  list-gap: "14px"
  list-gap-wide: "16px"
  card-pad: "20px"
  card-pad-wide: "24px"
components:
  app-card:
    textColor: "{colors.card-ink}"
    rounded: "{rounded.card}"
    padding: "20px 20px 22px"
  app-card-wide:
    textColor: "{colors.card-ink}"
    rounded: "{rounded.card-wide}"
    padding: "24px 30px 24px 24px"
  button-download:
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0 22px"
    height: "48px"
  slot-coming-soon:
    textColor: "{colors.muted-taupe}"
    rounded: "{rounded.card}"
    padding: "0 22px 0 18.5px"
    height: "76px"
  site-header:
    backgroundColor: "{colors.charcoal-ground}"
    textColor: "{colors.oat-text}"
    height: "72px"
  header-wordmark:
    textColor: "{colors.title-champagne}"
    typography: "{typography.wordmark}"
  chip-all-apps:
    textColor: "{colors.oat-text}"
    rounded: "{rounded.pill}"
    padding: "0 16px"
    height: "44px"
  chip-app:
    rounded: "{rounded.pill}"
    padding: "0 15px 0 6px"
    height: "44px"
---

# Design System: YH Downloads

## Overview

**Creative North Star: "The Soft Contents Page"**

YH Downloads is a zine's contents page, made soft: one big champagne title, one muted line, then a tight stack of rounded cards, one per app. The site's own look, "Warm", is a warm charcoal room with oat text and a single champagne-gold voice. It is professional and only slightly stylised. It never speaks for any one app; it is the shelf the apps sit on.

The site has two layers, and they never mix. **Warm** is the site's own system: the catalogue page, the sticky header on every app page, the tab icon, and the frame around each app's card. **App looks** belong to the apps: each app's own page wears that app's look, taken from the app's own DESIGN.md, and on the catalogue each app's card is filled with that app's colours. The frontmatter above is Warm only. The first app look, YT Music Downloader's Liner Notes, is recorded under "App Pages" at the end as an instance, not as tokens for future pages to inherit.

Density is low and calm: few elements, generous radii, soft ambient shadow, one accent. The user confirmed two rejections for the Warm layer: no pink, and no Bagel Fat One.

**Key Characteristics:**
- Dark, warm charcoal ground with oat text; the only accent is the champagne title.
- Figtree everywhere, heavy (750) and tightly tracked for the title.
- Round cards (28px, 32px from 760px) with no outlines and a soft drop shadow.
- Pill buttons and pill chips.
- Each app arrives as a block of its own colour on the one shared charcoal page.
- A dashed empty slot under the last app says more are coming.

## Colors

A narrow, warm, low-chroma palette: charcoal, oat and taupe neutrals, with one champagne gold.

### Primary
- **Champagne Title** (#E6C88E): The site's name, on the catalogue's title, the header's "YH Downloads" wordmark and the tab icon. Also the focus ring and the text-selection fill. It sits close to YT Music Downloader's gold but is deliberately not the same, so the site never reads as that app.

### Neutral
- **Warm Charcoal** (#1B1917): The page ground on the catalogue, the sticky header's fill on app pages, and the tab icon's tile.
- **Oat** (#EEE7DD): Body text on the charcoal ground, and the "All apps" chip's text.
- **Muted Taupe** (#ADA397): Secondary text on the charcoal: the line under the title, the dashed slot's words, the footer.
- **Card Ink** (#F1ECE4): Text on every app card, whatever the card's colour. The card's one line and version line are this ink mixed toward the card's own fill (74% ink, 64% for the faintest note), so secondary text always tints toward its card.
- **Dashed Umber** (#4A443D): The one line colour in Warm: the dashed slot's 1.5px border and the "All apps" chip's 1.5px inset ring.

### Per-app slots
Each app card sets three custom properties inline, from its app's own look: `--card` (the card's fill and the app chip's fill), `--btn` (the download button, the card's "Setup, how to use it, FAQ" link, the letter-icon fallback, the current app chip) and `--btn-text` (text on that button). These are not Warm tokens; they are the app's.

### Named Rules
**The One Champagne Rule.** Champagne is the site's name, the focus ring and the text-selection fill, nothing else. It is never an app's button colour and never a card fill.

**The Borrowed Colour Rule.** An app's colours appear only inside that app's card or chip. The ground, title, header and slot stay Warm on every page.

**The Dark Card Rule.** Card text is always Card Ink (#F1ECE4), so an app's `--card` must be dark enough to carry light text. A light-themed app brings its darkest surface to the catalogue, not its lightest.

## Typography

**Display Font:** Figtree (with sans-serif), self-hosted variable 400 to 800 from `assets/fonts/`
**Body Font:** Figtree (with sans-serif)

**Character:** One friendly geometric sans in every role, heavy and tightly tracked for the title, plain at reading sizes. The hierarchy comes from weight and size alone.

### Hierarchy
- **Display** (750, min(13vw, 104px), 1, -0.035em): The catalogue's "YH Downloads" title, in Champagne.
- **Wordmark** (750, 21px, 24px from 1100px, 1, -0.025em): "YH Downloads" in the app pages' header, linking home.
- **Title** (700, 27px from 760px, 22px below, 1.2, -0.015em): An app's name on its card.
- **Lead** (400, 21px from 760px, 19px below, 1.45): The muted line under the title, held to about 36ch.
- **Body** (400, 17px, 1.55): Default text; an app's one line on its card is 16px, held to 50ch.
- **Label** (700, 16px): The download button. Links beside it are 600, 15px. Chips are 650, 15px.
- **Meta** (400, 14px): The version line on a card (its version number in 600 Card Ink) and the footer.

### Named Rules
**The Self-Hosted Rule.** Every font comes from `assets/fonts/`, with its OFL licence beside it, loaded with `font-display: swap`. No page ever waits on another server for a font.

## Layout

The catalogue is one centred column, 1080px wide, with 16px side padding on phones and 40px from 760px. The title block sits top left; the card list follows 40px below (56px from 760px), cards stacked with a 14px gap (16px from 760px). 760px carries the whole catalogue for a one-button card. A two-button card adds two more: 360px and 900px.

From 760px a card is a three-column grid: the 80px icon, the text, and an actions column on the right with the download pill over the "Setup, how to use it, FAQ" link, both right-aligned. Under 760px a card has one left edge: the 60px icon sits beside the name, and the line, version line, a full-width download pill and the link all start at the card's left edge beneath them. The dashed slot's text lines up with the icon's left edge at every width.

A two-button card (an app with an Android and a Windows version) lays out its own way. From 760px the two buttons sit up and down in the right column, the same width, and the pair is centred on the card's height. "Setup, how to use it, FAQ" moves under the card's text on the left, so the buttons sit alone in the card's middle. From 900px each version sits to its button's right. At 760 to 899px it goes under its button instead, centred, so the text keeps more room. Under 760px the two buttons stay side by side and share the width, each with its version centred under it, and the link is centred under both. The whole button area stops at 440px, so on a small tablet the buttons aren't mostly empty colour. Under 360px the buttons get a little less padding and a smaller arrow.

On app pages the Warm header is sticky at the top, 72px tall from 760px, with the wordmark left and the chips right. Under 760px the chips take a second row of their own and scroll sideways. From 1100px the header's content lines up with the app page's own column.

**The One Left Edge Rule.** On phones a card's content starts at one left edge, and the button runs the full width.

A two-button card keeps the one left edge for its icon, name and text. Its two buttons share the width side by side instead, and its link is centred.

## Elevation & Depth

Warm is lifted, not layered: surfaces have no outlines, and depth comes from one soft, low, ambient shadow that falls well below each card. The ground is flat. The header carries a hairline highlight plus a short shadow so content scrolling under it stays separate.

### Shadow Vocabulary
- **Card Lift** (`box-shadow: 0 18px 40px -28px rgba(0,0,0,.8)`): Every app card. Large negative spread keeps it a soft pool under the card, not a halo.
- **Header Shelf** (`box-shadow: 0 1px 0 rgba(255,255,255,.05), 0 12px 24px -16px rgba(0,0,0,.9)`): The sticky site header on app pages.

### Named Rules
**The No-Outline Card Rule.** Cards are separated from the ground by colour and the Card Lift shadow, never by a border. The only lines in Warm are the dashed slot and the "All apps" ring, both Dashed Umber.

## Shapes

Everything is round. Cards are 28px (32px from 760px), app icons are rounded squares (16px, 22px from 760px), header chip icons 10px (8px from 760px), and every button and chip is a full pill (999px). The tab icon is a 14/64 rounded tile. The placeholder for apps to come is a card-shaped dashed outline (1.5px, Dashed Umber) with the card's radius, so it reads as an empty slot in the same list.

## Components

### Buttons
Warm, solid and friendly; the button always belongs to its app.
- **Shape:** Full pill (999px), at least 48px tall.
- **Download:** The app's `--btn` fill and `--btn-text` text, 700 16px, 22px side padding, an 18px stroked down-arrow SVG before the words "Download for Android". Under 760px it fills the card's width.
- **Hover:** Brightens slightly (`filter: brightness(1.07)`, 0.2s) and the arrow drops 2px (0.25s, `cubic-bezier(.16,1,.3,1)`). Hover only applies on devices that hover.
- **Focus:** 2px Champagne outline, 3px offset, 6px radius.
- **Text link:** "Setup, how to use it, FAQ" in the app's `--btn` colour, 600 15px, underlined on hover with a 4px offset.
- **Two downloads:** an app with two versions gets two buttons in the same `--btn` fill, never one solid and one quiet. They're smaller, so two fit beside the text: 44px tall, 18px side padding, 15px words, a 16px arrow, 20px apart up and down from 900px (14px at 760 to 899px). Each says "Download for Android" or "Download for Windows". Under 760px they grow to 52px and the words go in two lines left of centre, next to the arrow: "Download for" in 600 12px, the platform in 16px under it. Each button's version sits beside or under it in the Meta size, the number in 600 Card Ink.

### Cards / Containers
- **Corner Style:** 28px, 32px from 760px.
- **Background:** The app's `--card`.
- **Shadow Strategy:** Card Lift (see Elevation & Depth).
- **Border:** None.
- **Internal Padding:** 20px 20px 22px; 24px 30px 24px 24px from 760px.
- **Contents:** The app's own icon (or its first letter on `--btn` when it has no icon), the name, one line, a version line ("Version 1.0 · Android 10 and up, 64-bit phones · file name", the file name never breaking), then the actions.
- **Two versions:** a card with class `two` swaps the version line for what each version needs ("Android 10 and up, 64-bit phones · Windows 10 and 11, 64-bit", each half never breaking), with no file names. The versions move under the buttons, and the actions follow the two-button layout in Layout. A card without `two` keeps the one-button layout.

### Coming-Soon Slot
A dashed, card-shaped placeholder under the last app, reading "And more apps to come…" in 600 Muted Taupe at 17px (18px from 760px). 76px tall (84px from 760px). No fill, no shadow.

### Navigation (app pages' site header)
- **Style:** Sticky, Warm Charcoal fill, Header Shelf shadow, Figtree throughout, even on a page whose app uses other fonts.
- **Wordmark:** "YH Downloads" in Champagne, linking to the catalogue; underlined on hover.
- **All apps chip:** Transparent pill with a 1.5px Dashed Umber inset ring and Oat text, 44px tall (40px from 760px).
- **App chip:** Pill in the app's `--card` with its name in `--btn`, led by the app's icon in a 32px rounded tile (28px from 760px). The current app's chip inverts to a `--btn` fill with `--btn-text` text. Other app chips brighten on hover (`brightness(1.18)`).
- **Mobile:** The chips wrap to their own row and scroll sideways with the scrollbar hidden.

### Tab Icon
"YH" drawn as shapes in Champagne on a Warm Charcoal rounded tile (`assets/favicon.svg`), used by every page including app pages.

## Do's and Don'ts

### Do:
- **Do** keep the catalogue, the header and the tab icon in Warm on every page: Warm Charcoal, Oat, Champagne, Figtree.
- **Do** give each app's card and chip that app's own colours through `--card`, `--btn` and `--btn-text`, set inline on the card or chip.
- **Do** set card text in Card Ink and mix secondary card text toward the card's fill (74%, 64% for the faintest).
- **Do** use round shapes throughout: 28 to 32px cards, pill buttons and chips.
- **Do** gate hover effects behind `(hover:hover)` and drop transitions under `prefers-reduced-motion: reduce`.
- **Do** load every font from `assets/fonts/` with its licence beside it.

### Don't:
- **Don't** use pink or Bagel Fat One anywhere in Warm.
- **Don't** use Champagne for an app's button, card or link; it is the site's name colour.
- **Don't** give a card an outline; separate it with its colour and the Card Lift shadow.
- **Don't** carry an app's colours or fonts into the header, the ground or the title.
- **Don't** give a future app's page navy, gold, Barlow Condensed or Roboto because YT Music Downloader's page has them; those are that app's, not the site's.

## App Pages

Each app has its own page, and that page wears the app's own look, taken from the app's own DESIGN.md in its private repo. Only the sticky header at the top stays Warm (see Navigation). The tab icon stays the site's "YH". An app look is recorded here per app, as an instance; nothing in it is a site token.

**The Own Look Rule.** A new app's page starts from that app's DESIGN.md, not from another app's page. Copy the page's structure if it fits, never its colours or fonts.

### First instance: YT Music Downloader, "Liner Notes"

Source: the app repo's DESIGN.md. Navy ground, warm ink, one gold, set like an album's liner notes.

**Colours** (as `:root` custom properties on `yt-music-downloader/index.html`):
- Navy Ground (#0F151D): page ground.
- Navy (#16202C): the gold pill's text; the app's `--card` and `--btn-text` on the catalogue.
- Panel (#1C2734): the "What it's for" panel, the fill of the app's Help pop-up.
- Highest (#23303F): hairlines, phone and screenshot borders, tick and cross discs.
- Outline (#3A4757): step rings, dotted leaders, the wave's unplayed part, scrollbar thumb.
- Warm Ink (#ECE7DE): body text.
- Grey (#9AA4B1): secondary text, credit labels, captions, idle tabs, the facts' ticks.
- Gold (#EDBB4E): kept for what you tap and for progress (the download pill, tab underlines, the active step's ring, the FAQ plus, "Back to top", the wave's played part), plus "YT" in the name, echoing the app icon. It is the app's `--btn` on the catalogue. Pill hover: #F4C866.

**Type:**
- Barlow Condensed 700, uppercase, 0.04em tracking: the app's name (min(15vw, 116px), line-height 0.9, two lines) and section headings (36px, 44px from 760px). Until Barlow loads, the name draws in a local Roboto or Arial shrunk with `size-adjust: 67%`, so "DOWNLOADER" never cuts off.
- Roboto 400 for text (17px, 1.5), 500 for emphasis, step titles, tabs and the pill. Hook 19px, 22px from 1100px.
- Credit labels: 700, 11.5 to 12px, 0.14em tracking, uppercase, Grey; they label a fact or a list ("File", "Size", "Made for", "Not").

**Layout:** one 1200px column with a 20px gutter (32px from 760px, 56px from 1100px). The first screen puts name, hook, the version switch, facts, the pill with its version and date, and the credits on the left, and the phone stack (or the window stack) on the right from 760px; on phones the pill comes before the picture. The version and date sit beside the pill from 920px, and on one line under it at 760 to 919px, so the pictures beside them don't cover them. Under 560px the File credit takes a whole row. Below, the switch shows again, then Setup and How to use it sit side by side from 900px, then What it's for and the FAQ across both columns. What it's for puts "Made for" and "Not" side by side only from 1100px, where both lists have room for their notes; below that "Made for" sits above "Not". Breakpoints: 560px, 760px, 900px, 920px, 1100px, 1280px.

**Components:**
- **Gold pill:** 56px tall, full pill, Gold fill, Navy text, 500 16px, at least 320px wide from 760px, pressing down 1px.
- **Text tabs:** Grey labels, Warm Ink when selected, a 2px Gold underline that scales in (0.35s).
- **Phone stack:** three real screenshots, the front one centred, the other two dimmed to half brightness and peeking out each side; picking one swaps it into the centre (0.55s, `cubic-bezier(.16,1,.3,1)`).
- **Numbered steps:** 34px rings on a 1px Highest line; a step with a picture takes a Gold ring while its screen shows.
- **Credits lines:** a tick or cross in a 30px Highest disc, the item, a 2px dotted Outline leader, a short Grey note.
- **Sound-wave divider:** a 32px bar-wave mask between section groups, its Gold part filling a third, two thirds, then all of it, animated on scroll where the browser supports it.
- **FAQ:** hairline-ruled disclosures, a Gold plus that turns to a cross when open.
- **Version switch:** "Android phone / Windows PC", the text tabs made bigger (500 17px, 48px tall, 30px apart), each led by a 20px drawn phone or PC, on a 1px Highest rule up to 420px wide. The whole page follows it. It sits under the hook, with the facts straight under it and no rule of their own on top, and again where the details start, after a Grey "Steps and answers for" and with no rule. Both move together. Which one shows is set in the page's head before anything draws, a Windows PC on Windows and everyone else on Android, and `?os=` in the link picks one.
- **Window stack:** the phone stack with the Windows app's windows in it. Same swap and dimming, an 8px corner, the side ones peeking out by a tenth of its width. min(80vw, 330px) wide on phones, 280px from 760px, 420px from 1280px.
- **Android-only tag:** "(Android only)" after a tab's name in plain Grey 400, not small capitals. The tab is 40px from the next one, and on narrow phones the tag drops under the name.
- **Mini switch:** small text tabs (500 14px, 36px tall, 18px apart) above a step's pictures, the same Gold underline, for when a picture has an Android and a Windows version. It starts on the version you're on, swaps only the pictures and caption, and shows only while its step's picture does.
- **See the FAQ link:** at the end of a step's Grey words, in the same Grey, underlined in Outline with a 3px offset; Gold text and underline on hover. It opens its FAQ answer, not just scrolls to it.
- **Two pictures in a step:** one under the other, 10px apart, in the same rounded Highest frame as one.
- **Whole file names:** a file name inside a step never breaks, at its hyphens or anywhere.
- **Hairlines:** 1px Highest everywhere a rule is needed; no shadows inside the app's own look.
