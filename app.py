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
@app.route('/recipebookIndex')
def recipebookIndex():
	return render_template('recipebookindex.html')

@app.route('/recipes', methods=["GET", "POST"])
def recipes():
	root = os.path.realpath(os.path.dirname(__file__))
	data = os.path.join(root, 'data', 'meatrecipes.json')
	recipes = json.load(open(data))

	if request.method == "POST":
		if 'delete' in request.form:
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
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']
			return updatePage(entryname, entryinstr, entryingr, entrynumber)
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
			entry['name'] = request.form['name']
			entry['ingr'] = request.form['ingr']
			entry['instr'] = request.form['instr']
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('recipes'))

	else:
		return render_template("recipes.html", recipebook=recipes, type="Meat")

@app.route('/souprecipes', methods=["GET", "POST"])
def soupRecipes():
	root = os.path.realpath(os.path.dirname(__file__))
	data = os.path.join(root, 'data', 'souprecipes.json')
	recipes = json.load(open(data))

	if request.method == "POST":
		if 'delete' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'souprecipes.json')

			olddata = json.load(open(data))
			del olddata[int(request.form['delete'])]
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('souprecipes'))
		elif 'update' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'souprecipes.json')

			olddata = json.load(open(data))
			entry = olddata[int(request.form['update'])]
			entrynumber = int(request.form['update'])
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']
			return updatePage(entryname, entryinstr, entryingr, entrynumber)
		elif 'name' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'souprecipes.json')

			olddata = json.load(open(data))
			entrynumber = int(request.form['entrynumber'])
			entry = olddata[entrynumber]
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']

			newname = request.form['name']
			newingr = request.form['ingr']
			newinstr = request.form['instr']
			entry['name'] = request.form['name']
			entry['ingr'] = request.form['ingr']
			entry['instr'] = request.form['instr']
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('souprecipes'))

	else:
		return render_template("recipes.html", recipebook=recipes, type="Soups")

@app.route('/vegetarianrecipes', methods=["GET", "POST"])
def vegetarianRecipes():
	root = os.path.realpath(os.path.dirname(__file__))
	data = os.path.join(root, 'data', 'vegetarianrecipes.json')
	recipes = json.load(open(data))

	if request.method == "POST":
		if 'delete' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'vegetarianrecipes.json')

			olddata = json.load(open(data))
			del olddata[int(request.form['delete'])]
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('vegetarianRecipes'))
		elif 'update' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'vegetarianrecipes.json')

			olddata = json.load(open(data))
			entry = olddata[int(request.form['update'])]
			entrynumber = int(request.form['update'])
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']
			return updatePage(entryname, entryinstr, entryingr, entrynumber)
		elif 'name' in request.form:
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'vegetarianrecipes.json')

			olddata = json.load(open(data))
			entrynumber = int(request.form['entrynumber'])
			entry = olddata[entrynumber]
			entryname = entry['name']
			entryinstr = entry['instr']
			entryingr = entry['ingr']

			newname = request.form['name']
			newingr = request.form['ingr']
			newinstr = request.form['instr']
			entry['name'] = request.form['name']
			entry['ingr'] = request.form['ingr']
			entry['instr'] = request.form['instr']
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('vegetarianRecipes'))

	else:
		return render_template("recipes.html", recipebook=recipes, type="Vegetarian")

@app.route('/updateentry', methods=["GET", "POST"])
def updatePage(entryname, entryinstr, entryingr, entrynumber):
	return render_template("updatepage.html", entryname=entryname, entryingr=entryingr, entryinstr=entryinstr, entrynumber=entrynumber)

@app.route('/newrecipe', methods=["GET", "POST"])
def newRecipe():
	if request.method == "POST":
		nameVar = request.form['name']
		ingrVar = request.form['ingr']
		instrVar = request.form['instr']
		recipeType = request.form['recipeType']
		newList = dict(ingr=ingrVar, instr=instrVar, name=nameVar)

		if recipeType == "meat":
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'meatrecipes.json')

			olddata = json.load(open(data))
			olddata.append(newList)
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('recipes'))
		elif recipeType == "soup":
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'souprecipes.json')

			olddata = json.load(open(data))
			olddata.append(newList)
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('soupRecipes'))
		elif recipeType == "vegetarian":
			root = os.path.realpath(os.path.dirname(__file__))
			data = os.path.join(root, 'data', 'vegetarianrecipes.json')

			olddata = json.load(open(data))
			olddata.append(newList)
			with open(data, 'w') as f:
				json.dump(olddata, f)
			return redirect(url_for('vegetarianRecipes'))
	else:
		return render_template("newrecipe.html")

#Debug
if __name__ == '__main__':
	app.run(debug=True)