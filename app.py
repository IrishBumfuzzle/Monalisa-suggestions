from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        file = open("suggestions.txt", "a")
        file.write("\n")
        file.write("NOW BEGINS NEW SUGGESTION")
        file.write("\n")
        file.write(request.form.get("suggestions"))
        return render_template("end.html")
