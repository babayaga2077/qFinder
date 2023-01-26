from app import app
from app.modules import *
from flask import request, render_template, session, redirect,flash
from s2t import speech2text
from face_recognition_compare import compare_face
import os
import socket
import time

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/ai")
def ai():
	y = session.get('LoggedIn', False)
	if not y:
		return redirect('index')
	return render_template('ai.html')

@app.route('/upload', methods=['POST'])
def upload():
	y = session.get('LoggedIn', False)
	if not y:
		return redirect('index')
	if request.method == 'POST':
		if 'audio_data' not in request.files:
			return 'No file part'
		file = request.files['audio_data']
		if file.filename == '':
			return 'No selected file'
		if file:
			filename = "wav_"+str(int(time.time()))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			output=speech2text(app.config['UPLOAD_FOLDER']+filename)
			if output[1]==1:
				query_res=GetQuote(output[0])
				if not isinstance(query_res, str):
					res="<h1><span style=\"color:#0f457f\">Our understanding of your input is : </span></h1><p>"+output[0]+"</p><h1><span style=\"color:#0f457f\">Query result : </span></h1>"
					if len(query_res) > 100:
						res+='<h1>Too many matches, returning the last 100 search results: </h1>'
					for x in query_res[-100:]:
						quote=x[0]
						author=x[1]
						res+="<dev class='quote'><p>"+quote+"</p><p>"+author+"</p></dev>"
				else:
					res="<h1><span style=\"color:#0f457f\">Our understanding of your input is : </span></h1><p>"+output[0]+"</p><h1><span style=\"color:#0f457f\">Query result : </span></h1><p>"+query_res+"</p>"
			else:
				res="<p>"+output[0]+"</p>"
			return res
	
@app.route('/login', methods=['POST','GET'])
def login():

	y = session.get('LoggedIn', False)
	if request.method == 'POST' and not y:
		if 'img_data' not in request.files:
			return 'No file part'
		file = request.files['img_data']
		if file.filename == '':
			return 'No selected file'
		if file:
			filename = "img_"+str(int(time.time()))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			res=compare_face(app.config['UPLOAD_FOLDER']+filename,5)
			os.remove(filename)
			if not (res['face_found_in_image']):
				return "Sorry, can't recognize face in image. Try again!"
			elif not (res['is_picture_of_admin']):
				return "Not admin picture. Try again!"
			else:
				session['LoggedIn'] = True
				return "True"
	else:
		if y:
			return redirect('index')
		return render_template('login.html')

@app.route('/logout')		
def logout():
	session.clear()
	return redirect('index')	