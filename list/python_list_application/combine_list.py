
### list data 
TH = ['姓名','學號','國文','英文','數學'] #=> Table Header
TD = [['陳O明','100001','90','95','98'],
      ['王O明','100003','91','90','87'],
      ['吳O明','100005','89','86','89'],
      ['蔡O明','100002','84','91','100'],
    ]


### 單一List 與 多重List 結合為 dict
def singleList_combine_multipleList_to_dict():
    #Make dict Header
    Make_dict_Header = {TH[i]:[] for i in range(len(TH))}
    print(Make_dict_Header)

    #put data in the dict
    data = []
    for j in range(len(TD)):
        data.append({TH[i]: TD[j][i] for i in range(len(TH))})
    print(data)
    return data


### Tuple -> List -> dict

return_data = (['0','123','456','789'], 'Ture')
def asign_to_dict():
      #get_return_data_for_list
      data = return_data[0]
      dict = {id:[data[0],data[i]] for i in range(1,len(data))}
      
      

if __name__=="__main__":
    singleList_combine_multipleList_to_dict()
