import os
from flask import Flask, render_template, url_for, jsonify, request, make_response, json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/contactparsing')
def contactparsing():
	return render_template('contactparsing.html')

@app.route('/getData', methods=['GET', 'POST'])
def getData():
	root = os.path.realpath(os.path.dirname(__file__))

	data = os.path.join(root, 'data', 'contacts.json')
	contacts = json.load(open(data))
	return jsonify(contacts)

@app.route('/postData', methods=["GET", "POST"])
def postData():
	root = os.path.realpath(os.path.dirname(__file__))
	jsdata = request.get_json()

	data = os.path.join(root, 'data', 'contacts.json')
	with open(data, 'w') as f:
		json.dump(jsdata, f)
	return print("Contacts saved")

if __name__ == '__main__':
	app.run(debug=True)