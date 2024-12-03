import requests
import pickle
import time
from bs4 import BeautifulSoup
import ddddocr

head = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

def download_img(filename , href):
    img = requests.get(href, headers=head)
    with open(filename , 'wb') as file:
        file.write(img.content)
import json

def save_cookies_to_file(session, filename):
    with open(filename, 'w') as file:
        json.dump(session.cookies.get_dict(), file)

def load_cookies_from_file(session, filename):
    with open(filename, 'r') as file:
        cookies = json.load(file)
        session.cookies.update(cookies)

def login_to_website(base_url, login_path, username, password):
    """
    使用爬蟲模擬登錄網站。
    :param base_url: 網站的基礎 URL，例如 "https://example.com"
    :param login_path: 登錄的 URL 路徑，例如 "/login"
    :param username: 登錄帳號
    :param password: 登錄密碼
    """

    # 建立一個 session 以保留 Cookies
    # session = requests.Session()
    session = requests.Session()
    load_cookies_from_file(session, "cookies.json")
    a = '/WebResource.axd?d=tBmHPwqt5FZ_fz9Akc9MrJaFgPQJw412uICKlLfoMPw5ZrxpqET-qokPkZQzXaX0TRBPEoHZ1qqa_0aDlJfku8zi6zw1&t=63856889274506778'
    b = '/ScriptResource.axd?d=DqBaCMv3HvhEO-U4ESLWYrZY2mo5nHKEJCDb9act8CeFzbCFI-fn1K4WuIYtI9_0UdMgER1Mo_hMrd_To1Kn0rt86dZIhkyUS4g-5tPddT8ffK6pFZEDiZWRklKEMLZw543VA9IzOuleFA0RBs-12WCHZeBoE4zTfHKfx74RVzy3jLlJa9MpsZjkhzhhdixsDILUiQ2&t=ffffffffc820c39'
    c = '/ScriptResource.axd?d=v24Q6AfOjuOjn_zfhYrZXqSw3ofXPBtdRu-6fHzA47xb43Ei2VMZiLw3FpCj7aZK7GcyFY_RzHpi5zFofZfvoghQKf1GsmJAElyP1-Dup0UxbuoZB3In_VFJTM0mHlI5zwl36lrHPMYZaK_F9pwvOol4Si4UQ7cfKYgVgQf1SYfBBAef0&t=ffffffffc820c39'
    d = '/ScriptResource.axd?d=1iwX_N96F-GE2OSWzmJueu4xawlIvxaYJkz5_lyAK0DgAJ2tOakpmh_iZS1wUHtwGuM7QVIcuI_6zcxr0AaJUp12YDW9AKW-7CM7wzh8TJM4yO0IFwzei0Tzr5Jbc7kQ4KeM_82VLjgLR77gQ631TYjIAC2y59hBxAIwS2iUC-swE4AN0&t=ffffffffc820c39'
    e = '/script/DateUtil.js'

    # Step 1: 取得登入頁面，並抓取 CSRF token（如需要）
    save_cookies_to_file(session, "cookies.json")
    return session
    # while 1:
    #     response = requests.get(base_url+login_path, headers=head , cookies=session.cookies)
    #     while len(response.text) <= 200:
    #         # session = requests.Session()
    #         # Step 1: 取得登入頁面，並抓取 CSRF token（如需要）
    #         response = requests.get(base_url + login_path ,headers=head , cookies=session.cookies)

    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     img = soup.find_all('img' , id ="importantImg")
    #     print(img)
    #     link = img[0].get('src')
    #     if link != None:
    #         break
    # link = base_url + link
    # download_img("CatchaImage.png" , link)
    # # 假設 CSRF token 在 `<input name="csrf_token" value="...">` 中
    # # csrf_token = soup.find("input", {"name": "csrf_token"})["value"] if soup.find("input", {"name": "csrf_token"}) else None
    # ocr = ddddocr.DdddOcr(beta=True)  # 切换为第二套ocr模型
    # image = open("CatchaImage.png", "rb").read()
    # csrf_token = ocr.classification(image)
    # csrf_token = csrf_token.upper()
    # print(csrf_token)


    # # Step 2: 模擬登錄表單提交
    # login_payload = {
    #     "M_PORTAL_LOGIN_ACNT": username,
    #     "M_PW": password,
    #     "M_PW2": csrf_token,  # 如果有 token，則添加
    # }

    # login_response = session.post(login_url, data=login_payload, headers=head)
    # # print(login_response)
    # login_response = session.get("https://ais.ntou.edu.tw/MainFrame.aspx")

    # if login_response.status_code == 200 and "Dashboard" in login_response.text:
    #     print("登錄成功！")
    #     return session  # 返回已登錄的 session
    # else:
    #     print("登錄失敗！")
    #     return None

def access_protected_page(session, protected_path, base_url):
    """
    使用已登錄的 session 訪問受保護的頁面。
    :param session: 已登錄的 requests.Session
    :param protected_path: 受保護頁面的路徑，例如 "/dashboard"
    :param base_url: 網站的基礎 URL
    """
    protected_url = base_url + protected_path
    response = session.get(protected_url)

    if response.status_code == 200:
        print(f"成功訪問受保護頁面：{base_url+protected_path}")
        response = BeautifulSoup(response.text , "html.parser")	
        print(response)  # 顯示前 500 字元
        return
    else:
        print(f"無法訪問受保護頁面，狀態碼：{response.status_code}")

# 使用範例
if __name__ == "__main__":
    base_url = "https://ais.ntou.edu.tw"  # 更改為目標網站的主 URL
    login_path = "/Default.aspx"            # 更改為登入頁面的路徑
    protected_path = "/MainFrame.aspx"    # 更改為受保護頁面的路徑
    username = "123123"       # 替換為實際帳號
    password = "123123"       # 替換為實際密碼

    # 執行登錄
    session = login_to_website(base_url, login_path, username, password)

    # 若登錄成功，訪問受保護的頁面
    if session:
        access_protected_page(session, protected_path, base_url)
        course_list_url = '/Application/TKE/TKE22/TKE2240_.aspx?progcd=STU1220'