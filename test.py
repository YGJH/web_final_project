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
# print(f'word= {word}')
url = 'https://ais.ntou.edu.tw/MainFrame.aspx'
head = {
    "Cookie":"ASP.NET_SessionId=10bqlkxsnce20ne1geqvu0cq; f5-ltm=!H0jGCPG4B8UkCDIpErpzwHvgcas10caFkSMh1JPHqzX6f11CcMHlV8B5S0B2fVmaPYgg3FaM7X9/K2k=; .ASPXAUTH=1810B75BD430B6F6BFF0BC3DC80C23C1565E34660D0FEAB9B87D4179A2CBC39CBAF11ECDD2A25BE7E00371D25BFF4D71CB65A5B8CA537D64B2EE919FAA8FD05813878FEEEEF37A5C4C04180F9E7712C8844F4C129948EC1D7853788BA290F342D3D7132DB6F65420796C60CD5BCA7067E40BB128; TS01a306fb=01c1994270eff9676afce4902f1a08f49d1be7f88b7cd4ad114af24c11879ee56234719392249b8dff521461799279b35ed7e9e4e91a0aeda433154f430265243282c08f8a100002107aed9baf409fc32a51dfdfc7be1a365091b9c02fdd1227a20c879820",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
def download_img(filename , href):
    img = requests.get(href, headers=head)
    with open(filename , 'wb') as file:
        file.write(img.content)


def main():
    # 使用示例
    # login_handler = WebLogin()

    # while True:
    while True:
        response = requests.get(url=url , headers=head)
        if len(response.text) <= 200:
            continue
        else:
            break
    
    # response = requests.get('https://ais.ntou.edu.tw/Application/TKE/TKE22/TKE2240_.aspx?progcd=STU1220',headers=head)
    # response = requests.get('https://ais.ntou.edu.tw/Css/RWDCss/remixicon/remixicon.woff2?t=1708865856766',headers=head)
    response = requests.get(url='https://ais.ntou.edu.tw/Application/TKE/TKE22/TKE2240_01.aspx',headers=head)
    soup = BeautifulSoup(response.text , "html.parser")
    print(soup)
    table = soup.find_all('table')
    print(table)
    
# user = browser.find_element_by_id('ctl00_Login1_UserName')
# passwd = browser.find_element_by_id('ctl00_Login1_Password')
# vcode=browser.find_element_by_id('ctl00_Login1_vcode')


# userid='這裡改成你的帳號'
# userpw='這裡改成你的密碼'
# user.send_keys(userid)
# passwd.send_keys(userpw)
# vcode.send_keys(res)



#         img = soup.find_all('img' , id='importantImg')
#         print(img)
#         link = img[0].get('src')
#         if(link is None):
#             continue
#         link = "https://ais.ntou.edu.tw/MainFrame.aspx" + link
#         filename = 'CatchaImage.png'
#         download_img( filename , link)
#         image = Image.open('CatchaImage.png')
#         result = pytesseract.image_to_string(image)
#         result = result[-4:]
#         ocr = ddddocr.DdddOcr()

#         image = open("CatchaImage.png", "rb").read()
#         result = ocr.classification(image)
#         print(result)
#         if len(result) == 4 and result[0] in word and result[1] in word and result[2] in word and result[3] in word:
#             break
#         else:
#             continue
    
#     print(result)
    
#     # 使用 requests 方式登錄
#     login_success = login_handler.requests_login(
#         login_url=url,
#         M_PORTAL_LOGIN_ACNT='01257049',
#         M_PW='Jihuty940123',
#         M_PW2={'Check': f'{result}'}
#     )
        
#     if login_success:
#         # 保存 cookies
#         login_handler.save_cookies('cookies.json')
        
#         # 檢查登錄狀態
#         is_logged_in = login_handler.check_login_status('https://ais.ntou.edu.tw/Default.aspx')
#         print(f'登錄狀態: {"已登錄" if is_logged_in else "未登錄"}')
    
#     # 使用 Selenium 方式登錄
#     selenium_success = login_handler.selenium_login(
#         login_url=url,
#         M_PORTAL_LOGIN_ACNT='01257049',
#         M_PW='Jihuty940123'
#     )
    
#     if selenium_success:
#         print('Selenium 登錄成功')

if __name__ == '__main__':
    main()