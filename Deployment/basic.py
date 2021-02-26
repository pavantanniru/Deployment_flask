
from flask import Flask,redirect,url_for,request,render_template
import pickle
import joblib
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def fun():
    return render_template('index.html')

@app.route('/result',methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/api_request',methods=['POST','GET'])

def api_req():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)






if __name__ == '__main__':
   app.run(debug=True)
