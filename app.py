from distutils.log import debug
from flask import Flask
import json

app = Flask(__name__)
books = []
@app.route('/libro', methods=['POST'])
def libro():
    books.append({"a":"b"})
    return {'msg': 'este es un libro'}

@app.route('/libro', methods=['GET'])
def persona():
    return json.dumps(books)

if __name__ == '__main__':
    app.run(debug = True)