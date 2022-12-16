# python request 基本使用方法


## 1. requests 介紹
### requests使用時機
我個人認為requests使用就是主要來爬網頁,最好是能夠搭配BeautifulSoup做使用  
將所想要的資訊做成表格,或是自動化去做一些事情,主要看個人使用方式  
```
import requests
from bs4 import BeautifulSoup
```

### 簡單使用request方法
使用requests,需要Headers將UA加入,讓網站會覺得你是使用瀏覽器作業,否則有可能會判定你是機器人不給瀏覽   
headers值可以透過,chrome F12 開發人員查看,一般都會在headers底下,只接複製貼上到程式碼就可以使用,  
這個user-agent就是使用自己本機開啟的瀏覽器,像我範例是使用chrmoe開啟的  
![image](https://user-images.githubusercontent.com/16216879/195295470-7297420c-30dd-4c99-ad95-01d6ba865ead.png)  

```
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
```

### 使用get方法
一般爬網一樣是透過F12 開發人員,裡面的網路(network)確認他的行為,  
並且用程式去模仿它的行為


![image](https://user-images.githubusercontent.com/16216879/195299571-7bee247a-6322-4744-beac-d428732eb07d.png)  

一般找網路內容都是看像"文件"的檔案,主要網站讀取都是透過它  
其他部分像是css,javascript等等之類都是用來美觀網頁,或是跟後端要一些資料,但是主要觀察得對象為網站為主  
### requests.session()
我會透過resquets內的方法session作為爬網的主窗口
```
request = requests.session()
```
然後再使用get方法,並代入headers,用法如下:  
request.get( "URL", headers = dict )
```
google = request.get('https://github.com/login?',headers=headers)
```
### 使用BeautifulSoup
BeautifulSoup有很多方法可以使用,目前主要了解大致理解怎麼使用requests  
BeautifulSoup('html','html格式'(html.parser=>為BeautifulSoup default))   
``` 
soup = BeautifulSoup(google.text,'html.parser')
```

### 完整code
```
import requests
from bs4 import BeautifulSoup
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
request = requests.session()
google = request.get('https://github.com/login?',headers=headers)
soup = BeautifulSoup(google.text,'html.parser')
print(soup.prettify()) 
```

## 2. request進階用法(login)
request其實就跟其他api應用一樣,但是如果網站或是開發人沒有提供api,  
可以透過觀察web上的行為,去模仿怎麼去使用,可以透過github來示範怎麼去登入網站,並去想要到的地方  
  
我們可以先從github F12開發人員觀察web的行為,可以看到登入頁面是使用get  
![image](https://user-images.githubusercontent.com/16216879/195480595-f1a8744c-b874-4815-a57b-a6429af56c41.png)
  
在登入觀察一下看看web是什麼樣的狀態,而發現網站則是是使用post,並且可以看到他往哪個url送去(https://github.com/session)    
![image](https://user-images.githubusercontent.com/16216879/195488113-d3d1e749-11aa-4a90-afae-f3877edf1875.png)


### get解釋
get的方法就是唯獨,去訪問web不改變伺服器的任行資訊,簡單來說可以要做"讓我看看"  
### Post解釋
Post的方法就是送出,去提交Web一些資訊給伺服器做使用,簡單來說"登入"就像是比較常送的資料,也要依Web開發人員配置的行為為主  

基於post的理論,我們可以去觀察登入到底提交了什麼資訊伺服器,從F12開發人員=>Payload可以查看,如圖:  
![image](https://user-images.githubusercontent.com/16216879/195482834-4e024929-8a93-4858-8ca1-5710c1dfb78b.png)
登入提交的清單如下:
```
commit: Sign in
authenticity_token: 提交表單後的安全authenticity_token,會依登入狀態而改變
login: 個人帳號
password: 個人密碼
webauthn-support: supported
webauthn-iuvpaa-support: unsupported
return_to: https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home
allow_signup: 
client_id: 
integration: 
required_field_1a96: 
timestamp: 登入狀態而改變
timestamp_secret: 登入狀態而改變
```
那我們要怎麼獲得這些資訊呢?可以到login的web上查看,一般使用Post功能都會透過html<From>的框架去發送,我們可以觀察一下,如圖:  
  ![image](https://user-images.githubusercontent.com/16216879/195484429-80266135-abd4-4a7c-bcf5-0603887f3489.png)
  那還有其他的參數也是要這樣去查找,或是可以透過搜尋去找這些參數  
  ![image](https://user-images.githubusercontent.com/16216879/195484793-ee26f0cb-850a-4660-86eb-2e9ff6634bb4.png)
  那在code中怎麼表示查找這些參數呢?可以透過BeautifulSoup去將這些參數爬出來  

先將網頁資訊爬下來,code如下
```
import requests
from bs4 import BeautifulSoup
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
request = requests.session()
login_page = request.get('https://github.com/login?',headers=headers)
soup = BeautifulSoup(login_page.text,'html.parser')
```
然後我們使用BeautifulSoup去獲取authenticity_token的資料  
我們可以觀察web上的資訊,去透過find去找這些參數,input到name一層一層下去找參數   
![image](https://user-images.githubusercontent.com/16216879/195486034-ca0748a3-5ad3-4070-82b4-7ce6510f9a0f.png)
code如下:
```
authenticity_token = soup.find('input', {"name": "authenticity_token"} ).get('value')
```
使用上面這個方法,我們可以將payload的資訊模仿出來,在使用post的方式去登入    
post用法:request.post('URL',data='觀察的payload',headers='使用假UA')  
code如下:  
```
import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

request = requests.session()
login_page = request.get('https://github.com/login?',headers=headers)


soup = BeautifulSoup(login_page.text,'html.parser')
authenticity_token = soup.find('input', {"name": "authenticity_token"} ).get('value')
commit = soup.find('input', {"name": "commit"} ).get('value')
webauthn_support = soup.find('input', {"name": "webauthn-support"} ).get('value')
return_to = soup.find('input', {"id": "return_to"} ).get('value')
timestamp = soup.find('input', {"name": "timestamp"} ).get('value')
timestamp_secret = soup.find('input', {"name": "timestamp_secret"} ).get('value')

payload ={
"commit": commit,
"authenticity_token": authenticity_token,
"login": "youself_account",
"password": "youself_password",
"webauthn-support": "supported",
"webauthn-iuvpaa-support": "unsupported",
"return_to": return_to,
"allow_signup":"",
"client_id":"", 
"integration":"", 
"required_field_500e":"",
"timestamp":timestamp,
"timestamp_secret": timestamp_secret
}


github_page = request.post('https://github.com/session',data=payload,headers=headers)
print(github_page.status_code)
```
最後可以透過github_page.status_code去觀察登入是否成功,成功的話就會顯示 "200"  

那我們在重新去get登入後的畫面,並在爬出網頁\<p\>底下的文字資,最終code如下:  
```
import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

request = requests.session()
login_page = request.get('https://github.com/login?',headers=headers)


soup = BeautifulSoup(login_page.text,'html.parser')
authenticity_token = soup.find('input', {"name": "authenticity_token"} ).get('value')
commit = soup.find('input', {"name": "commit"} ).get('value')
webauthn_support = soup.find('input', {"name": "webauthn-support"} ).get('value')
return_to = soup.find('input', {"id": "return_to"} ).get('value')
timestamp = soup.find('input', {"name": "timestamp"} ).get('value')
timestamp_secret = soup.find('input', {"name": "timestamp_secret"} ).get('value')

payload ={
"commit": commit,
"authenticity_token": authenticity_token,
"login": "ccs96504@gmail.com",
"password": "0602Love0113",
"webauthn-support": "supported",
"webauthn-iuvpaa-support": "unsupported",
"return_to": return_to,
"allow_signup":"",
"client_id":"", 
"integration":"", 
"required_field_500e":"",
"timestamp":timestamp,
"timestamp_secret": timestamp_secret
}


github_page = request.post('https://github.com/session',data=payload,headers=headers)
print(github_page.status_code)
github_page = request.get('https://github.com/', headers=headers)
soup = BeautifulSoup(github_page.text,'html.parser')
for p in soup.find_all('p'):
    print(p.string) 
```
