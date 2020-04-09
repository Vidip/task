from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)


@app.route('/')
def hello():
	print("helo")
	return render_template("home.html")

@app.route('/auth',methods=['POST'])
def auth():
	otp = request.form['auth']
	if otp == 'bemoacad1234':
		return redirect("http://ec2-18-212-51-62.compute-1.amazonaws.com:8000/")
	else:
		message = "Wrong Password"
		return message

if __name__ == '__main__':
    app.run(host="0.0.0.0")