# Shared design-system CSS + helpers for PLMK 트렌드 pages
from icons import ICONS

PALETTE = {
    "lime": "#E8F26B",
    "lilac": "#D9CCFF",
    "coral": "#FF9F80",
    "pink": "#FFC2DD",
    "mint": "#A6F0CB",
    "ink": "#111111",
    "paper": "#FFFFFF",
    "gray": "#6B6B6B",
    "hair": "#E3E1DC",
    "cream": "#FAF9F6",
}

FONT_FACE_CSS = """
@font-face {
  font-family: 'Pretendard';
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url(data:font/woff2;base64,{{PRETENDARD_REGULAR_B64}}) format('woff2');
}
@font-face {
  font-family: 'Pretendard';
  font-weight: 600;
  font-style: normal;
  font-display: swap;
  src: url(data:font/woff2;base64,{{PRETENDARD_SEMIBOLD_B64}}) format('woff2');
}
@font-face {
  font-family: 'Pretendard';
  font-weight: 700;
  font-style: normal;
  font-display: swap;
  src: url(data:font/woff2;base64,{{PRETENDARD_BOLD_B64}}) format('woff2');
}
"""

BASE_CSS = """
:root{
  --ink:#111111; --paper:#FFFFFF; --gray:#6B6B6B; --hair:#E3E1DC; --cream:#FAF9F6;
  --lime:#E8F26B; --lilac:#D9CCFF; --coral:#FF9F80; --pink:#FFC2DD; --mint:#A6F0CB;
}
@media (prefers-color-scheme: dark){
  :root{ --paper:#FFFFFF; --cream:#FAF9F6; }
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:var(--paper);color:var(--ink);}
body{
  font-family:'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
  font-weight:400; -webkit-font-smoothing:antialiased; line-height:1.55;
  letter-spacing:-0.01em;
}
a{color:inherit; text-decoration:none;}
img{max-width:100%; display:block;}
.wrap{max-width:1040px; margin:0 auto; padding:0 24px;}
.eyebrow{font-size:13px; font-weight:600; letter-spacing:0.04em; text-transform:uppercase; color:var(--gray);}
.pill{
  display:inline-flex; align-items:center; gap:6px;
  padding:12px 22px; border-radius:999px; border:1.5px solid var(--ink);
  font-weight:700; font-size:14px; background:var(--ink); color:var(--paper);
  white-space:nowrap; transition:opacity .15s ease;
}
.pill:hover{opacity:.78;}
.pill.outline{ background:transparent; color:var(--ink); }
.pill.on-dark{ background:var(--paper); color:var(--ink); border-color:var(--ink); }

/* NAV */
.nav{
  position:sticky; top:0; z-index:20; background:var(--paper);
  border-bottom:1.5px solid var(--ink);
}
.nav .wrap{display:flex; align-items:center; justify-content:space-between; padding-top:18px; padding-bottom:18px;}
.brand{font-weight:700; font-size:19px; letter-spacing:-0.02em; display:flex; align-items:center; gap:8px;}
.brand .dot{width:9px; height:9px; border-radius:50%; background:var(--lime); border:1.5px solid var(--ink); display:inline-block;}
.navlinks{display:flex; align-items:center; gap:10px;}
.back-home{font-weight:600; font-size:14px; color:var(--gray); display:flex; align-items:center; gap:6px;}
.back-home:hover{color:var(--ink);}

/* HERO */
.hero{ padding:72px 0 56px; border-bottom:1.5px solid var(--ink); }
.hero h1{ font-size:44px; line-height:1.18; font-weight:700; letter-spacing:-0.03em; margin:14px 0 18px; }
.hero p{ font-size:17px; color:var(--gray); max-width:520px; margin:0 0 28px; }

/* COLOR BLOCK SECTIONS */
.block{ border-bottom:1.5px solid var(--ink); padding:56px 0; }
.block .wrap{ position:relative; }
.block-tag{
  display:inline-block; padding:6px 14px; border-radius:999px; border:1.5px solid var(--ink);
  font-size:13px; font-weight:700; background:var(--paper); margin-bottom:20px;
}
.block h2{ font-size:30px; font-weight:700; letter-spacing:-0.02em; margin:0 0 22px; }

/* SUMMARY LIST (3-line) */
.summary-list{ list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:14px; max-width:680px; }
.summary-list li{ font-size:18px; font-weight:600; line-height:1.5; padding-left:30px; position:relative; }
.summary-list li::before{
  content:attr(data-n); position:absolute; left:0; top:0;
  width:22px; height:22px; border-radius:50%; background:var(--ink); color:var(--paper);
  font-size:12px; font-weight:700; display:flex; align-items:center; justify-content:center;
}

/* ARCHIVE GRID */
.archive-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:18px; margin-top:8px; }
.archive-card{
  background:var(--paper); border:1.5px solid var(--ink); border-radius:16px; overflow:hidden;
  display:flex; flex-direction:column; transition:transform .15s ease;
}
.archive-card:hover{ transform:translateY(-3px); }
.archive-thumb{ aspect-ratio:16/9; width:100%; }
.archive-body{ padding:16px 16px 18px; }
.archive-date{ font-size:12px; font-weight:700; color:var(--gray); margin-bottom:6px; }
.archive-title{ font-size:15px; font-weight:700; line-height:1.4; }
.archive-badge{
  display:inline-block; margin-top:10px; font-size:11px; font-weight:700; padding:4px 10px;
  border-radius:999px; border:1.5px solid var(--ink);
}

/* ISSUE BANNER */
.banner{
  border-radius:20px; border:1.5px solid var(--ink); padding:36px 32px; margin-bottom:28px;
  display:flex; align-items:center; justify-content:space-between; gap:24px; overflow:hidden; position:relative;
}
.banner .banner-text{ position:relative; z-index:2; }
.banner .banner-eyebrow{ font-size:13px; font-weight:700; opacity:.7; margin-bottom:8px; }
.banner h3{ font-size:26px; font-weight:700; letter-spacing:-0.02em; margin:0; }
.banner-icon{ width:96px; height:96px; flex:none; background:var(--paper); border-radius:50%; border:1.5px solid var(--ink); display:flex; align-items:center; justify-content:center; position:relative; z-index:2;}
.banner-icon svg{ width:52px; height:52px; }
.banner-deco{ position:absolute; inset:0; opacity:.5; }

/* CASE CARDS */
.case, .meme-card{
  display:flex; align-items:flex-start; gap:16px; padding:20px; border:1.5px solid var(--ink);
  border-radius:16px; margin-bottom:14px; background:var(--paper); position:relative;
  transition:transform .15s ease, box-shadow .15s ease;
}
.case:hover, .meme-card:hover{ transform:translateX(2px); box-shadow:4px 4px 0 var(--ink); }
.case-icon{
  width:56px; height:56px; flex:none; border-radius:12px; border:1.5px solid var(--ink);
  display:flex; align-items:center; justify-content:center;
}
.case-icon svg{ width:30px; height:30px; }
.case-body{ flex:1; min-width:0; }
.case-title{ font-size:17px; font-weight:700; margin:0 0 4px; letter-spacing:-0.01em; }
.case-meta{ font-size:12px; font-weight:600; color:var(--gray); margin-bottom:8px; }
.case-meta b{ color:var(--ink); }
.case-row{ font-size:14.5px; line-height:1.6; margin:0 0 4px; }
.case-row b{ font-weight:700; }
.case-insight{
  margin-top:10px; padding:10px 14px; border-radius:10px; background:var(--cream);
  font-size:14px; font-weight:600; border-left:3px solid var(--ink);
}
.case-link{
  flex:none; align-self:center; font-size:13px; font-weight:700; color:var(--ink);
  display:flex; align-items:center; gap:4px; white-space:nowrap;
}
.case-source{ font-size:11.5px; color:var(--gray); font-weight:600; margin-top:8px; }

/* FOOTER */
.foot{ padding:48px 0 64px; }
.foot .wrap{ display:flex; flex-direction:column; gap:18px; }
.foot-top{ display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px; }
.foot-brand{ font-weight:700; font-size:18px; }
.foot-copy{ font-size:12.5px; color:var(--gray); }

@media (max-width: 760px){
  .archive-grid{ grid-template-columns:repeat(2,1fr); }
  .hero h1{ font-size:32px; }
  .banner{ flex-direction:column; align-items:flex-start; }
  .banner-icon{ width:72px; height:72px; }
  .banner-icon svg{ width:38px; height:38px; }
  .case, .meme-card{ flex-direction:column; }
  .case-link{ align-self:flex-start; }
}
@media (max-width: 480px){
  .archive-grid{ grid-template-columns:1fr 1fr; }
}
"""

def icon(name, bg):
    return f'<div class="case-icon" style="background:{bg}">{ICONS[name]}</div>'

def banner_icon(name):
    return f'<div class="banner-icon">{ICONS[name]}</div>'

def block_deco_svg(seed, color):
    """Simple abstract pastel deco shapes for banner backgrounds."""
    import random
    random.seed(seed)
    shapes = []
    for i in range(4):
        cx = random.randint(10, 90)
        cy = random.randint(10, 90)
        r = random.randint(20, 70)
        shapes.append(f'<circle cx="{cx}%" cy="{cy}%" r="{r}" fill="{color}" opacity="0.12"/>')
    return f'<svg class="banner-deco" viewBox="0 0 300 200" preserveAspectRatio="none">{"".join(shapes)}</svg>'
