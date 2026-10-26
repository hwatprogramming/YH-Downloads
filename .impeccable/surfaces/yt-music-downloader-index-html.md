---
version: 1
slug: "yt-music-downloader-index-html"
primary_target: "yt-music-downloader/index.html"
related_targets: []
---

# YT Music Downloader's page

Scope: one app's page, `yt-music-downloader/index.html`, with two versions of the app
on it: Android phone and Windows PC. Mode: Persuade. The visitor succeeds when they
understand what the app does, trust it enough to install it from outside the Play Store
or the Microsoft Store, download the right file and get it set up.

- Audience: me, people I know, strangers. Most download the APK on the Android phone it's
  for, so phone width counts most. The Windows installer gets downloaded on a PC, so
  desktop width counts for that version.
- Job: show the app off like a small landing page, with the download right there. Then
  Setup, How to use it, What it's for, and the FAQ. An "Android phone / Windows PC"
  switch under the app's line picks the version, and the whole page follows it.
- Proof: real screenshots of Android 1.0 (Download, History, Help) and Windows 1.0.0
  (Downloading, History, Help), real install screenshots for both, the phone's music
  player and Windows' Media Player playing a downloaded song, and facts from the app's
  repos. Nothing invented. The Download tabs' songs are labelled as made up or test
  songs. Private parts (other songs, the username) are blurred or cropped out.
- Constraints: wears the app's own look, Liner Notes. The site header is in the
  catalogue's Warm look. Version and date sit beside each version's button. "Is this
  legal?" stays out of the FAQ for good. Only what's true and public. Fonts come from the
  site itself (`assets/fonts/`), never another server. The site's "YH" tab icon, not the
  app's. A Windows PC opens on Windows, everything else on Android, set before the page
  draws. `?os=android` or `?os=windows` on the link picks one.
- Memorable moment: three real screens in a stack with the app's tab style over them
  (phones on Android, the app's windows on Windows), and a sound wave between section
  groups that fills gold as you scroll.
- Unresolved: whether the sticky header goes to one row on phones.

Written 2026-10-16 from what shipped, before the finish review. The build went straight
from the picked mockup to the site with no contract on record. Updated the same day
after the user's stack change and the review fixes: the front phone moved to the centre,
the tabs became Help, Download, History, step screens open inside the step on phones,
and the phone cut-off was found and fixed (the name in its stand-in font on a slow load).
Updated 2026-10-26 for the Windows version, built from the OK'd mockup
`.impeccable/mocks/both-platforms/src/tabs.html`, before its finish review.

## Direction contract

THESIS: neat, important stuff first, then the details. The app's name set like its own
title, the real app in a stack beside it, and every detail a short titled step next to
the real screen it describes. It refuses the stock phone-mockup hero over a feature grid
and testimonials.

OWN-WORLD: Liner Notes, from the app's `DESIGN.md`. Navy ground `#0F151D`, navy
`#16202C`, panel `#1C2734`, highest `#23303F`, outline `#3A4757`, warm ink `#ECE7DE`,
grey `#9AA4B1`, one gold `#EDBB4E` kept for what you tap and for progress. Barlow
Condensed 700 capitals for the name and section headings, Roboto for the rest. Until
Barlow arrives, the name draws in Roboto shrunk to Barlow's width, so it never cuts off.
Hairlines, small spaced-capital credit labels, the gold pill, text tabs with a gold
underline, numbered rings on a thin line, credits lines with dotted leaders.

STORY: the visitor reads the name and one line, sees the page is already on their
version (or switches it), three facts, the button with its version and date and the
file's credits, and the real app. Below, they learn how to get past Play Protect or
SmartScreen, how to use it, what it is and isn't, and find answers.

FIRST VIEWPORT: one 1200px column. From 1280px, left: two-line name up to 116px with
"YT" in gold, hook at 22px, the version switch (the app's text tabs, bigger, 17px, a
drawn phone and a drawn PC, gold underline on the picked one, up to 420px wide), three
ticked facts on hairlines under it, the gold pill (at least 320px) with version and date
beside it, then credits in two columns. Right: the stack, the front screen in the centre
and the other two peeking out one each side, dimmed. On Android, 320px phones with Help,
Download and History tabs over it. On Windows, the app's windows at 420px (300px at
760px, up to 330px on phones), with Help, Downloading and History. A caption under it.
On phones, one column, the name at 15vw, and the download button is on the first screen
at 390px with the picture after it.

SIGNATURE INTERACTION: the version switch swaps every part of the page at once: facts,
button, version and date, credits, screens, Setup, How to use it, What it's for's items
and the FAQ. The same switch shows again where the details start, after "Steps and
answers for", and both move together. A tab over the stack, or a click on a peeking
screen, swaps that screen with the centre one (0.55s ease-out). The tabs stay in one
order and the gold underline moves. On load the side screens match the tabs: Help left,
History right. A step with a picture shows its real screen beside the steps and takes a
gold ring. On phones (under 560px) the screen opens inside the tapped step, under its
text, and a grey line under Setup and How to use it says "Tap a step to see its screen."
On Android, How to use it has two text tabs, "Paste a link" (first, open by default) and
"Share from YT Music" with "(Android only)" in plain grey after it. "Play it" has its own
small Android phone / Windows PC switch above its pictures, starting on the version
you're on, so either player can be seen from either version. Windows' "Play it" shows two
pictures, one under the other. Each "Play it" ends on "See the FAQ", which opens that
answer. The wave fills gold on scroll: a third, two thirds, then all of it by the FAQ.

FORM: user-pinned. The Two-Ink Riso layout (a challenger in the first direction round),
re-skinned in the app's Liner Notes look on 2026-10-16. The surface round `626a70e0`
drew three fresh structures (album back cover, app screen, tags before and after), and
all three lost to it. The Windows version came in 2026-10-26 as the Tabs direction, over
Merged (one page for both, two buttons, one table of files) and a page each.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
