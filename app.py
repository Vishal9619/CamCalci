from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import re
import base64

app=Flask(__name__)

@app.route('/')
def my_form():
	return render_template('index.html')

@app.route('/calculate',methods=['POST','GET'])
def camcalci():
	if(request.method=="POST"):
		camimage = request.form['input-id']
		data = camimage[22:]
		camimage = data.encode('ascii')
		#print(camimage)
		# camimg = Image.fromstring('RGB',(150,100),decodestring(camimage))
		target = pytesseract.image_to_string(base64.decodestring(camimage), lang='eng',config='--psm 1000')
		return render_template('index.html',camtext = target)

# @app.route('/login',methods=['POST'])
# def login():
# 	if request.method=='POST':
# 		username=request.form['username']
# 		passwd=request.form['passwd']
# 		return "Welcome: %s"%username

if __name__=="__main__":
	app.debug = True
	app.run(host='0.0.0.0',port=8000)