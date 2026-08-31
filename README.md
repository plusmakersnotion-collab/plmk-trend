# PLMK 트렌드 — 정적 사이트

## 구조
```
/index.html              홈 (주소 고정, 매일 덮어씀)
/YYYY-MM-DD/index.html   개별 호 (매일 새 경로 추가, 기존 호는 그대로)
/assets/pretendard.css   Pretendard 400/600/700 base64
/archive.json            발행 레지스트리
```

## 배포 (둘 중 하나)

### Netlify — 가장 빠름, 계정도 필요 없음
1. https://app.netlify.com/drop 접속
2. 압축을 푼 폴더를 통째로 드래그
3. 몇 초 뒤 `https://<임의이름>.netlify.app` 주소가 나옴 (이게 고정 주소)
4. Site settings → Change site name 에서 원하는 이름으로 변경 가능

### GitHub Pages
1. 새 저장소 생성 후 이 폴더 내용을 루트에 올림
2. Settings → Pages → Deploy from a branch → `main` / `/ (root)`
3. `https://<계정>.github.io/<저장소>/` 로 열림

## 주소 규칙 (배포 후 고정)
- 홈: `https://<도메인>/`
- 제3호: `https://<도메인>/2026-08-31/`
- 제2호: `https://<도메인>/2026-08-30/`
- 제1호: `https://<도메인>/2026-08-29/`

## 매일 발행할 때
1. `content.py`의 ISSUE_DATE / ISSUE_NO / SUMMARY3 / POSTS 교체
2. `python3 build_static.py` 실행
3. `site/` 폴더를 다시 배포 (Netlify는 드래그, GitHub은 커밋)

홈은 덮어써지고 새 날짜 폴더가 추가됩니다. 지난 호 주소는 그대로 살아 있어서, 예전에 보낸 메일 링크도 계속 열립니다.
