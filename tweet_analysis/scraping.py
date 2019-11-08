from bs4 import BeautifulSoup
import requests
from google.colab import files
import pandas as pd

# スクレイピングURL
url = ""
response = requests.get(url).text

# BeautifulSoupの初期化
soup = BeautifulSoup(response, 'html.parser')

# タイトルとURLのタグを取得
tags = soup.find_all("", {"class": ""})

# データフレームを作成。列名：name, url
columns = ["name", "url"]
df2 = pd.DataFrame(columns=columns)

# 記事名と記事URLをデータフレームに追加
for tag in tags:
    name = tag.a.string
    url = tag.a.get("href")
    se = pd.Series([name, url], columns)
    print(se)
    df2 = df2.append(se, columns)

# Fileを自動DL
filename = "result.csv"
df2.to_csv(filename, encoding = 'utf-8')
files.download(filename)