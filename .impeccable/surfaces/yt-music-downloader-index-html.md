---
version: 1
slug: "yt-music-downloader-index-html"
primary_target: "yt-music-downloader/index.html"
related_targets: []
---

# YT Music Downloader's page

Scope: one app's page, `yt-music-downloader/index.html`. Mode: Persuade. The visitor
succeeds when they understand what the app does, trust it enough to install an APK from
outside the Play Store, download it and get it set up.

- Audience: me, people I know, strangers. Most download on the Android phone it's for,
  so phone width counts most.
- Job: show the app off like a small landing page, with the download right there. Then
  Setup, How to use it, What it's for, and the FAQ.
- Proof: real 1.0 screenshots (Download, History, Help), real install screenshots, and
  facts from the app's repo. Nothing invented. The Download tab's songs are labelled as
  made up for the picture.
- Constraints: wears the app's own look, Liner Notes. The site header is in the
  catalogue's Warm look. Version and date sit beside the button. "Is this legal?" stays
  out of the FAQ for good. Only what's true and public.
- Memorable moment: three real phone screens in a stack with the app's tab style over
  them, and a sound wave between section groups that fills gold as you scroll.
- Unresolved: whether the sticky header goes to one row on phones. A phone cut-off seen
  on the old Riso page that couldn't be reproduced.

Written 2026-10-16 from what shipped, before the finish review. The build went straight
from the picked mockup to the site with no contract on record.

## Direction contract

THESIS: neat, important stuff first, then the details. The app's name set like its own
title, the real app in a stack beside it, and every detail a short titled step next to
the real screen it describes. It refuses the stock phone-mockup hero over a feature grid
and testimonials.

OWN-WORLD: Liner Notes, from the app's `DESIGN.md`. Navy ground `#0F151D`, navy
`#16202C`, panel `#1C2734`, highest `#23303F`, outline `#3A4757`, warm ink `#ECE7DE`,
grey `#9AA4B1`, one gold `#EDBB4E` kept for what you tap and for progress. Barlow
Condensed 700 capitals for the name and section headings, Roboto for the rest.
Hairlines, small spaced-capital credit labels, the gold pill, text tabs with a gold
underline, numbered rings on a thin line, credits lines with dotted leaders.

STORY: the visitor reads the name and one line, three facts, sees the button with its
version and date and the file's credits, and sees the real app. Below, they learn how to
get past Play Protect, the two ways to use it, what it is and isn't, and find answers.

FIRST VIEWPORT: one 1200px column. From 1280px, left: two-line name up to 116px with
"YT" in gold, hook at 22px, three ticked facts on hairlines, the gold pill (at least
320px) with version and date beside it, then credits in two columns. Right: a 320px
phone stack with Download, History and Help tabs over it and a caption under it. On
phones, one column, and the download button is on the first screen at 390px with the
picture after it.

SIGNATURE INTERACTION: a tab over the stack, or a click on a peeking phone, brings that
screen to the front (0.55s ease-out). A step with a picture shows its real screen beside
the steps and takes a gold ring. The wave fills gold on scroll: a third, two thirds, then
all of it by the FAQ.

FORM: user-pinned. The Two-Ink Riso layout (a challenger in the first direction round),
re-skinned in the app's Liner Notes look on 2026-10-16. The surface round `626a70e0`
drew three fresh structures (album back cover, app screen, tags before and after), and
all three lost to it.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
