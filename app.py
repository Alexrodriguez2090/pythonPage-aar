from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/contactparsing')
def contactparsing():
	return render_template('contactparsing.html')

if __name__ == '__main__':
	app.run(debug=True)