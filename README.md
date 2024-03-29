# book-chatbot

ICT 도서추천 챗봇

## 도서추천 챗봇 만들기 (한이음 프로젝트)

[한이음 팀블로그](https://www.hanium.or.kr/portal/project/teamBlogView.do)

![main character](https://github.com/BookChatbot/itggi-api/assets/60846847/90d7bea0-b9ad-4551-b467-9be7742a6b56)

### 팀명: 책잇아웃

- 멘토: 김현진
- 팀장: 곽유진
- 팀원: 김병준
- 팀원: 이범기
- 팀원: 정예빈

### 팀 활동

- 매일 월요일 9시 회의 (Google Meet)
- 회의 및 스터디 내용 문서화(Notion)
- 활발한 소통 (KakaoTalk)
- Gitlab 을 활용하여 프로젝트 관리 및 협업

### 시스템 구성도

![system architecture](https://github.com/BookChatbot/itggi-api/assets/60846847/5101bbb4-4771-46b2-b58a-798dd65af79f)

### 추천 기능

- 오늘의 책 추천 (베스트셀러)
- 줄거리 기반 추천 (Word2Vec, Doc2Vec)
- 평점 기반 추천 (협업 필터링)
- 장르 기반 추천 (장르 필터링)
- 영화 & 음악 추천 (책 기반 유사한 영화 or 음악 추천)

### 챗봇 구현

- KakaoTalk 채널 봇을 활용하여 채팅 시스템 구현
- 대화형 방식으로 원하는 메뉴로 대화를 통해 진입 가능
- 버튼형 방식으로 직관적인 쉬운 사용 가능

### 내 서재 기능

- 읽고 싶은 책
  - 추천 받은 책이나 검색한 책 중 읽고 싶은 책으로 저장하여 확인 가능
- 읽은 책
  - 읽은 책에 대하여 평점을 남기고 리뷰 남기기 가능
  - 저장한 리뷰를 확인하고 수정 가능
  - 평점을 남긴 책에 대하여 분석하여 맞춤 추천 데이터로 활용
- 저장한 책 들을 확인하고 삭제 가능
- 독서량 자신의 랭킹 확인 (다른 유저들과 비교한 그래프)

### 검색 기능

- 키워드 검색
  - 키워드 (제목, 작가, 출판사 등)의 단어를 입력하면 관련된 책 검색
- 바코드 검색
  - 바코드를 찍어서 ISBN 값을 가져와 책 검색 가능
- 검색한 책을 '내 서재' 에 저장 가능


### 메뉴 구성도

![menu](https://github.com/BookChatbot/itggi-api/assets/60846847/5ff1e819-9fcf-4bbf-be27-96977cadc78d)
