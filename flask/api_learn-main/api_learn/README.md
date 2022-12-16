# api_learn

## 1.創建Flask框架
先定義app.py為flask的輸出框架,並使用Flask的模組  
code如下:  
```
from flask import Flask  
app = Flask(__name__)
```
執行後可以看到  

<img src="https://user-images.githubusercontent.com/16216879/194278171-47069b89-a746-44c2-a194-d9b3744d05d7.png" width="80%" height="80%" alt="flask run"/><br/>
## 2.json物件定義
先定義json格式的物件  
code如下:  
```
stores = [  
    {  
    "name":"My Store",  
    "items":[  
        {  
            "name":"Chair",  
            "price":"15.99"  
        }  
    ]  
    }  
]  
```
## 3.使用get方法
get解讀方式為"讀取,獲取"json值的參數  
使用方式"@app.get('[url]')",套在function上後回傳json
```
@app.get('/Store')
def get_store():
    return {"stores":stores}
```
試試看使用postname去撈撈看是否回傳為json資訊
![image](https://user-images.githubusercontent.com/16216879/194278021-3716782f-9f0b-4915-997f-ef32bb850a54.png)

## 4.使用post方法
post解讀方式為"新增,加入"json值的參數  
使用方式"@app.post('[url]')",套在function上後回傳json

```
@app.post('/Store')
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data['name'],"items":[]}
    stores.append(new_store)
    return new_store, 201
```
因post的方式,只有name是透過request_data['name']獲取的值    
而items是沒有透過request_data拿值,而是給他 "[]"  
所以最後return的狀態,如下:  
![image](https://user-images.githubusercontent.com/16216879/194989183-370f1772-ed2a-44c0-be77-d3742e2ff4eb.png)

那我們已經將name的參數post後,再重新get看看,就會獲取到新增的參數  
![image](https://user-images.githubusercontent.com/16216879/195005349-da18f7cb-2beb-415d-843d-3ea2f904f39a.png)
### 延伸用法  
透過url來判斷,參數是否存在  
使用方式"@app.post('[url]/\<string:name>\/item')",套在function(def create_item(name))  
利用url的name來判斷此api是否存在  
```
@app.post('/Store/<string:name>/item')
def create_item(name):
    request_data = request.get_json()
    print(request_data, name)
    
    for store in stores:
        print(store)
        #print(store['name'])
        if store['name'] == name:
            new_list = {"name":request_data['name'],"price":request_data['price']}
            store['items'].append(new_list)
            return new_list, 201
    return {"message":"store is not found"},404
```
