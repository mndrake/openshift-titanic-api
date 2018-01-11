"""
basic flask-restplus api example
"""
from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == "__main__":
    app.run()
