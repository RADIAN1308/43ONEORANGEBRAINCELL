from flask import Flask, request
import model as m
import json
import numpy as np

#encoder for convertion from np_float32
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.float32):
            return float(obj)
        return super().default(obj)


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    input_data = request.json
    prediction = m.search_funds(input_data,top_k=4)#fuction call to ai
    json_list = json.dumps(prediction,cls=NumpyEncoder)#to jsonify list
    return json_list

#main
if __name__ == '__main__':
    print(type(m.search_funds("sample",top_k=3)))
    app.run(host='0.0.0.0', port=5000)
#first run this and run localserver
#then portforward local server using ngrok : ngrok http 5000
#then use curl on other pc using the given ngrok url to use the api call

