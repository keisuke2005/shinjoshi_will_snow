from flask import Flask,render_template,request,redirect,Markup
from models.IrisType import IrisType
from models.WillSnow import WillSnow

app=Flask(__name__)

@app.route('/')
def login_get():
	return render_template('login.html')

@app.route('/',methods=["POST"])
def login_post():
	username = "admin"
	password = "admin123"

	un = request.form["username"]
	pw = request.form["password"]
	if un != username or pw != password :
		msg = "ユーザ名またはパスワードが違います"
		return render_template('login.html', username = un, password = pw, message = msg)

	return redirect('/main')

@app.route('/main')
def main_get():
	return render_template('index.html',form=Markup(globals()[get_inference()].form()))

@app.route('/main',methods=["POST"])
def result():
	inference = globals()[get_inference()]
	result = inference.drive(inference(request))
	return render_template('result.html',result=result)
	
@app.route('/signup')
def signup_get():
	return render_template('signup.html')
	
@app.route('/signup',methods=["POST"])
def signup_post():
	return redirect('/main')

def get_inference():
	return 'WillSnow'

if __name__ == '__main__':
	app.run(debug=True)


