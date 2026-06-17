FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Streamlit의 기본 포트인 8501번 지정
EXPOSE 8501

# 컨테이너 실행 시 외부 접속을 허용하는 옵션으로 Streamlit 실행
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]