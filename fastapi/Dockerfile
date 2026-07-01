FROM python:3.10
# WORKDIR
# → 컨테이너 안에서 작업할 폴더 지정
# → /app 폴더 만들고 거기로 이동
#
# 이후 명령어들이 전부 /app 안에서 실행됨
# ├── COPY . .   → /app 안으로 복사
# ├── RUN pip    → /app 안에서 실행
# └── CMD        → /app 안에서 실행
WORKDIR /app
# COPY . .
# ├── 왼쪽 . → 내 로컬 현재 폴더 전체
# └── 오른쪽 . → 컨테이너 WORKDIR(/app)
#
# 즉
# main.py, requirements.txt 등
# 전부 다 /app 안으로 복사
COPY . .
# RUN → image 빌드할 때 실행되는 명령어
#
# "pip install -r requirements.txt 실행해줘"
# → requirements.txt에 있는 라이브러리 설치
# → fastapi, uvicorn 설치됨
RUN pip install -r requirements.txt
# EXPOSE → "나 8000번 포트 쓸 거야" 라고 선언
#           문서화 용도
#           실제로 포트를 열어주는 건 아님
#
# 실제 포트 연결은
# docker run -p 8000:8000 할 때 열림
EXPOSE 8000
# CMD → 컨테이너 실행될 때 자동으로 실행할 명령어
#
# "uvicorn으로 main.py의 app을 
#  0.0.0.0:8000 으로 실행해줘"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]