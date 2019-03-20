from flask import Flask, jsonify
from flask_restplus import Resource, Api, reqparse

from asyncio_mongodb_1_5 import Dbfirst
from asyncio_mongodb_6_10 import Dbsecond
from asyncio_mongodb_11_15 import Dbthird
from asyncio_mongodb_16_20 import Dbforth
from asyncio_mongodb_21_25 import Dbfifth

app = Flask(__name__)
api = Api(app, version=1.0, title='Taking Information', description='gathering all info of user')

parser = reqparse.RequestParser()   #it shows how much args we want
parser.add_argument('email', type=str, help='here you can find data behalf of email', required=True)
search1 = api.namespace('searching1', description='for searching domain')
search2 = api.namespace('searching2', description='for searching domain')
search3 = api.namespace('searching3', description='for searching domain')
search4 = api.namespace('searching4', description='for searching domain')
search5 = api.namespace('searching5', description='for searching domain')


@search1.route('/search')
class HelloWorldOne(Resource):
    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args()
        # print(args['email'])
        obj = Dbfirst()
        result = obj.searching1(args['email'])
        return jsonify(result)


@search2.route('/search1')
class HelloWorldTwo(Resource):
    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args()
        obj = Dbsecond()
        result = obj.searching2(args['email'])
        return jsonify(result)


@search3.route('/search2')
class HelloWorldThree(Resource):
    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args()
        obj = Dbthird()
        result = obj.searching3(args['email'])

        return jsonify(result)


@search4.route('/search3')
class HelloWorldFour(Resource):
    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args()
        obj = Dbforth()
        result = obj.searching4(args['email'])
        return jsonify(result)


@search5.route('/search4')
class HelloWorldFive(Resource):
    @api.expect(parser, validate=True)
    def get(self):
        args = parser.parse_args()
        obj = Dbfifth()
        result = obj.searching5(args['email'])
        return jsonify(result)
