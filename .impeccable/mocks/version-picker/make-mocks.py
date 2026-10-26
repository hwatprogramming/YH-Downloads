"""Builds the version picker mockups from the live app page.

Each mockup is a copy of yt-music-downloader/index.html with one way of picking a
version added. The versions are made up for the mockup: only 1.0 is real.
Run from the repo root: python .impeccable/mocks/version-picker/make-mocks.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
live = open(os.path.join(ROOT, '..', '..', '..', 'yt-music-downloader', 'index.html'), encoding='utf-8').read()

# Example versions, newest first. Only 1.0 is real.
VERSIONS = [
    ('1.2', '30 Nov 2026', 'Big playlists start faster. Album covers fixed on some songs.', 'About 68 MB'),
    ('1.1', '12 Nov 2026', 'Retry all, for every failed song at once.', 'About 67 MB'),
    ('1.0', '15 Oct 2026', 'First version.', 'About 67 MB'),
]
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11"/><path d="M7 11l5 5 5-5"/><path d="M5 20h14"/></svg>'
CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>'

OLD_VER = '<p class="ver"><span class="v">Version 1.0</span><span class="d">15 Oct 2026</span></p>'
SPECS = '<dl class="specs" data-for="android">'
END = '<div class="end">'
assert live.count(OLD_VER) == 1 and live.count(SPECS) == 1 and live.count(END) == 1

# Shared: assets resolve from the live page's folder, and the mockup always opens on
# Android, so every mockup shows the same version.
base = live.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="../../../../yt-music-downloader/">', 1)
base = base.replace("forced || (/Windows/i.test(navigator.userAgent) ? 'windows' : 'android')", "'android'")
NEW_VER = '<p class="ver"><span class="v">Version 1.2</span><span class="d">30 Nov 2026</span></p>'

CSS_COMMON = """
/* Mockup: picking a version. A small grey label in the credits style. */
.lab{font-size:11.5px; font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--grey)}
.vdl{display:inline-flex; align-items:center; gap:8px; min-height:44px; color:var(--gold); font-size:15px; font-weight:500; text-decoration:none; white-space:nowrap}
.vdl svg{width:18px; height:18px; flex:none}
.vdl .z{color:var(--grey); font-weight:400}
"""

# A: the version line beside the button becomes a menu. Open here, to show it.
CSS_A = CSS_COMMON + """
.vpick{position:relative; justify-self:start}
/* As tall as the gold pill beside it, with room around the two lines. */
.vbtn{display:inline-flex; align-items:center; gap:24px; min-height:56px; padding:9px 16px 9px 20px; border:1px solid var(--outline); border-radius:16px; background:none; color:var(--ink); font:500 15px/1.4 'Roboto',sans-serif; text-align:left; cursor:pointer}
.vbtn span{display:grid; row-gap:2px}
.vbtn .d{color:var(--grey); font-weight:400}
.vbtn svg{width:18px; height:18px; color:var(--gold); transform:rotate(180deg)}
.vmenu{position:absolute; z-index:5; left:0; top:calc(100% + 8px); width:min(340px, calc(100vw - 40px)); margin:0; padding:4px 0; list-style:none; background:var(--panel); border:1px solid var(--outline); border-radius:16px}
.vmenu li{display:grid; grid-template-columns:18px minmax(0,1fr) auto; column-gap:12px; row-gap:2px; padding:12px 16px}
.vmenu li + li{border-top:1px solid var(--highest)}
.vmenu .ck{grid-row:span 2; width:18px; height:18px; color:var(--gold); margin-top:1px}
.vmenu .v{font-weight:500}
.vmenu .d{color:var(--grey); font-size:14px}
.vmenu .s{grid-column:2 / -1; font-size:14px; line-height:1.4; color:var(--grey)}
.vmenu .lab{align-self:center}
"""
def html_a():
    items = []
    for i, (v, d, s, z) in enumerate(VERSIONS):
        ck = f'<span class="ck">{TICK}</span>' if i == 0 else '<span class="ck"></span>'
        lab = '<span class="lab">Latest</span>' if i == 0 else '<span></span>'
        items.append(f'<li>{ck}<span><span class="v">Version {v}</span> <span class="d">· {d}</span></span>{lab}<span class="s">{s}</span></li>')
    return ('<div class="vpick"><button class="vbtn" aria-expanded="true"><span><span class="v">Version 1.2</span>'
            '<span class="d">30 Nov 2026 · Latest</span></span>' + CHEVRON + '</button>'
            '<ul class="vmenu">' + ''.join(items) + '</ul></div>')

# B: the button stays on the newest. A link under its version goes to a Versions
# section near the end, set like the FAQ: one row per version, what changed, and a
# download for each.
CSS_B = CSS_COMMON + """
.ver .older{width:100%; margin-top:2px; color:var(--grey); text-decoration:underline; text-underline-offset:3px; text-decoration-color:var(--outline)}
.vers{grid-column:1 / -1}
.vlist{margin:0; padding:0; list-style:none; border-top:1px solid var(--highest)}
.vlist li{display:grid; grid-template-columns:minmax(0,1fr) auto; column-gap:32px; row-gap:4px; padding:16px 0; border-bottom:1px solid var(--highest)}
.vlist .row{display:flex; flex-wrap:wrap; align-items:baseline; column-gap:14px}
.vlist .t{font-size:17px; font-weight:500}
.vlist .d{font-size:15px; color:var(--grey)}
.vlist p{grid-column:1; margin:0; max-width:62ch; font-size:15px; color:var(--grey)}
.vlist .vdl{grid-column:2; grid-row:1 / span 2; align-self:center}
@media (max-width:559px){.vlist li{grid-template-columns:minmax(0,1fr)} .vlist .vdl{grid-column:1; grid-row:auto; justify-self:start}}
"""
def html_b_section():
    rows = []
    for i, (v, d, s, z) in enumerate(VERSIONS):
        lab = '<span class="lab">Latest</span>' if i == 0 else ''
        rows.append(f'<li><div class="row"><span class="t">Version {v}</span><span class="d">{d}</span>{lab}</div>'
                    f'<p>{s}</p><a class="vdl" href="#">{ARROW}Download {v} <span class="z">· {z}</span></a></li>')
    return ('<section class="vers" id="versions"><h2>Versions</h2><ol class="vlist">' + ''.join(rows) + '</ol></section>\n\n    ')

# C: under the button, "All versions" opens a panel right there, with what changed
# and a download for each. Open here, to show it.
CSS_C = CSS_COMMON + """
.allv{max-width:520px; margin-top:16px}
.allv summary{display:inline-flex; align-items:center; gap:10px; min-height:44px; color:var(--ink); font-size:16px; font-weight:500; cursor:pointer; list-style:none}
.allv summary::-webkit-details-marker{display:none}
.allv summary svg{width:18px; height:18px; color:var(--gold); transition:transform .3s cubic-bezier(.16,1,.3,1)}
.allv[open] summary svg{transform:rotate(180deg)}
.allv summary .n{color:var(--grey); font-weight:400}
.allv ol{margin:6px 0 0; padding:4px 20px; list-style:none; border-radius:20px; background:var(--panel)}
.allv li{display:grid; grid-template-columns:minmax(0,1fr) auto; column-gap:20px; row-gap:2px; padding:14px 0}
.allv li + li{border-top:1px solid var(--highest)}
.allv .row{display:flex; flex-wrap:wrap; align-items:baseline; column-gap:12px}
.allv .t{font-weight:500}
.allv .d{font-size:14px; color:var(--grey)}
.allv p{grid-column:1; margin:0; font-size:14px; line-height:1.4; color:var(--grey)}
.allv .vdl{grid-column:2; grid-row:1 / span 2; align-self:center; font-size:15px}
@media (min-width:760px){.allv{grid-column:1}}
"""
def html_c():
    rows = []
    for i, (v, d, s, z) in enumerate(VERSIONS):
        lab = '<span class="lab">Latest</span>' if i == 0 else ''
        rows.append(f'<li><div class="row"><span class="t">Version {v}</span><span class="d">{d}</span>{lab}</div>'
                    f'<p>{s}</p><a class="vdl" href="#">{ARROW}{v}</a></li>')
    return ('<details class="allv" data-for="android" open><summary>' + CHEVRON + 'All versions and what changed '
            '<span class="n">(3)</span></summary><ol>' + ''.join(rows) + '</ol></details>\n    ')

def write(name, css, html):
    out = html.replace('</style>', css + '</style>', 1)
    open(os.path.join(ROOT, 'src', name), 'w', encoding='utf-8').write(out)
    print('wrote', name)

a = base.replace(OLD_VER, html_a())
write('a-menu.html', CSS_A, a)

b = base.replace(OLD_VER, NEW_VER.replace('</p>', '<a class="older" href="#versions">Older versions and what changed</a></p>'))
b = b.replace(END, html_b_section() + END)
write('b-versions-section.html', CSS_B, b)

c = base.replace(OLD_VER, NEW_VER).replace(SPECS, html_c() + SPECS)
write('c-under-the-button.html', CSS_C, c)
