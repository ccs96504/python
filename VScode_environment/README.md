# VScode
## 目錄
## 1. 配置python-虛擬環境配置(venv)


### 1. 配置python-虛擬環境配置(venv)
#### 1.環境配置(For Windows)

第一步：以管理員身份執行powershell  
第二步：執行：get-ExecutionPolicy 回覆Restricted，表示狀態是禁止的。  
第三步：執行：set-ExecutionPolicy RemoteSigned  
第四步：選擇Y，Enter  

![image](https://user-images.githubusercontent.com/16216879/194230657-48da8abd-6a49-49b4-baa3-367dc5be4433.png)

### 2.環境配置(For Windows)
#### 在Vscode環境Terminal使用以下指令  
```
(For Mac) sudo apt-get install python3-venv first   
(Windows) pip install virtualenv  
```
#### macOS/Linux  
```
python3 -m venv .venv  
```
#### Windows  
```
python -m venv .venv  
```
### 3.設定Terminal選擇Interpreter為虛擬環境
Vscode ==> Ctrl+P ==> '>Python: Select Interpreter'  
```
>Python: Select Interpreter
```
 ![image](https://user-images.githubusercontent.com/16216879/194231363-de796190-bb37-44a9-911a-a3a283bc3686.png)

 ![image](https://user-images.githubusercontent.com/16216879/194231350-8bab4bb0-c9c0-4454-9875-10676bf2b05f.png)

選擇後,在將Terminal關閉  

使用Ctrl+J 重新呼叫Terminal,系統會重新呼叫為虛擬環境(venv)
 ![image](https://user-images.githubusercontent.com/16216879/194231371-9d5c0f4b-41fc-4cbf-9e4a-8cecc73eb7e4.png)

#### 存取python當前環境 
```
pip freeze > requirements.txt   
```
