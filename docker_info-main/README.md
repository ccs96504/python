# docker_info

## dockerfile用法
如果一個程式開發完成,需要將程式打包成docker,減少後續部屬上的麻煩,  
我們可以先建置將環境部屬起來,以下程式都會透過python去解釋  
### 獲取python requirements.txt
建議先在python使用新veun的虛擬環境建置完成並且可以使用,以免造成安裝多的不必要的modiles  
可以參考我這篇 [VSCode配置](https://github.com/ccs96504/VScode "link")  
```
pip freeze > requirements.txt 
```
### 撰寫dockerfile
先將dockerfile撰寫出來,配置如下:
```
# 建置最基礎的image也就是python3.8.10
FROM python:3.8.10

# 定義當前的目錄位置
WORKDIR /api_learn

#將資料夾檔案複製到/api_learn底下
COPY . /api_learn

#到contain底下執行 pip install -r requirements.txt
RUN pip install -r requirements.txt

# 環境部屬完成後,直接執行python app.py
CMD ["python","app.py"]
```
### docker create images
透過docker指令來build images環境
```
docker image build -t [image名稱] [打包程式位置]  
docker image build -t docker_app D:\docker_base\.
```
### 執行container
```
#docker run -d -p 80:8888 --name [docker可以自己定義] [image名稱]
docker run -d -p 5000:5000 --name test_app  docker_app
```
然後我們可以到(本機)127.0.0.1:5000/index,index的是根據code內容為主  
![image](https://user-images.githubusercontent.com/16216879/197478078-d6ec702f-7d3d-43ae-9aca-c446a87d4c23.png)

### 上傳更新至dockerhub
我們到dockerhub登入自己的docker帳密,
然後Create repository,屬於自己的dockerhub

![image](https://user-images.githubusercontent.com/16216879/197479777-1945f84e-76a4-483e-a455-3f76b5eee3bd.png)

我們將它命名test,描述可以隨意寫,我簡單寫個 test dockerhub
![image](https://user-images.githubusercontent.com/16216879/197480285-b9989527-bce0-4dcb-b1f7-4aafabc30d8f.png)

圖片有告知怎麼push新的images到dockerhub,那我等等按照圖片去操作
![image](https://user-images.githubusercontent.com/16216879/197480571-c601671b-e99e-4f00-9211-830855dad212.png)

先check docker images
```
docker images
```
![image](https://user-images.githubusercontent.com/16216879/197481017-e8ad6b44-574f-47e4-883f-d1ff8e253aef.png)

製作一個新的tag版本要上傳至dockerhub使用
```
docker tag SOURCE_IMAGE[:TAG]/ContainerID  TARGET_IMAGE[:TAG](dockerhub的路徑)
docker tag  4fa61db2a248 yuzhu0113/test:1.1.0
```
![image](https://user-images.githubusercontent.com/16216879/197483141-43a88270-8725-454d-8b09-26503cba573d.png)

將docker image push 到dockerhub上
```
docker push TARGET_IMAGE[:TAG](dockerhub的路徑)
docker push yuzhu0113/test:1.1.0
```
等待他部署~  
![image](https://user-images.githubusercontent.com/16216879/197484525-11876edc-8060-4d22-be4e-bdce9ec76ff5.png)  
最後在dockerhub就可以看到部屬的images  
![image](https://user-images.githubusercontent.com/16216879/197484501-ca7d1633-a2b0-49e9-aa92-e1087ac5de40.png)

然後我們將image空清,直接透過dockerhub直接部屬在自己本機環境
```
docker run -d -p 5000:5000 --name test_app  yuzhu0113/test:1.1.0
```
![image](https://user-images.githubusercontent.com/16216879/197485560-93f4afde-68d1-4919-be58-23e55162bf31.png)
查看contain有沒有部屬成功
```
docker ps -a
```
![image](https://user-images.githubusercontent.com/16216879/197485749-6b60cc29-63a0-4647-b345-5f361ea576be.png)
成功後,可以看到利用dockerhub直接部屬了
![image](https://user-images.githubusercontent.com/16216879/197485880-c0fbc3bf-7944-4249-bfd7-bbb93a4b904b.png)

