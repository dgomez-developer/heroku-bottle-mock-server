import os
import json
from bottle import route, run, template, request, BaseResponse, response

@route('/exercise4/people')
def getPeople():
    return open('exercise4/people.json')

@route('/exercise4/menu')
def getMenu():
    response.headers['Content-Type'] = 'xml/application'
    return open('exercise4/menu.xml')

run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
