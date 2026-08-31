# -*- coding: utf-8 -*-
"""PLMK 트렌드 — 고정 호스팅용 정적 사이트.

/index.html              홈 (주소 고정, 매일 덮어씀)
/YYYY-MM-DD/index.html   개별 호 (매일 새 경로 추가, 기존 호는 그대로)
/assets/pretendard.css   Pretendard 400/600/700 base64 (한 번 받아 캐시)
/archive.json            발행 레지스트리 (다음 빌드가 읽어 아카이브를 이어감)
"""
import sys, os, json, html, shutil, importlib.util

sys.path.insert(0, "/home/claude/export1")
from build_common import BASE_CSS, PALETTE, block_deco_svg
from icons import ICONS

SITE = "/home/claude/plmk/site"
REG = "/home/claude/plmk/archive.json"
esc = lambda s: html.escape(str(s), quote=False)
attr = lambda s: html.escape(str(s), quote=True)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


C1 = load("c1", "/home/claude/plmk/content_001.py")
C2 = load("c2", "/home/claude/plmk/content.py")
C3 = load("c3", "/home/claude/export1/content.py")

ICON_MAP = {
    "bell": "megaphone", "bolt": "target", "briefcase": "briefcase", "capsule": "capsule",
    "chart": "target", "chat": "speech", "clock": "clock", "clown": "clown",
    "coffee": "coffee", "cup": "coffee", "dice": "target", "factory": "factory",
    "gavel": "briefcase", "globe": "search", "home": "home", "mic": "speech",
    "music": "music", "phone": "phone", "radio": "music", "recipe": "heart",
    "robot": "robot", "shield": "briefcase", "spark": "target", "speech": "speech",
    "store": "home", "target": "target", "tv": "tv",
}
SECTION = [
    ("①", "브랜드·캠페인", "BRAND & CAMPAIGN", "coral", "#FFE3D8", "music"),
    ("②", "SNS·밈", "SNS & MEME", "pink", "#FFDCEC", "clown"),
    ("③", "업계·인사이트", "INDUSTRY & INSIGHT", "mint", "#D6F7E6", "robot"),
]


def normalize(mod):
    if hasattr(mod, "SUMMARY_3LINES"):
        return dict(no=int(mod.ISSUE_NO), date=mod.ISSUE_DATE.replace(".", "-"),
                    date_dot=mod.ISSUE_DATE, date_long=mod.ISSUE_DATE_LONG,
                    summary=mod.SUMMARY_3LINES, posts=list(mod.POSTS))
    posts = []
    for i, p in enumerate(mod.POSTS):
        num, title, eyebrow, color, bg, bicon = SECTION[i]
        cases = [dict(icon=ICON_MAP.get(c["icon"], "target"), bg=bg, title=c["brand"],
                      meta=c["headline"], rows=[("What", c["body"])], insight=None,
                      source=c["meta"].replace("출처 · ", "").strip(), url=c["url"])
                 for c in p["cases"]]
        posts.append(dict(num=num, title=title, banner_title=p["title"],
                          banner_eyebrow=eyebrow, color=color, icon=bicon,
                          intro=p["lead"], cases=cases))
    return dict(no=int(mod.ISSUE_NO), date=mod.ISSUE_DATE,
                date_dot=mod.ISSUE_DATE.replace("-", "."), date_long=mod.ISSUE_DATE_KR,
                summary=mod.SUMMARY3, posts=posts)


SUMMARY_TABLE = {
    1: ("이미 있던 행동에 브랜드가 올라탄 주",
        "저가 커피 4사 콜라보·랜덤·이슈 탑승 · 백억커피 X 조회 497만",
        "8월 밈 5종(삐바삐·연락 없네 잘 살아) · 브랜드 15곳 탑승",
        "IAB, AI 표시 기준을 '오해 가능성'으로 개정 · 마케터 75% 사용, 13%만 성과"),
    2: ("유행을 제도화하고, 장치로 승부한 주",
        "LUX #LUXMyWill 등 트렌드를 공식 문서·제품으로 만든 6건",
        "인급동 릴스 5선 · 구름 타임랩스 20.6M, 협찬 표기 릴스도 상위",
        "쇼피파이 AI 유입 197%↑, 오가닉 검색도 12%↑ · PDP 시작 세션 50%"),
    3: ("일상을 세심하게 포착한 콘텐츠가 이긴 주",
        "인천시 LOST&FOUND 4,765만 · KCC 스위첸 2,731만",
        "8월 타임라인 지배한 밈 총정리 5종",
        "AEO 실전 매뉴얼 · 틱톡 마이크로드라마 광고 · 개인 맞춤 건기식"),
}

ISSUES = sorted([normalize(m) for m in (C1, C2, C3)], key=lambda i: i["date"], reverse=True)
LATEST = ISSUES[0]
path_of = lambda iss: "/%s/" % iss["date"]

# ---------- 발행 레지스트리 ----------
json.dump([{"no": i["no"], "date": i["date"], "date_long": i["date_long"],
            "path": path_of(i), "headline": i["posts"][0]["banner_title"]} for i in ISSUES],
          open(REG, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---------- 조각 ----------
HEAD = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><link rel="stylesheet" href="/assets/pretendard.css"><style>%s</style></head><body>"""

NAV = """<nav class="nav"><div class="wrap">%s<div class="brand"><span class="dot"></span>PLMK 트렌드</div>
<a class="pill outline" href="/">전체 호 보기</a></div></nav>"""

FOOT = """<footer class="foot"><div class="wrap"><div class="foot-top">
<div class="foot-brand">PLMK 트렌드</div><a class="pill" href="/">← 홈으로</a></div>
<div class="foot-copy">매일 아침 자동 발행되는 마케팅·광고 트렌드 브리핑</div></div></footer></body></html>"""


def render_case(c):
    rows = "".join('<p class="case-row"><b>%s</b> · %s</p>' % (esc(l), esc(t)) for l, t in c["rows"])
    ins = '<div class="case-insight">💡 %s</div>' % esc(c["insight"]) if c.get("insight") else ""
    return ('<a class="case" href="%s" target="_blank" rel="noopener">'
            '<div class="case-icon" style="background:%s">%s</div><div class="case-body">'
            '<p class="case-title">%s</p><p class="case-meta">%s</p>%s%s'
            '<p class="case-source">출처 · %s</p></div>'
            '<span class="case-link">원문 보기 →</span></a>'
            % (attr(c["url"]), c["bg"], ICONS[c["icon"]], esc(c["title"]),
               esc(c["meta"]), rows, ins, esc(c["source"])))


def render_post(p, seed):
    color = PALETTE[p["color"]]
    return ('<section class="block" style="background:%s22;"><div class="wrap">'
            '<span class="block-tag">%s %s</span><div class="banner" style="background:%s;">%s'
            '<div class="banner-text"><div class="banner-eyebrow">%s</div><h3>%s</h3></div>'
            '<div class="banner-icon">%s</div></div>'
            '<p style="font-size:15.5px;color:#333;max-width:660px;margin:0 0 24px;line-height:1.7;">%s</p>'
            '%s</div></section>'
            % (color, esc(p["num"]), esc(p["title"]), color, block_deco_svg(seed, "#111111"),
               esc(p["banner_eyebrow"]), esc(p["banner_title"]), ICONS[p["icon"]],
               esc(p["intro"]), "".join(render_case(c) for c in p["cases"])))


def write(rel, doc):
    full = os.path.join(SITE, rel.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(doc)


# ---------- 개별 호 ----------
for iss in ISSUES:
    summary = "".join('<li data-n="%d">%s</li>' % (i + 1, esc(s)) for i, s in enumerate(iss["summary"]))
    doc = (HEAD % ("PLMK 트렌드 — 제%d호" % iss["no"], BASE_CSS + """
.issue-header{padding:40px 0 44px;border-bottom:1.5px solid var(--ink);}
.issue-badge{display:inline-flex;align-items:center;gap:8px;padding:7px 16px;border-radius:999px;
 border:1.5px solid var(--ink);font-size:13px;font-weight:700;margin-bottom:18px;}
.issue-badge .dot{width:8px;height:8px;border-radius:50%;background:var(--lime);border:1.5px solid var(--ink);}
.issue-header h1{font-size:34px;font-weight:700;letter-spacing:-.02em;margin:0 0 22px;line-height:1.3;}""")
           + NAV % '<a class="back-home" href="/">← 홈</a>'
           + '<header class="issue-header"><div class="wrap">'
             '<div class="issue-badge"><span class="dot"></span>제%d호 · %s</div>'
             '<h1>오늘 마케터가 알아야 할 3가지,<br>PLMK 트렌드가 정리했어요.</h1>'
             '<ul class="summary-list">%s</ul></div></header>' % (iss["no"], esc(iss["date_long"]), summary)
           + "".join(render_post(p, iss["no"] * 10 + i) for i, p in enumerate(iss["posts"]))
           + FOOT)
    write(path_of(iss) + "index.html", doc)

# ---------- 홈 ----------
cards = "".join(
    '<a class="archive-card" href="%s"><div class="archive-thumb" style="background:%s;display:flex;'
    'align-items:center;justify-content:center;"><div style="width:44px;height:44px;">%s</div></div>'
    '<div class="archive-body"><div class="archive-date">%s</div>'
    '<div class="archive-title">%s</div><span class="archive-badge">제%d호</span></div></a>'
    % (path_of(i), PALETTE[["coral", "mint", "lilac"][n % 3]],
       ICONS[["music", "clown", "coffee"][n % 3]], esc(i["date_dot"]),
       esc(i["posts"][0]["banner_title"]), i["no"])
    for n, i in enumerate(ISSUES))

home_summary = "".join('<li data-n="%d">%s</li>' % (i + 1, esc(s)) for i, s in enumerate(LATEST["summary"]))
home = (HEAD % ("PLMK 트렌드", BASE_CSS + """
.hero-tagbar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px;}
.cmp{width:100%;border-collapse:collapse;background:var(--paper);border:1.5px solid var(--ink);border-radius:16px;overflow:hidden;}
.cmp th,.cmp td{border-bottom:1px solid var(--hair);padding:14px 16px;text-align:left;vertical-align:top;font-size:14px;line-height:1.6;}
.cmp thead th{background:var(--ink);color:var(--paper);font-size:12.5px;font-weight:700;letter-spacing:.03em;border-bottom:0;}
.cmp tbody tr:last-child td{border-bottom:0;}
.cmp td.no{font-weight:700;white-space:nowrap;}
.cmp td.no small{display:block;font-weight:600;color:var(--gray);font-size:12px;margin-top:3px;}
.cmp td.key{font-weight:600;}
.cmp a{text-decoration:underline;text-underline-offset:3px;}
.cmp-wrap{overflow-x:auto;}
.cmp-wrap table{min-width:760px;}
.hero-tag{font-size:12.5px;font-weight:700;padding:5px 12px;border-radius:999px;border:1.5px solid var(--ink);}""")
        + NAV % '' 
        + '<section class="hero"><div class="wrap"><div class="hero-tagbar">'
          '<span class="hero-tag">매일 아침 발행</span><span class="hero-tag">브랜드·캠페인</span>'
          '<span class="hero-tag">SNS·밈</span><span class="hero-tag">업계·인사이트</span></div>'
          '<h1>마케팅·광고 트렌드,<br>매일 아침 3분이면 끝.</h1>'
          '<p>어제오늘 화제가 된 브랜드 캠페인과 밈, 업계 인사이트를 매일 아침 자동으로 크롤링해 정리해요. '
          '출처는 전부 원문 링크로 확인할 수 있어요.</p>'
          '<a class="pill" href="%s">최신호 읽기 →</a></div></section>' % path_of(LATEST)
        + '<section class="block" style="background:var(--lime);"><div class="wrap">'
          '<span class="block-tag" style="background:var(--paper);">제%d호 · %s</span>'
          '<h2>오늘의 3줄 요약</h2><ul class="summary-list">%s</ul>'
          '<div style="margin-top:28px;"><a class="pill" href="%s">제%d호 전체 보기 →</a></div>'
          '</div></section>' % (LATEST["no"], esc(LATEST["date_dot"]), home_summary,
                                path_of(LATEST), LATEST["no"])
        + '<section class="block" style="background:var(--lilac);"><div class="wrap">'
          '<span class="block-tag" style="background:var(--paper);">ARCHIVE</span>'
          '<h2>지난 조간</h2><div class="archive-grid">%s</div></div></section>' % cards
        + '<section class="block"><div class="wrap">'
          '<span class="block-tag">SUMMARY</span><h2>호별 핵심 정리</h2>'
          '<p style="font-size:15px;color:#333;margin:0 0 22px;">발행된 호를 한눈에 비교할 수 있게 정리했어요.</p>'
          '<div class="cmp-wrap"><table class="cmp"><thead><tr>'
          '<th>호</th><th>이번 호 한 줄</th><th>① 브랜드·캠페인</th><th>② SNS·밈</th><th>③ 업계·인사이트</th>'
          '</tr></thead><tbody>%s</tbody></table></div></div></section>' % "".join(
            '<tr><td class="no"><a href="%s">제%d호</a><small>%s</small><small>사례 %d건</small></td>'
            '<td class="key">%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            % (path_of(i), i["no"], esc(i["date_dot"]),
               sum(len(p["cases"]) for p in i["posts"]),
               esc(SUMMARY_TABLE[i["no"]][0]), esc(SUMMARY_TABLE[i["no"]][1]),
               esc(SUMMARY_TABLE[i["no"]][2]), esc(SUMMARY_TABLE[i["no"]][3]))
            for i in ISSUES)
        + FOOT)
write("/index.html", home)

# ---------- 폰트 ----------
fonts = open("/home/claude/plmk/fonts.css", encoding="utf-8").read()
write("/assets/pretendard.css", fonts)
shutil.copy(REG, os.path.join(SITE, "archive.json"))

for root, _, files in os.walk(SITE):
    for f in sorted(files):
        p = os.path.join(root, f)
        print(p.replace(SITE, "") or "/", round(os.path.getsize(p) / 1024), "KB")
