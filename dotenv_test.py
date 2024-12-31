from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# API 키 읽어오기
API_KEY = os.getenv("API_KEY")

print(f"Your API Key: {API_KEY}")  # 테스트용
