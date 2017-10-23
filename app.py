#!/usr/bin/python

"""A simple number and datetime addition JSON API.
Run the app:
    $ python examples/flaskrestful_example.py
Try the following with httpie (a cURL-like utility, http://httpie.org):
    $ pip install httpie
    $ http GET :5001/
    $ http GET :5001/ name==Ada
    $ http POST :5001/add x=40 y=2
    $ http POST :5001/dateadd value=1973-04-10 addend=63
    $ http POST :5001/dateadd value=2014-10-23 addend=525600 unit=minutes
"""
import datetime as dt

from flask import Flask, jsonify
from flask_restful import Api, Resource

from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

import multiprocessing
import subprocess

app = Flask(__name__)
api = Api(app)


class IndexResource(Resource):
    """A welcome page."""

    hello_args = {
        'name': fields.Str(missing='Friend')
    }

    @use_args(hello_args)
    def get(self, args):
        return {'message': 'Welcome to clustered jtr, {}!'.format(args['name'])}


class ExecuteApp(Resource):
    """An addition endpoint."""

    app_args = {
        'passwordFile': fields.Str(required=True),
        'config': fields.Str(missing='john.conf'),
        'executionType': fields.Str(missing='simple'),
        'charsetGroup': fields.Str(missing='Al'),
    }

    @use_kwargs(app_args)
    def post(self, passwordFile, config, executionType, charsetGroup):
        """An addition endpoint."""
        #jsonify({'tasks': tasks})
        print subprocess.check_output(['./johnFake.py', '-p', passwordFile, '-c', config, '-t', executionType, '-g', charsetGroup])
        return {'john': passwordFile}

class StatusResource(Resource):
    def post(self):
        return {'john': "running"}

class ResultsResource(Resource):
    def post(self):
        return {'john': "running"}

class AvailableCPUsResource(Resource):
    def post(self):
        return {'cores': multiprocessing.cpu_count()}

# This error handler is necessary for usage with Flask-RESTful
@parser.error_handler
def handle_request_parsing_error(err):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)

if __name__ == '__main__':
    api.add_resource(IndexResource, '/')
    api.add_resource(ExecuteApp, '/john')
    api.add_resource(StatusResource, '/status')
    api.add_resource(ResultsResource, '/results')
    api.add_resource(AvailableCPUsResource, '/resources')
app.run(port=5001, debug=True)
