# 사이트 생성기: python3 _build/gen.py  (공통 메뉴·푸터·다음으로 블록을 한 곳에서 관리)
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = 'https://sei-ban.github.io/memory-ender/'

PROJECTS = [
  dict(slug='memory-ender', tag='PROJECT 01 · 개인 프로젝트 · 웹 게임', name='메모리 엔더',
       hook='기억을 지우는 장의사가 장례를 거부한 망자를 쫓아, 마지막 장례를 치른다. 쌓아 온 감정을 마지막에 플레이어의 손으로 터뜨리는 구조.',
       thumb='assets/img/me-climax.jpg'),
  dict(slug='aftermath', tag='PROJECT 02 · 5인 팀 · Unity', name='Aftermath',
       hook='온라인 협동 타워 디펜스. 콘텐츠 기획을 맡아 기획서 → 데이터테이블 → 요청서로 구현까지 연결했다.',
       thumb=None, color='#2F5496'),
  dict(slug='echo', tag='PROJECT 03 · 개인 프로젝트 · Unity 6', name='잔향 (Echo)',
       hook='"10초 전의 내가 지금의 동료가 된다" — 수치로 정답 루트를 고정한 시간 루프 퍼즐 플랫포머.',
       thumb=None, color='#3A4F7A'),
  dict(slug='whoami', tag='PROJECT 04 · 5인 팀 · 비주얼 노벨', name='WHO AM I?',
       hook='감정 순서대로 여섯 방을 배치한 추리 비주얼 노벨.',
       thumb=None, color='#4A5D85'),
]

def head(title, depth, active):
    p = '../' * depth
    nav = [('index.html', '프로젝트', 'home'), ('about.html', '소개', 'about'), ('files/portfolio.pdf', 'PDF', 'pdf')]
    items = ''.join(f'<li><a href="{p}{h}" class="{"on" if k == active else ""}">{t}</a></li>' for h, t, k in nav)
    return f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="게임 기획자 김준현 포트폴리오">
<link rel="stylesheet" href="{p}assets/style.css?v=2"></head><body>
<nav class="top"><div class="wrap"><a class="brand" href="{p}index.html">김준현<span>게임 기획 포트폴리오</span></a><ul>{items}</ul></div></nav>
'''

def foot(depth):
    p = '../' * depth
    return f'''<footer><div class="wrap"><span>김준현 · rlawnsgus560@gmail.com · 010-9003-3750</span><span><a href="{p}files/portfolio.pdf">포트폴리오 PDF</a> · <a href="{GAME}">메모리 엔더 플레이</a></span></div></footer>
<script src="{p}assets/site.js?v=1"></script></body></html>'''

def card(pr, p):
    if pr['thumb']:
        th = f'<img src="{p}{pr["thumb"]}" alt="">'
    else:
        th = f'<div class="txt" style="background:{pr["color"]}">{pr["name"]}</div>'
    return f'''<a class="card" href="{p}projects/{pr["slug"]}.html"><div class="thumb">{th}</div><div class="c"><div class="tag">{pr["tag"]}</div><h4>{pr["name"]}</h4><p>{pr["hook"]}</p><div class="more">자세히 보기 →</div></div></a>'''

def next_block(slug):
    i = [x['slug'] for x in PROJECTS].index(slug)
    nx = PROJECTS[(i + 1) % len(PROJECTS)]
    return f'''<section class="next"><div class="wrap"><div class="grid">
<a class="box dark" href="../about.html"><small>ABOUT</small><b>이 기획을 한 사람이 궁금하다면 →</b><span>연출에서 게임 기획으로, 일하는 방식과 AI 활용 범위</span></a>
<a class="box" href="{nx["slug"]}.html"><small>NEXT PROJECT</small><b>{nx["name"]} →</b><span>{nx["hook"][:48]}…</span></a>
</div></div></section>'''

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(html)

# ---------------- 홈 ----------------
home = head('김준현 | 게임 기획 포트폴리오', 0, 'home') + f'''
<header class="hero"><div class="wrap">
<div class="k">GAME DESIGNER · 신입</div>
<h1>오래 남는 순간은 우연이 아니라 설계입니다.</h1>
<p class="lead">의도한 감정을 규칙·수치·레벨로 옮기고, AI와 함께 끝까지 구현하는 게임 기획자 김준현입니다.</p>
<div class="video" data-v="memory-ender"><div class="ph"><img src="assets/img/me-chase.jpg" alt=""><div><b style="font-size:20px;color:#fff">메모리 엔더 플레이 영상</b><br>영상 준비 중 — 아래 버튼으로 바로 플레이할 수 있습니다</div></div></div>
<div class="btns"><a class="btn p" href="{GAME}">▶ 메모리 엔더 바로 플레이 (약 5분)</a><a class="btn g" href="projects/memory-ender.html">기획 의도 보기</a></div>
</div></header>
<section class="s"><div class="wrap">
<h2 class="t">프로젝트</h2><p class="st">카드를 누르면 기획 의도와 설계, 플레이하며 고친 기록을 볼 수 있습니다.</p>
<div class="cards">{''.join(card(pr, '') for pr in PROJECTS)}</div>
</div></section>
<section class="next"><div class="wrap"><div class="grid">
<a class="box dark" href="about.html"><small>ABOUT</small><b>이 프로젝트들을 만든 사람 →</b><span>연출 전공에서 게임 기획으로 온 이야기와 일하는 방식</span></a>
<a class="box" href="files/portfolio.pdf"><small>PDF</small><b>포트폴리오 PDF로 보기 →</b><span>이력서와 프로젝트 기술서 6쪽</span></a>
</div></div></section>
''' + foot(0)
write('index.html', home)

# ---------------- 메모리 엔더 ----------------
me = head('메모리 엔더 | 김준현', 1, 'home') + f'''
<header class="phead"><div class="wrap"><div class="k">PROJECT 01 · 개인 프로젝트 · 웹 게임</div><h1>메모리 엔더 (Memory Ender)</h1><p>기억을 지우는 장의사가 장례를 거부한 망자를 쫓아, 마지막 장례를 치른다</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<div class="video" data-v="memory-ender"><div class="ph"><img src="../assets/img/me-funeral.jpg" alt=""><div><b style="font-size:20px;color:#fff">플레이 영상</b><br>영상 준비 중</div></div></div>
<div class="btns"><a class="btn n" href="{GAME}">▶ 바로 플레이 (설치 없이 브라우저, 약 5분)</a><a class="btn o" href="../files/memory-ender-gdd.pdf">게임 기획서 PDF</a><a class="btn o" href="https://github.com/sei-ban/memory-ender">저장소</a></div>
<p class="note" style="margin-top:8px">타이틀의 챕터 선택으로 원하는 구간을 바로 볼 수 있습니다. 클라이맥스는 '3. 장례'.</p>
<div class="stats"><div class="stat"><b>3구간</b><span>추리 → 추격 → 장례</span></div><div class="stat"><b>26</b><span>플레이 튜닝 항목</span></div><div class="stat"><b>약 5분</b><span>첫 에피소드</span></div><div class="stat"><b>1인 + AI</b><span>기획 · AI 협업 구현</span></div></div>
<table class="info"><tr><td class="h">기간</td><td>2026.04 제안서 → 09 컨셉 기획서 → 11 플레이 빌드</td></tr><tr><td class="h">역할</td><td>1인 · 기획 전반 + AI 협업 구현</td></tr><tr><td class="h">장르</td><td>스토리 중심 액션 어드벤처 (현재 빌드는 망자 한 명의 첫 에피소드, 이후 에피소드로 확장)</td></tr><tr><td class="h">사용 툴</td><td>Claude · Claude Code · Git · GitHub Pages</td></tr></table>
<div class="gallery"><img src="../assets/img/me-investigate.jpg" alt="추리"><img src="../assets/img/me-chase.jpg" alt="추격"><img src="../assets/img/me-funeral.jpg" alt="장례"><img src="../assets/img/me-climax.jpg" alt="클라이맥스"></div>
<p class="cap">추리 · 추격 · 장례 · 클라이맥스. 외부 이미지 없이 도형으로, 사운드는 브라우저에서 직접 합성했다.</p>

<h3>기획 의도</h3>
<p>빌드업을 쌓아 클라이맥스에서 터지는 한순간이 핵심 재미이며, 그 순간이 플레이를 계속하게 만든다. 중심 감정은 <b>연민과 갈등</b> — 지워야 한다는 걸 알지만 지우고 싶지 않은 마음을, 플레이어가 마지막에 <b>자기 손으로</b> 결정하게 만든다.</p>

<h3>목표 감정 곡선</h3>
<div class="fig"><img src="../assets/img/emotion_curve.png" alt="감정 곡선"></div>
<p class="cap">실측값이 아닌 설계 목표. 추격 끝에서 긴장감은 내려가고, 장례로 넘어가며 연민·갈등이 정점까지 올라간다.</p>

<h3>빌드업 구조 — 구간마다 쌓는 감정과 장치</h3>
<table><tr><th style="width:14%">구간</th><th style="width:20%">쌓이는 감정</th><th>기대 장치</th><th>방해 장치</th></tr>
<tr><td><b>추리</b></td><td>사명감 → 관계 추측</td><td>단서 3개로 관계가 조금씩 드러남 (결과 → 장소 → 동기)</td><td>신호로만 위치를 앎, 오답이면 다시 추리</td></tr>
<tr><td><b>추격</b></td><td>긴박감 + 연민의 시작</td><td>망자를 맞힐 때마다 기억 문장(주마등) 공개. 웃던 밤 → 싸우기 직전의 밤 순서</td><td>망자 회피 3종, 붕괴 지형, 잔해</td></tr>
<tr><td><b>장례</b></td><td>갈등</td><td>갑옷 파츠를 뜯을 때마다 둘의 기억 장면으로 전환</td><td>끌어당기는 저항감, 순서 고정</td></tr>
<tr><td><b>클라이맥스</b></td><td>연민과 갈등의 정점</td><td>데이터 망자를 누르는 동안 마지막 독백 진행</td><td>손을 떼면 멈춤 — 끝낼지는 플레이어가 쥐고 있음</td></tr></table>

<h3>핵심 플레이 — 추격 코어 루프</h3>
<div class="fig"><img src="../assets/img/core_loop.png" alt="코어 루프"></div>

<h3>클라이맥스 설계</h3>
<p>갑옷 5개를 모두 뜯어내면 데이터 망자만 남는다. 조등(장의사의 장례 도구)을 대고 <b>누르고 있는 9초</b> 동안 마지막 독백 3줄이 흐르고, 손을 떼면 멈춘다. 마지막 줄 "다음 편은… 혼자 봐야 할 거 같아."는 추격의 주마등 "다음 편은 내일 같이 보자."를 회수한다. 이후 현실의 방에서 그녀는 혼자 소파에 앉아, 이유 모를 허전함을 느낀다.</p>

<h3>문제 → 판단 → 해결 (튜닝 기록 26항목 중)</h3>
<table><tr><th style="width:28%">문제 (플레이하며 느낀 점)</th><th style="width:30%">판단</th><th>해결</th></tr>
<tr><td>장례가 단순 홀드라 아무 감정도 전달되지 않음</td><td>지우는 행위 자체가 감정을 만들어야 한다</td><td>기사의 갑옷 파츠를 정해진 순서로 <b>직접 붙잡고 뜯어내는 조작</b>으로 재설계</td></tr>
<tr><td>포착 링 2초가 늘어져 긴박감이 없음</td><td>추격의 리듬을 해치는 늘어짐 제거</td><td>링 2초 → <b>1초</b>, 흡수는 홀드 → <b>3초 안에 연타 10회</b></td></tr>
<tr><td>가시·함정·공격이 겹쳐 무조건 맞는 순간</td><td>불합리하게 지면 쌓아 온 몰입이 깨진다</td><td>기믹이 겹치지 않게 배치, 회피 전 <b>0.4초 예고</b></td></tr>
<tr><td>문구만으로는 둘에게 무슨 일이 있었는지 와닿지 않음</td><td>보여 주는 것이 읽히는 것보다 강하다</td><td>파츠를 뜯을 때마다 <b>기억 장면으로 화면 전환</b> (5초)</td></tr>
<tr><td>주마등 문장이 흡수 완료 시점에 나옴</td><td>망자가 맞은 타이밍에 나와야 한다</td><td>공개 시점을 <b>명중 순간</b>으로 이동 (2.6초)</td></tr></table>
<p class="note">전체 26항목은 게임 기획서 7-5·7-6에 변경 전·후 수치와 이유를 함께 기록했다.</p>

<h3>AI 협업 — 역할 분담</h3>
<table><tr><th style="width:16%">영역</th><th style="width:42%">본인</th><th>AI (Claude)</th></tr>
<tr><td>기획·설계</td><td>세계관·스토리·감정 설계, 조작 규칙, 클라이맥스 구조 결정</td><td>선택지 제시, 문구 초안 2~3안</td></tr>
<tr><td>구현</td><td>플레이 테스트, 버그·불편 판단</td><td>코드 작성, 사운드 합성, 자동 플레이 테스트</td></tr>
<tr><td>튜닝</td><td>직접 플레이 후 수치·규칙 변경 결정, 이유 작성</td><td>요청한 변경을 즉시 빌드에 반영</td></tr>
<tr><td>문서</td><td>기획 의도·판단 근거·최종 확정</td><td>표·서식 정리, 확정 내용 초안</td></tr></table>
<p class="note">AI 초안을 그대로 쓰지 않은 사례: 장례 단순 홀드를 반려하고 갑옷 뜯기로 재설계 / 세계관과 어긋난 단서·스토리 초안을 직접 수정 / AI가 임의로 뺀 '누르기' 조작을 복구하고 "사용자가 정한 구조는 AI가 바꾸지 않는다"는 작업 규칙 추가</p>
<div class="lesson"><b>배운 점</b>수치에 약해 숫자만으로는 판단이 안 됐지만, AI로 바로 만들어 직접 플레이하며 수치와 타이밍을 고치는 방식으로 그 약점을 보완했다.</div>
</div></section>
''' + next_block('memory-ender') + foot(1)
write('projects/memory-ender.html', me)

# ---------------- Aftermath ----------------
af = head('Aftermath | 김준현', 1, 'home') + '''
<header class="phead"><div class="wrap"><div class="k">PROJECT 02 · 팀 프로젝트 · Unity</div><h1>Aftermath</h1><p>5인 온라인 협동 타워 디펜스 — 콘텐츠 기획 담당 (2026.09 ~ 12)</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<div class="stats"><div class="stat"><b>40+</b><span>작성한 기획 문서</span></div><div class="stat"><b>73</b><span>규칙 변경 요청·합의</span></div><div class="stat"><b>37</b><span>Jira 담당 이슈</span></div><div class="stat"><b>5인</b><span>팀 · 콘텐츠 기획</span></div></div>
<table class="info"><tr><td class="h">기간</td><td>2026.09 ~ 12 (12.04 발표회)</td></tr><tr><td class="h">역할</td><td>콘텐츠 기획 (5인 중 1인)</td></tr><tr><td class="h">사용 툴</td><td>Unity · Jira · Confluence · Git · Claude</td></tr></table>
<h3>본인 기여 범위</h3>
<ul class="l"><li>스킬트리, 튜토리얼, 국왕·기사·귀족 추가 콘텐츠, 장비 시스템, 국왕 자동화, 귀족 정책 카드, 프롤로그 캠페인 기획</li>
<li>장비 일반 6종·특수 24종, 정책 카드 21장·전용 이벤트 17개 설계</li>
<li>스킬 데이터테이블에서 구현 수치와 기획의 충돌을 정리하고, 담당별 요청 11건 처리</li>
<li>1차 빌드 초반 구현(PR 10건) 후 기획에 집중</li></ul>
<h3>구현 담당이 바로 작업할 수 있는 전달 방식</h3>
<table><tr><th style="width:24%">단계</th><th>내용</th></tr>
<tr><td>기획서</td><td>규칙·예외·수치의 의도를 먼저 쓰고 상세는 표로</td></tr>
<tr><td>데이터테이블</td><td>수치의 원본. 기획서보다 우선하도록 버전 관리</td></tr>
<tr><td>구현·UI·아트 요청서</td><td>받는 사람별로 나눠 "무엇을, 왜, 우선순위"만 전달. 구현 방식은 담당이 결정</td></tr></table>
<h3>협업에서 지킨 원칙</h3>
<p>다른 파트의 결정은 직접 고치지 않고, <b>규칙 변경 요청서</b>로 현재 규칙·변경 요청·사유·영향을 정리해 제안하고 합의했다 (요청 73건, 명세 반영). 문서는 관리번호 체계로 Confluence에 정리하고, 작업은 Jira 이슈 단위로 진행했다.</p>
<h3>AI 활용</h3>
<p>Git·Jira·Confluence를 AI에 연결해 작업 시작마다 팀의 진행 상황을 동기화하고, 문서 초안·검산·충돌 확인은 AI가, 방향 결정·검토·수정은 본인이 맡았다. 팀원의 작업물을 건드리지 않도록 동기화와 문서 업로드 과정은 정해진 절차(스킬)로 고정했다.</p>
<p class="note">팀 프로젝트의 내부 문서는 비공개 자료라 링크하지 않았습니다. 위 내용은 본인 담당 범위만 정리했습니다.</p>
</div></section>
''' + next_block('aftermath') + foot(1)
write('projects/aftermath.html', af)

# ---------------- 잔향 ----------------
ec = head('잔향 | 김준현', 1, 'home') + '''
<header class="phead"><div class="wrap"><div class="k">PROJECT 03 · 개인 프로젝트 · Unity 6</div><h1>잔향 (Echo)</h1><p>"10초 전의 내가 지금의 동료가 된다" — 시간 루프 퍼즐 플랫포머 (2026.09.11 – 09.18)</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<div class="video" data-v="echo"><div class="ph" style="background:#3A4F7A"><div><b style="font-size:20px;color:#fff">잔향 플레이 영상</b><br>영상 준비 중</div></div></div>
<div class="stats"><div class="stat"><b>30</b><span>방 (스테이지 10 × 3)</span></div><div class="stat"><b>10+</b><span>기믹 종류</span></div><div class="stat"><b>1인</b><span>기획 + AI 협업 구현</span></div><div class="stat"><b>1주</b><span>개발 기간</span></div></div>
<h3>개요</h3>
<p>10초 동안의 움직임이 녹화되고, 되감으면 그 기록이 '잔향'이 되어 그대로 다시 움직인다. 과거의 내가 발판을 밟아 문을 열고, 닿지 않는 절벽은 과거의 나를 딛고 오른다. 목표 감정은 "내 계획이 맞아떨어지는 순간의 쾌감".</p>
<h3>담당 업무</h3>
<ul class="l"><li>컨셉 기획서·WBS 작성, 규칙 설계와 30개 방 레벨 디자인, 이동 방법별 수치 밸런싱</li>
<li>Claude로 구현: 루프·녹화 시스템, 기믹 10여 종, 로비·HUD, 되감기 연출 / 에디터 스크립트로 30개 방 자동 생성</li></ul>
<h3>레벨 설계 — 방법별 도달 높이</h3>
<table><tr><th>열쇠 든 점프</th><th>맨몸 점프</th><th>잔향 딛기</th><th>2단 탑</th><th>잔향 점프대</th></tr><tr><td>2.0</td><td>3.3</td><td>4.5</td><td>5.7</td><td>7.9</td></tr></table>
<p>절벽 높이를 두 값 사이로 정해 "이 방법이 아니면 오를 수 없는" 방을 만들었다. 방 1에서 새 요소를 소개하고 방 3에서 앞 요소를 조합한다.</p>
<h3>문제 → 판단 → 해결</h3>
<table><tr><th style="width:30%">문제</th><th style="width:30%">판단</th><th>해결</th></tr>
<tr><td>잔향 위에 서면 함께 떠오르는 버그</td><td>막기보다 퍼즐 재미로 쓸 수 있다</td><td>'잔향 점프대'를 정식 기믹으로 채택, 스테이지 4~5의 중심 규칙으로</td></tr>
<tr><td>후반 스테이지가 같은 풀이의 변주뿐</td><td>새로 배우는 규칙이 필요하다</td><td>'들면 점프가 낮아지는 열쇠' → 과거의 나에게 심부름 맡기는 퍼즐</td></tr>
<tr><td>마지막 방에서 의도보다 쉬운 풀이</td><td>감이 아닌 수치로 막아야 한다</td><td>점프 속도·중력으로 이동 거리 계산 → 열쇠·천장·절벽 높이 조정</td></tr></table>
<h3>문서</h3>
<div class="docs"><a class="btn o" href="https://docs.google.com/document/d/1vu-dxKQKkXPBQW5wbZy_s9ofKNE3KVF78_-24ECuPBc/view">컨셉 기획서</a><a class="btn o" href="https://docs.google.com/document/d/1d-xTOKkE7-KGidSy0CwK18o8fCUlGtUQuFIlzTlgtlg/view">WBS</a></div>
<div class="lesson"><b>배운 점</b>기획서는 만드는 사람이 그대로 구현할 만큼 구체적이어야 하고, 의도는 수치와 조건으로 고정해야 지켜진다.</div>
</div></section>
''' + next_block('echo') + foot(1)
write('projects/echo.html', ec)

# ---------------- WHO AM I ----------------
wa = head('WHO AM I? | 김준현', 1, 'home') + '''
<header class="phead"><div class="wrap"><div class="k">PROJECT 04 · 팀 프로젝트</div><h1>WHO AM I?</h1><p>감정 곡선 레벨 설계</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<h3 style="margin-top:0">WHO AM I? — 추리 미스터리 비주얼 노벨 (5인 팀 · 1주 · 2026.04)</h3>
<p><b>역할:</b> 컨텐츠 · 레벨 디자인 — 여섯 방의 감정 곡선과 배치 순서, 방별 조사 루프·아이템·상호작용 조건 설계, 팀원이 그대로 구현할 수 있는 조건 문서 작성</p>
<h3>팀 내 역할 (5인 · 렌파이 · 2026.04.20 – 26)</h3>
<table><tr><th style="width:30%">역할</th><th style="width:16%">담당</th><th>범위</th></tr>
<tr><td>PM · 프로그래밍</td><td>팀원 1</td><td>일정 관리, 렌파이 구현</td></tr>
<tr><td><b>콘텐츠 · 레벨 디자인</b></td><td><b>본인</b></td><td><b>여섯 방의 감정 단계와 배치 순서, 방별 조사 루프·아이템·상호작용 조건, 구현용 조건 문서</b></td></tr>
<tr><td>리소스 디자인</td><td>팀원 1</td><td>배경·이미지 리소스</td></tr>
<tr><td>시나리오 · 스크립트</td><td>팀원 2</td><td>메인 시나리오와 서브 스크립트</td></tr></table>
<h3>감정 설계 — 여섯 방의 배치 순서</h3>
<div class="fig"><img src="../assets/img/whoami_emotion.svg" alt="감정 단계별 여섯 방 배치"></div>
<table><tr><th style="width:18%">단계</th><th style="width:20%">방</th><th>설계</th></tr>
<tr><td>1 · 호감</td><td>언제 · 어디서</td><td>인물 정보 없이 배경만 서술해 분위기에 몰입시키고 NPC에게 호감을 갖게 함</td></tr>
<tr><td>2 · 의심·불안</td><td>무엇을 · 어떻게</td><td>사건의 실마리를 드러내 1단계의 호감과 부딪히게 함</td></tr>
<tr><td>3 · 혼란 → 선택</td><td>왜 · 누가</td><td>NPC 정체를 공개하는 '누가'를 마지막 방에 두어 엔딩 선택(3종)에 직결</td></tr></table>
<h3>플레이 루프</h3>
<div class="fig" style="max-width:640px"><img src="../assets/img/whoami_loop.svg" alt="조사, 아이템 획득, 해금, 단서 확인 루프"></div>
<p>조사 → 아이템 획득 → 해금 → 단서 확인 루프. 스토리 전달이 핵심이라 퍼즐 난이도는 낮추고, 탐색하는 동안 추측이 쌓이도록 했다.</p>
<h3>레벨 설계 슬라이드</h3>
<div class="slides"><iframe src="https://docs.google.com/presentation/d/11o8cVJIv6a7kVMNV6VL-Kx9cTSWrfof7U1WdUt_ZhTg/embed?start=false&loop=false" allowfullscreen loading="lazy" title="WHO AM I? 레벨 설계 슬라이드"></iframe></div>
<div class="docs"><a class="btn o" href="https://docs.google.com/presentation/d/11o8cVJIv6a7kVMNV6VL-Kx9cTSWrfof7U1WdUt_ZhTg/view">새 창에서 보기</a></div>
</div></section>
''' + next_block('whoami') + foot(1)
write('projects/whoami.html', wa)

# ---------------- 소개 ----------------
ab = head('소개 | 김준현', 0, 'about') + f'''
<header class="phead"><div class="wrap"><div class="k">ABOUT</div><h1>김준현</h1><p>오래 남는 순간은 우연이 아니라 설계입니다.</p></div></header>
<section class="s"><div class="wrap"><div class="about">
<img class="ph" src="assets/img/photo.png" alt="김준현">
<div>
<p style="font-size:18px;color:var(--navy);font-weight:700">'플레이어가 이 순간 무엇을 느껴야 하는가'부터 정하고, 그 감정이 생기도록 규칙과 레벨을 거꾸로 짭니다.</p>
<p>방송연예학과에서 연극 연출을 하며, 한 장면의 감정을 위해 조명과 음향의 타이밍, 배우의 동선을 계속 연구했습니다. 그 경험을 플레이어가 직접 움직이는 게임에서 쓰고 싶어 게임 기획을 시작했습니다.</p>
<div class="chips"><span class="chip">감정 곡선 기반 레벨 설계</span><span class="chip">수치로 해법을 강제하는 퍼즐</span><span class="chip">바로 구현되는 기획서</span><span class="chip">연출 전공의 장면 구성 감각</span><span class="chip">AI와 함께 끝까지 구현</span></div>
<div class="btns"><a class="btn n" href="files/portfolio.pdf">포트폴리오 PDF</a><a class="btn o" href="mailto:rlawnsgus560@gmail.com">rlawnsgus560@gmail.com</a></div>
</div></div>

<h3>걸어온 길</h3>
<div class="tl">
<div><b>2026.04 – 12</b> 디벨로켓(경일게임아카데미) 게임 기획 교육과정 (2026.12 수료 예정) — Aftermath, 잔향, WHO AM I?, 메모리 엔더</div>
<div><b>2025.11 – 2026.03</b> 오진양행 서비스사업부 — 커피머신 방문 수리·점검 및 고장 원인 진단</div>
<div><b>2023.02</b> 가톨릭관동대학교 방송연예학과 연출전공 학사 졸업</div>
<div><b>2021</b> 정기공연 '벚꽃동산' 연출 — 30명, 2개월, 40석 7회 전석 만석 / 극단 임영씨어터 대표로 '하멜린' 기획·운영·정산</div>
<div><b>2019</b> 정기공연 '임차인' 첫 연출 (7회)</div>
</div>

<h3>일하는 방식</h3>
<table><tr><th style="width:18%">단계</th><th>방식</th></tr>
<tr><td>규칙부터</td><td>작업 방향을 정하는 세션을 먼저 열어 규칙 문서를 만들고, AI 프로젝트에 넣어 둔다</td></tr>
<tr><td>동기화</td><td>팀 작업은 깃허브·Jira·Confluence에서 읽어 와 진행 상황부터 맞춘다. 팀원 작업물을 건드리지 않도록 절차를 스킬로 고정</td></tr>
<tr><td>토론</td><td>내 초안을 주고 이유와 안 되는 점을 반론하게 한 뒤 결정한다</td></tr>
<tr><td>검증</td><td>간단히 구현해 직접 플레이하며 조정한다. 재미와 감정은 내가 판단한다</td></tr></table>

<h3>AI 활용 범위</h3>
<table><tr><th style="width:18%">결과물</th><th style="width:40%">본인</th><th>AI (Claude)</th></tr>
<tr><td>메모리 엔더</td><td>기획·설계·튜닝 결정, 플레이 테스트</td><td>코드, 사운드 합성, 문구·문서 초안</td></tr>
<tr><td>잔향</td><td>기획·레벨 디자인·수치 밸런싱</td><td>시스템·기믹 코드</td></tr>
<tr><td>Aftermath</td><td>콘텐츠 기획, 방향 결정·검토·수정</td><td>문서 초안·검산·충돌 확인</td></tr>
<tr><td>이 사이트</td><td>구성·내용 결정</td><td>페이지 코드, 내용 정리</td></tr></table>

<h3>도구</h3>
<div class="chips"><span class="chip">Unity 6</span><span class="chip">VS Code</span><span class="chip">Git</span><span class="chip">Claude · Claude Code</span><span class="chip">Jira</span><span class="chip">Confluence</span><span class="chip">Notion</span><span class="chip">Excel</span><span class="chip">PowerPoint</span></div>
</div></section>

<section class="s alt"><div class="wrap">
<h2 class="t">프로젝트 다시 보기</h2><p class="st">궁금한 프로젝트를 골라 기획 의도와 설계 과정을 확인해 보세요.</p>
<div class="cards">{''.join(card(pr, '') for pr in PROJECTS)}</div>
</div></section>
''' + foot(0)
write('about.html', ab)
print('ok')
