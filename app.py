from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return """
	<h1>Flask app!</h1>
	<p>Your Python Flask app is successfully running inside a docker container.</p>
	<p>This page is being served by Flask on port 80</p>
	"""
if __name__ == '__main__':
	print("Starting Flask web server on port 80 ...")
	app.run(host='0.0.0.0', port=80, debug=False)
