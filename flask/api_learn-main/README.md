# api 學習筆記
## 目錄
- [json](#head1)
	- [1.關於josn data  ](#head2)
	- [2.Json格式說明  ](#head3)
	
# <span id="head1">json </span>
## <span id="head2">1.關於json data  </span>
格式參考:  
![test](https://user-images.githubusercontent.com/16216879/194221691-4830cfae-25a9-4c0e-b468-9c98c9b089fc.png)  

## <span id="head3">2.Json格式說明  </span>

使用 josn格式只能是List,或是物件 , 並透過"{" , "}" 儲存參數,並且透過 ":" 來定義Key值參數,如下:  
 * example: 
>json = [{'Key值':'參數'(可以是字串,數字,浮點數)}]  

可以擁有多Key值,需要透過 "," 來區隔,如下:  
 * example:  
>json = [{'Key1':'參數1',  
>'Key2':'參數2',  
>'Key3':'參數3'}]  

一個Key值可以,擁有多個參數,需要使用 "[]" , "," 來分隔參數,像是List的格式,如下  
 * example:  
>json = [{'Key1':['參數1','參數2','參數3'] }]  

補充說明:josn與dict的差異, json是屬於String, dict則是dict  

