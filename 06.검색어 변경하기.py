import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = input("검색어를 입력하세요>>>")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트
print(links)
for link in links :
    title = link.text # 태그 안에 텍스트 요소를 가져온다
    url = link.attrs['href'] #href의 속성값을 가져온다.
    print(title,url)