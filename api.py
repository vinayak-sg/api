from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Test(Resource):
	def __init__(self):
		self.testk = request.headers["testkey"]

	def get(self):
		return {'Flask RestFul api': 'Recommender API for Heka Smart Home'}


	def post(self):
		return {
				"status" : self.testk,
				}



api.add_resource(Test, '/')

if __name__ == '__main__':
	app.run(
			host="0.0.0.0",
			port=5000,
			debug=True
			)  
