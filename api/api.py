from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/calculate', methods=['GET', 'POST'])
@cross_origin()
def calculate():
    if request.method == 'POST':
        number = int(request.args.get('number', None))
        if number:
            divList = [i for i in range(1, number + 1) if number % i == 0]
            isPrime = (True if len(divList) == 2 else False)

            return {'divList': divList, 'isPrime': isPrime}
