from wsgiref import simple_server
from flask import Flask, Response, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from logistic_deploy import predObj
import pickle
import json

app = Flask(__name__, template_folder='template')  # initialize a flask app
CORS(app)
app.config['DEBUG'] = True


class ClientApi:
    def __init__(self):
        self.predObj = predObj()


@app.route('/', methods=['GET'])  # route to display the home
@cross_origin()
def homePage():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])  # route to display the home page
def predictRoute():
    if request.method == 'POST':
        try:
            data = request.form
            print('data is:', data)
            # node = data['bmi']
            #  print(str(node))
            pred = predObj()
            res = pred.predict_log(data)

            print('result is', res)
            # return Response(res)
            return render_template('results.html', prediction=res)

        except ValueError:
            return Response("Value not found")
        except Exception as e:
            print('exception is', e)
            # return Response(e)
            return render_template('index.html')


if __name__ == "__main__":
    clntApp = ClientApi()
    #host = '0.0.0.0'
    #port = 5000
    app.run(debug=True)
    # app.run(debug=True)
