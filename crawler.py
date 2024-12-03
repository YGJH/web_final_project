import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from typing import Dict, Optional
import logging
from bs4 import BeautifulSoup
from http.cookies import SimpleCookie
import pytesseract
from PIL import Image
import os
import ddddocr


word = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321".replace('' , ' ')[1:-1]
word = word.split(' ')
# url = 'https://ais.ntou.edu.tw/Default.aspx'
init_head = {
    "Cookie":"ASP.NET_SessionId=nxwgtesrn3fn32vjgbw0ls0t; f5-ltm=!vmlvqe2FugODfyYpErpzwHvgcas10c3rB/TjX9iDfYdPmPN1wuh3956rvlXKwj82NoBvq/oK+qGgJvQ=; .ASPXAUTH=7192454ED6D0BFA213FD3947C64F5D3F2DB532A8EFE8B521245D8B9686F6D0F97CA8C4955716B90D5EA64D9F90D5F3E8E97F24ED0E86FA2919FDAB637EE7CEF868723874FAA7B3864F67117FF366E180C9E8953FDF5D9501DF5D2BC5759BFE1551205264B2FF670B5C45DF9F7D9843F1BB57AD13; TS01a306fb=01c199427081c4766b324918fd45673695e057002a586745d74bb6d052ede68331f5e4b395505e26846abe1434ed5a9c414a5a3eaad62b9e5b2cc5c1269936c8776d8bcd0932b02b2c09ca49722654628d42632acc63b209ff51b40df95d0c92d519a467ee",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}



def download_img(filename , href):
    img = requests.get(href, headers=init_head)
    with open(filename , 'wb') as file:
        file.write(img.content)


def main():
    # 使用示例
    # login_handler = WebLogin()
    url_head = "https://ais.ntou.edu.tw"
    url_login = "/Default.aspx"
    url_main = "/MainFrame.aspx"
    url = url_head+url_main
    soup = None
    while True:
        session = requests.Session()
        response = session.get(url=url , headers=init_head)
        if len(response.text) <= 200:
            continue
        else:
            # 第一次請求，會自動獲取並保存Cookie
            # soup = BeautifulSoup(response.text , "html.parser")
            # img = soup.find_all('img' , id ="importantImg")
            # link = img[0].get('src')
            # link = url_head + link
            # download_img("CatchaImage.png" , link)
            break
    
    
    url_course = '/Application/TKE/TKE22/TKE2240_.aspx'
    url = url_head + url_course
    response = session.get(url , headers=init_head)
    soup = BeautifulSoup(response.text , "html.parser")
    print(soup)

    # ocr = ddddocr.DdddOcr(beta=True)  # 切换为第二套ocr模型

    # image = open("CatchaImage.png", "rb").read()
    # result = ocr.classification(image)
    # result = result.upper()
    # print(result)


if __name__ == '__main__':
    main()