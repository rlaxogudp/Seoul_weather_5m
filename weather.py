import requests # url : get요청
import csv # csv로 저장
import os # 폴더 생성
from datetime import datetime # 시간 변환
city = "seoul"
API_KEY_W = os.getenv("API_KEY_W")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
result = response.json()
temp = result["main"]["temp"] # 현재 기온
humidity = result["main"]["humidity"] # 습도
weather = result["weather"][0]["main"] # 날씨 상태
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 현재 시각

# csv
header = ["current_time", "weather", "temp", "humidity"]
# 만약 파일이 없으면 만들고 있으면 덮어쓰기
csv_exist = os.path.exists("seoul_weather.csv")

with open("seoul_weather.csv", "a") as file:
    writer = csv.writer(file)
    if not csv_exist:
        writer.writerow(header)

    writer.writerow([current_time, weather, temp, humidity])
    print("서울 기상 상태")
