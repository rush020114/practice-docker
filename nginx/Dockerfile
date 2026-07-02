# FROM
# docker hub로부터 nginx의 이미지를 가져와서 runtime 환경을 설정
FROM nginx
# COPY
# ├── 왼쪽 → 내 로컬 파일 (index.html)
# └── 오른쪽 → 컨테이너 안에 복사할 경로
# "내 nginx.conf파일을 컨테이너 안의 /etc/nginx/conf.d/default.conf 에 복사해줘"
COPY nginx.conf /etc/nginx/conf.d/default.conf