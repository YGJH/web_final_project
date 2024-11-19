from bs4 import BeautifulSoup
import requests


head = {
    # "Cookie":"ASP.NET_SessionId=jzz1aqgyyj0cwgsivtgfcxdp; f5-ltm=!4QtunCJBD1Fyu+IpErpzwHvgcas10VOp96Mi93sY/1UaJjdx9xTZyCrP11oykX+RagITCZ1j7kUfTKQ=; .ASPXAUTH=96F8EA386F58160FFFF47C18C62408E6399883CD1B9367F6BCD16D3CC43C54E0A20F20C49DF00AF7F8CE2E1EA148CC1E52BBA723B1ED62A29C7D208E524859A4E5C600E936CEA2658F028F141A5510EFC91C3A9EA318B0F0EEDA4FE1D749FEFA4F972C31D23CD0772630EBBA4B46A58D975D977F; TS01a306fb=01c199427035c9a51fbac6da2526634626bf6922c9afeae467f5d2c58ef007cd97f2b8db50bdc0dd10621227ac1f35b09b36fa040608b91aa41112c4f194954f2c430bf2a576d20da899d9444d7d0532257ac120a3315340dd0fe0c703e0ccc66d322d2570",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
data = {
    "loginName":"你的账号",
    "password":"你的密码"
}

url = "https://ais.ntou.edu.tw/MainFrame.aspx"
session = requests.session()

data = {
    "loginName":"01257049",
    "password":"Jihuty940123",
}




content = requests.get(url=url , headers=head)
while True:
    if content.ok:
        val = content.text
        if len(val) <= 200:
            content = requests.get(url=url , headers=head)
            continue
        
        print(val)

        break
    else:
        print('fail to get response')




