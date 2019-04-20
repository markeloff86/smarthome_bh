from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def po():
    return jsonify('test')


if __name__ == '__main__':
    app.run()
