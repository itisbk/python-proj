# -*- coding: utf-8 -*-

from webapp import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello world'
