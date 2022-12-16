from flask import Flask,request
app = Flask(__name__)

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

@app.get('/Store')
def get_stores():
    return {"stores":stores}

@app.post('/Store')
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data['name'],"items":[]}
    stores.append(new_store)

    return new_store, 201


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
