# -*- coding: utf-8 -*-
ISSUE_NO = 3
ISSUE_DATE = "2026.08.31"
ISSUE_DATE_LONG = "2026년 8월 31일 월요일"
ISSUE_DATE_ISO = "2026-08-31"

SUMMARY_3LINES = [
    "인천광역시가 축제 분실물로 만든 뮤직비디오가 인스타그램에서 4,765만 조회를 넘겼어요.",
    "‘삐에로’ ‘면접 포기’ 밈이 타임라인을 휩쓸었고, 스크럽대디부터 GS건설까지 이 위에 올라탔어요.",
    "AI가 브랜드를 직접 추천하게 만드는 ‘AEO’ 전략과 틱톡의 신규 마이크로드라마 광고가 다음 격전지로 떠올랐어요.",
]

GOGUMA_MEME = "https://gogumafarm.kr/%eb%8c%80%eb%b0%95%ec%82%90-%ec%82%90%eb%b0%94%ec%82%90-%eb%b0%88%ec%9e%98%ec%95%8c%ec%82%90-%eb%a7%8c%eb%93%a4%ec%96%b4-%ec%a3%bc%eb%8a%94-2026%eb%85%84-8%ec%9b%94-%ec%b5%9c%ec%8b%a0-%eb%b0%88/"
GOGUMA_COFFEE = "https://gogumafarm.kr/%ec%9d%b4%ec%a0%9c-%ea%b0%80%ec%84%b1%eb%b9%84%eb%8a%94-%ea%b8%b0%eb%b3%b8-%ec%b9%98%ec%97%b4%ed%95%9c-%ea%b2%bd%ec%9f%81%ec%97%90%ec%84%9c-%ec%82%b4%ec%95%84%eb%82%a8%ea%b8%b0-%ec%9c%84%ed%95%9c/"
GOGUMA_MV = "https://gogumafarm.kr/4700%eb%a7%8c-%ec%a1%b0%ed%9a%8c%ec%88%98%eb%a5%bc-%eb%8f%8c%ed%8c%8c%ed%95%9c-%eb%b6%84%ec%8b%a4%eb%ac%bc-%eb%ae%a4%ec%a7%81%eb%b9%84%eb%94%94%ec%98%a4-%ec%9d%bc%ec%83%81%ec%9d%84-%ec%a1%b0/"
GOGUMA_AEO = "https://gogumafarm.kr/ai%ea%b0%80-%ec%9a%b0%eb%a6%ac-%eb%b8%8c%eb%9e%9c%eb%93%9c%eb%a5%bc-%ec%b6%94%ec%b2%9c%ed%95%98%ea%b2%8c-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b2%95-%eb%a7%88%ec%bc%80%ed%84%b0%eb%a5%bc-%ec%9c%84%ed%95%9c/"
GOGUMA_FASTFOOD = "https://gogumafarm.kr/%eb%a7%a5%eb%8f%84%eb%82%a0%eb%93%9c%c2%b7%eb%b2%84%ea%b1%b0%ed%82%b9%c2%b7%eb%a1%af%eb%8d%b0%eb%a6%ac%ec%95%84%eb%a1%9c-%eb%b3%b4%eb%8a%94-%ed%8c%a8%ec%8a%a4%ed%8a%b8%ed%91%b8%eb%93%9c-3%ec%82%ac/"
MADTIMES_HANSOL = "https://madtimes.co.kr/news/articleView.html?idxno=28354"
IBOSS_MEZZO = "https://www.i-boss.co.kr/ab-3208-1795"
MOBIINSIDE_PILLY = "https://www.mobiinside.co.kr/2026/08/25/personalized-health-functional-food/"

# ---------------- ① 브랜드·캠페인 ----------------
BRAND_POST = {
    "key": "brand",
    "num": "①",
    "title": "브랜드·캠페인",
    "banner_title": "이번 주, 브랜드가 이야기하는 법",
    "banner_eyebrow": "BRAND & CAMPAIGN",
    "color": "coral",
    "icon": "music",
    "intro": "거창한 이벤트보다 ‘일상을 얼마나 세심하게 포착했는가’가 승부처였어요. 분실물, 집안일, B2B 사업까지 — 원래 있던 이야기를 다르게 보여준 4개 캠페인을 모았어요.",
    "cases": [
        {
            "icon": "music", "bg": "#FFE3D8",
            "title": "인천광역시 × 극동아시아타이거즈 — “LOST&FOUND”",
            "meta": "유튜브·인스타그램 · 조회수 약 4,765만 회",
            "rows": [
                ("What", "2026 인천펜타포트 락페스티벌 현장의 실제 분실물을 소재로 만든 뮤직비디오예요."),
                ("How", "“왜 가져온 거야 / 틀니 태엽 피규어”처럼 위트 있는 가사로 분실물을 하나씩 나열하며 노래로 엮었어요."),
            ],
            "insight": "새 이야기를 지어내지 않고 현장의 사소한 해프닝을 그대로 콘텐츠화했더니, 축제에 없던 사람까지 웃게 만들며 도시 이미지까지 끌어올렸어요.",
            "source": "고구마팜", "url": GOGUMA_MV,
        },
        {
            "icon": "home", "bg": "#FFE3D8",
            "title": "KCC건설 스위첸 — “위대한 집안일”",
            "meta": "유튜브 · 공개 2주 만에 조회수 2,731만 회",
            "rows": [
                ("What", "“저절로 돌아가는 일상은 없습니다”라는 메시지로 집안일의 소소한 순간을 감성적으로 담은 영상이에요."),
                ("How", "특별한 이벤트가 아니라 매일 반복되는 가사노동 자체를 주인공으로 세웠어요."),
            ],
            "insight": "당연하게 여겨지던 수고로움을 새로운 시선으로 재조명하는 것만으로도 시청자의 깊은 감정 반응을 끌어냈어요.",
            "source": "고구마팜", "url": GOGUMA_MV,
        },
        {
            "icon": "factory", "bg": "#FFE3D8",
            "title": "대홍기획 × 한솔그룹 — “당연, 한솔이 하고 있습니다”",
            "meta": "유튜브 · 공개 1개월 만에 누적 조회수 1,100만 회",
            "rows": [
                ("What", "전기차 충전 속도, 물류비 인상 같은 일상 불편함을 질문으로 던지고 “당연한 소리 하고 있어! 당연, 한솔이 하고 있습니다!”로 답하는 기업 캠페인이에요."),
                ("How", "계열사 임직원이 직접 출연해 친환경 종이부터 이차전지 음극재, AI·물류 플랫폼까지 다양한 사업을 소개했어요."),
            ],
            "insight": "그룹명 ‘한솔’과 ‘당연한 소리’를 언어유희로 엮어, 낯선 B2B 사업 영역을 생활 밀착형 스토리로 쉽게 풀어냈어요.",
            "source": "매드타임스", "url": MADTIMES_HANSOL,
        },
        {
            "icon": "coffee", "bg": "#FFE3D8",
            "title": "컴포즈커피 — “매샷추”",
            "meta": "인스타그램 릴스 · 조회수 75만 회",
            "rows": [
                ("What", "알바생이 낸 메뉴 아이디어를 실제 정식 메뉴로 출시한 사례예요."),
                ("How", "출시 소식을 알린 릴스가 큰 반응을 얻으며 자연스럽게 확산됐어요."),
            ],
            "insight": "현장 직원발 아이디어를 빠르게 포착해 제품화하는 속도감이, 화제성과 브랜드 호감도를 동시에 만들었어요.",
            "source": "고구마팜", "url": GOGUMA_COFFEE,
        },
    ],
}

# ---------------- ② SNS·밈 ----------------
MEME_POST = {
    "key": "meme",
    "num": "②",
    "title": "SNS·밈",
    "banner_title": "지금 타임라인 뒤덮은 밈 총정리",
    "banner_eyebrow": "SNS & MEME",
    "color": "pink",
    "icon": "clown",
    "intro": "8월 커뮤니티·SNS 타임라인을 지배한 밈 5개예요. 브랜드들이 어떤 포맷에, 어떻게 올라탔는지까지 같이 정리했어요.",
    "cases": [
        {
            "icon": "target", "bg": "#FFDCEC",
            "title": "면접 포기 밈",
            "meta": "커뮤니티 · 인스타그램",
            "rows": [
                ("What", "“죄송합니다, 면접 포기하겠습니다”와 “면접을 하겠습니다”를 오가며, 중요한 결정 앞에서의 내적 갈등을 표현하는 밈이에요."),
                ("Who", "스크럽대디, 극지연구소가 이 포맷으로 콘텐츠를 만들었어요."),
            ],
            "insight": "결정 장애라는 보편적 감정을 짧은 대사 반복으로 표현해, 브랜드가 진지한 소재도 가볍게 얹기 좋은 포맷이에요.",
            "source": "고구마팜", "url": GOGUMA_MEME,
        },
        {
            "icon": "clown", "bg": "#FFDCEC",
            "title": "삐에로 밈 (선배삐·개대박삐·삐바삐)",
            "meta": "커뮤니티 · 인스타그램 · X",
            "rows": [
                ("What", "능력 있는 방송인 중 ‘삐에로 출신(삐출)’이 유독 많다는 사실이 화제가 되며 생긴 호칭 밈이에요."),
                ("Who", "이용주, 이은지, 허경환, 윤경호 등이 언급되며 확산됐어요."),
            ],
            "insight": "특정 이력을 밈화된 애칭으로 재해석하는 흐름이라, 인물 콜라보 콘텐츠에 붙이면 자연스러운 반응을 얻기 좋아요.",
            "source": "고구마팜", "url": GOGUMA_MEME,
        },
        {
            "icon": "speech", "bg": "#FFDCEC",
            "title": "무례하지 않게 말해주세요 밈",
            "meta": "인스타그램 릴스",
            "rows": [
                ("What", "“‘까맣다’를 무례하지 않게 말해주세요”처럼, 신체 특징이나 평가를 완곡하게 돌려 말하도록 요청하는 형식이에요."),
                ("Who", "리챔, 뽀로로가 이 포맷을 활용했어요."),
            ],
            "insight": "정답이 정해져 있지 않은 ‘드립 대결’ 구조라 댓글 참여를 자연스럽게 유도할 수 있는 포맷이에요.",
            "source": "고구마팜", "url": GOGUMA_MEME,
        },
        {
            "icon": "briefcase", "bg": "#FFDCEC",
            "title": "일하기 전후 밈",
            "meta": "인스타그램 릴스",
            "rows": [
                ("What", "업무 시작 전의 말끔한 모습과 종료 후 지친 모습을 극명하게 대조하는 콘텐츠예요."),
                ("Who", "기아(퍼펭), 틴더가 이 밈을 활용했어요."),
            ],
            "insight": "비포·애프터 구조는 직군을 가리지 않고 누구나 공감할 수 있어서, 채용·브랜딩 콘텐츠 어디든 붙이기 쉬워요.",
            "source": "고구마팜", "url": GOGUMA_MEME,
        },
        {
            "icon": "phone", "bg": "#FFDCEC",
            "title": "연락 없네 잘 살아 밈",
            "meta": "블라인드 · 인스타그램 · X",
            "rows": [
                ("What", "“37분간 답장 없다”는 블라인드 게시글에서 출발해, 연락을 기다리는 불안감을 과장해서 표현하는 밈이에요."),
                ("Who", "GS건설, 에이블리가 브랜드 콘텐츠에 접목했어요."),
            ],
            "insight": "사소한 일상의 불안을 과장된 유머로 승화한 케이스라, 고객 응대·알림 콘텐츠에 붙이면 공감을 사기 좋아요.",
            "source": "고구마팜", "url": GOGUMA_MEME,
        },
    ],
}

# ---------------- ③ 업계·인사이트 ----------------
INSIGHT_POST = {
    "key": "insight",
    "num": "③",
    "title": "업계·인사이트",
    "banner_title": "마케터가 챙겨야 할 이번 주 인사이트",
    "banner_eyebrow": "INDUSTRY & INSIGHT",
    "color": "mint",
    "icon": "robot",
    "intro": "AI가 검색을 대체하기 시작하면서 마케터의 할 일도 바뀌고 있어요. AI 최적화 전략부터 숏폼 플랫폼의 신무기, 맞춤형 커머스 신호까지 3가지를 짚었어요.",
    "cases": [
        {
            "icon": "robot", "bg": "#D6F7E6",
            "title": "AEO(AI Engine Optimization) 실전 매뉴얼",
            "meta": "가이드 · AI 검색 최적화",
            "rows": [
                ("What", "ChatGPT·Gemini 같은 생성형 AI가 브랜드를 직접 추천하도록 만드는 최적화 전략이에요."),
                ("How", "브랜드 명칭을 하나의 ‘엔티티’로 통일하고, 홈페이지엔 시맨틱 태그·JSON-LD 구조화 데이터를, 블로그엔 첫 문단에 정의형 문장을 배치하는 3단계로 접근해요."),
            ],
            "insight": "통일된 명칭과 구체적인 맥락이 웹에 꾸준히 쌓여야, AI가 브랜드를 ‘확실한 정답’으로 인식한다는 점이 핵심이에요.",
            "source": "고구마팜", "url": GOGUMA_AEO,
        },
        {
            "icon": "tv", "bg": "#D6F7E6",
            "title": "CJ 메조미디어 2026년 8월 미디어 리포트",
            "meta": "미디어 이슈 · 틱톡 · 인스타그램",
            "rows": [
                ("What", "틱톡이 브랜드 전용 ‘마이크로드라마’ 광고 상품을 새로 출시했고, 인스타그램은 TV 시청용 롱폼 영상 포맷을 테스트 중이에요."),
                ("Why", "두 플랫폼 모두 체류시간을 늘리기 위해 유튜브·넷플릭스 영역까지 넘보기 시작했다는 신호예요."),
            ],
            "insight": "숏폼 강자들이 롱폼·시리즈 콘텐츠로 영역을 넓히는 중이라, 브랜드 콘텐츠도 ‘한 편’이 아닌 ‘시리즈’ 단위 기획이 유리해질 수 있어요.",
            "source": "아이보스", "url": IBOSS_MEZZO,
        },
        {
            "icon": "capsule", "bg": "#D6F7E6",
            "title": "개인 맞춤형 건강기능식품, ‘필리’가 보여준 신호",
            "meta": "커머스 · 헬스케어",
            "rows": [
                ("What", "문진 기반으로 영양제 조합을 추천하는 구독 서비스 ‘필리’가, 문진 한 번당 27만 건의 추천을 만들어냈어요."),
                ("Why", "6조 원대에서 성장이 멈춘(2025년 성장률 0.2%) 건기식 시장에서, 이제 성분·할인이 아니라 ‘왜 나에게 필요한지 납득시키는 경험’이 핵심 상품이 되고 있어요."),
            ],
            "insight": "핵심 KPI도 전환율에서 추천 수락률·30일 섭취 지속률로 옮겨가는 중이에요. ‘한 번 팔기’보다 ‘계속 쓰게 만들기’가 커머스 마케팅의 다음 과제예요.",
            "source": "모비인사이드", "url": MOBIINSIDE_PILLY,
        },
    ],
}

POSTS = [BRAND_POST, MEME_POST, INSIGHT_POST]
