from flask import render_template, send_from_directory
from app import app 

def navbar():
	nav= []
	for item in ['about','work','fun1','fun2']:
		name = ".%s" % item
		nav.append({'name':name,'url':item})
	
	return nav 

@app.route('/static/fonts/<path:path>')
def serve(path):
	print("-> static file: %s" % path)
	return send_from_directory('static','fonts/'+path)

@app.route('/')
def home():
	return render_template("index.html",nav=navbar())

@app.route('/about')
def about():
	return render_template("about.html",nav=navbar())


@app.route('/work')
def work():
	return render_template("work.html",nav=navbar())

@app.route('/fun1')
def fun1():
	return render_template("fun1.html",nav=navbar())

@app.route('/fun2')
def fun2():
	return render_template("fun2.html",nav=navbar())







