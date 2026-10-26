# Repo journal

[My own entries about this project, oldest first, all in this one file. Each entry is
in my words. Claude fixes grammar, spelling and small things like that, as long as
the meaning and most of my wording stay the same. Nothing gets added to an entry. A new entry goes at the end of the entries, above "Repo summary".

Claude keeps the Repo summary up to date from the entries.]

## 13 Oct 2026, I want it to be a GitHub page

I want it to be a GitHub page. It'll just be a long page of my downloads, and it's separated by sections. Each section is one app, and contains the app details and the download links, as well as some image of the app.

## 13 Oct 2026, Opting out of adding apps by myself

I think I'd opt out of the "You can add the next app yourself without me" for this repo, because if I'm developing any repo, it means I have a Claude sub, which means I can ask you to upload and design each section for me.

[Note by Claude: the quoted line was Claude's. It was the third part of what Claude
read "done" to mean for this repo, taken from the independence rule in my global
`CLAUDE.md`. The other two parts were "page is live in that layout" and "first app is
on it".]

## 13 Oct 2026, Each section gets its own theme

Each section gets its own theme, based on the project it's built on.

## 26 Oct 2026, The Windows version on the same page

I want the catalogue to have 2 buttons, one for the APK and one more for Windows. As for
YT Music Downloader, I haven't decided if I want to merge them or make them separate.
Overall I think a lot of wordings need to get reviewed to support both APK and Windows,
or perhaps 2 tabs in the app page, APK and Windows (desktop).

I'm leaning tabs/merged.

I like tabs.

## 26 Oct 2026, How to use it, and Play it

For Share from YT Music, there should be a (mobile/Android only) label. I think a plain
(Android only) would work better, and add some padding so that it's not too near the next
tab. Then the default should be Paste a link, and it's the first tab.

Also, on a side note, my friend pointed out that in How to use it, point 5 isn't
clickable, so maybe you can just screenshot the song in a default player or something?

Also add a note that not all phones have a default player, and some of them may be
YouTube Music, so... a suggestion is to either figure out if their phone has an
uninstalled default player, or they can install a 3rd party music player.

At Play it, 2 tabs appear as well, Windows and Android. I think a good place to put it is
above the images.

Also 2 more screenshots from Windows, 1 in Media Player and one in the music player. Help
me blur out other songs and personal info.

## 26 Oct 2026, Two buttons on the catalogue card

Two gold buttons side by side, each with its version under it. Make the button smaller,
push the text to the left a bit more to squeeze 2 buttons.

Try up and down for desktop, mobile one is fine. Version to the right of the button.
Centre the 2 buttons: basically shift it downwards, such that the centre of the 2 buttons
aligns with the whole tab's centre.

Too much padding on top. Actually it looks good already, add a bit more gap between the
buttons.

Great.

For Android, the Setup, how to use it, FAQ should be centred.

## 26 Oct 2026, Picking which version to install

I'm thinking I should allow users to choose the version they want to install in the app
page. The catalogue page should show the latest version, for simplicity. A changelog and
the difference in between versions would be nice too.

## 26 Oct 2026, A version picker for every app with more than one version

Can we make the version picker something that every app uploaded that has more than 1
version should have? How do we enforce this? Just put it in CLAUDE.md, or?

## 26 Oct 2026, Picking the version picker's look

For the version picker, I like A.

# Repo summary

[Kept by Claude, built from the entries above. Every line carries the date of the
entry it came from, e.g. `[6 Oct]`, so the reasoning is one jump away.]

## Problems

[What I ran into that this app is for.]

## Ideas and features

- A GitHub page of my downloads. [13 Oct]
- One section per app. A section has the app details, the download links and some
  image of the app. [13 Oct]
- Claude uploads each app and designs its section when I ask. [13 Oct]
- The catalogue card has 2 buttons, one for the APK and one for Windows. [26 Oct]
- YT Music Downloader's page has Android and Windows tabs. [26 Oct] [Mockup in
  `.impeccable/mocks/both-platforms/src/tabs.html`, reasons in
  `doc/live-design-choices/downloads-page.md`.]
- In How to use it, Paste a link is the first tab and opens first, and Share from YT
  Music says "(Android only)". [26 Oct]
- Play it shows a song in the default music player, with a Windows / Android switch
  above the pictures. [26 Oct]
- A note for phones with no default music player, or only YouTube Music: check whether
  the phone's own player was uninstalled, or install a 3rd party one. [26 Oct] [It's
  under Play it and in the FAQ.]
- Screenshots on the page get other songs and personal info blurred. [26 Oct]
- On an app's page, people can choose which version to install. [26 Oct] [Not started.
  The upload steps in `doc/uploading-a-build.md` replace the old file on every update,
  so old versions are gone after an update. Keeping them changes how uploads work.]
- The catalogue shows only the latest version, for simplicity. [26 Oct]
- A changelog, and the difference between versions, would be nice too. [26 Oct]
- Every uploaded app with more than 1 version has the version picker. [26 Oct] [How
  it's made to stick isn't decided: a step in `doc/uploading-a-build.md`, a picker
  built from a list of versions, or a check script.]

## Goals

[Checkboxes. All ticked means the app is done. A goal I drop moves to Rejected with
the date and why, never gets deleted.]

1. [ ] The GitHub page is live: one long page, a section per app, each with the app
   details, the download links and some image of the app. [13 Oct]
2. [ ] The first app is on it. [13 Oct]
   [Goal 2 isn't in my words. It's from Claude's reading of "done" on 13 Oct. I opted
   out of the third part of that reading and left this one.]

## Rejected

[Ideas and goals dropped, with the date and why.]

- Adding the next app by myself, without Claude. Opted out for this repo. If I'm
  developing any repo I have a Claude sub, so I can ask Claude to upload and design
  each section. [13 Oct]
- Merging Android and Windows into one page's wording, or a page each: tabs instead.
  [26 Oct]
- "(Android only)" in small spaced capitals: plain works better. [26 Oct]
- On the catalogue card on desktop, the 2 buttons side by side, or with the version
  under each: up and down, version to the right. The link under the buttons with space
  above to centre them: too much padding on top. [26 Oct]

## Look

[Layout, font, colours, and why they were picked.]

- One long page, separated by sections, one section per app. [13 Oct]
- Each section gets its own theme, based on the project it's built on. [13 Oct]
- "(Android only)" is plain, with some padding before the next tab. [26 Oct]
- The version picker is A: a menu beside the download button, with each version's date
  and what changed. [26 Oct] [Mockups in `.impeccable/mocks/version-picker/`, B and C
  in `doc/live-design-choices/downloads-page.md`.]
- The catalogue card's 2 buttons are gold and smaller. On desktop they're up and down
  with the version to the right of each, a bit more gap between them, and their centre
  on the card's centre. On phones they're side by side, the words pushed left, with
  the version under each and "Setup, how to use it, FAQ" centred. [26 Oct] [Picture:
  `.impeccable/mocks/both-platforms/catalogue-two-buttons.png`.]
