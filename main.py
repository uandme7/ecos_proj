from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests

# .env 파일에서 환경 변수 로드
load_dotenv()

# FastAPI 앱 생성
app = FastAPI()

# API 키 가져오기
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://ecos.bok.or.kr/api"

@app.get("/")
async def root():
    return {"message": "Welcome to the Public Data App"}

@app.get("/economic-data")
async def get_economic_data(start_date: str, end_date: str):
    """
    Fetch economic data from Bank of Korea API.
    - start_date: 시작 날짜 (형식: YYYYMM)
    - end_date: 종료 날짜 (형식: YYYYMM)
    """
    url = f"{BASE_URL}/StatisticSearch/{API_KEY}/json/kr/1/10/902Y001/M/{start_date}/{end_date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"status": "success", "data": data}
    else:
        return {"status": "error", "message": "Failed to fetch data"}
