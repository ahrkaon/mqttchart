mqtt로 보낸 bmp180데이터 중 온도를 그래프
TCP Clinet (교재 4장 예제)
TCP Server (교재 echo서버 + 파일 쓰기)
chart.html (메인 페이지)
sensor-data.html (temp 데이터 값)
solar.html (태양 전압값(임의) 그래프 이미지 저장용 페이지)
ctolist.py (csv읽어서 리스트화)
chartapp.py (flask 서버, 각 데이터 저장용 코드)
sqlconnect.py (mqtt값 최근 10개 데이터 조회)
test.js (temp 그래프 그리기 및 30초마다 자동 갱신)
