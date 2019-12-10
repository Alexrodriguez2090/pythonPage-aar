import os
from flask import Flask, render_template, url_for, jsonify, request, make_response, json, redirect
import sys

app = Flask(__name__)

#Index
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

#Recreating mustang
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

#Recipe websites
@app.route('/recipes', methods=["GET", "POST"])
def recipes():
	root = os.path.realpath(os.path.dirname(__file__))
	data = os.path.join(root, 'data', 'meatrecipes.json')
	recipes = json.load(open(data))

	if request.method == "POST":
		if "delete" in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'meatrecipes.json')

			olddata = json.load(open(data))
			del olddata[int(request.form['delete'])]
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('recipes'))
		elif 'update' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'meatrecipes.json')

			olddata = json.load(open(data))
			entry = olddata[int(request.form['update'])]
			entrynumber = int(request.form['update'])
			#print(entry, file=sys.stderr)
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']
			done = 0
			#with open(data, 'w') as f:
				#json.dump(olddata, f)
			return updatePage(entryname, entryinstr, entryingr, entrynumber, done)
		elif 'name' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'meatrecipes.json')

			olddata = json.load(open(data))
			entrynumber = int(request.form['entrynumber'])
			entry = olddata[entrynumber]
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']

			newname = request.form['name']
			newingr = request.form['ingr']
			newinstr = request.form['instr']
			entryname = newname
		#entryinstr = entry['instr']
		#entryingr = entry['ingr']
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('recipes'))

	else:
		return render_template("recipes.html", recipebook=recipes, type="Home")

@app.route('/updateentry', methods=["GET", "POST"])
def updatePage(entryname, entryinstr, entryingr, entrynumber, done):
	print(entryname, file=sys.stderr)
	if request.method == "POST" and done == 1:
		root = os.path.realpath(os.path.dirname(__file__))
		data = os.path.join(root, 'data', 'meatrecipes.json')

		olddata = json.load(open(data))
		entry = olddata[entrynumber]
		entryname = entry['name']
		entryinstr = entry['instr']
		entryingr = entry['ingr']

		newname = request.form['name']
		newingr = request.form['ingr']
		newinstr = request.form['instr']
		entryname = newname
	#entryinstr = entry['instr']
	#entryingr = entry['ingr']
		with open(data, 'w') as f:
			json.dump(olddata, f)
		return redirect(url_for('recipes'))
	else:
		return render_template("updatepage.html", entryname=entryname, entryingr=entryingr, entryinstr=entryinstr, entrynumber=entrynumber)

#Debug
if __name__ == '__main__':
	app.run(debug=True)