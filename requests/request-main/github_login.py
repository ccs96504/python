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
github_page = request.get('https://github.com/', headers=headers)
soup = BeautifulSoup(github_page.text,'html.parser')



data = soup.prettify()
authenticity_token = soup.find('form', {"action":"/users/ccs96504/profile_readme"} )
authenticity_token = authenticity_token.find('input',{"name":"authenticity_token"}).get('value')
payload ={"authenticity_token":authenticity_token}
##profile README 需要使用Post方法##
github_page = request.post('https://github.com/users/ccs96504/profile_readme',data=payload,headers=headers)
print(github_page.status_code)
soup = BeautifulSoup(github_page.text,'html.parser')
abc = soup.prettify()
for p in soup.find_all('p'):
    print(p.string) 


