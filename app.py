from flask import Flask, flash, jsonify, redirect, render_template, request, session
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
file_no = 0
app.config['UPLOAD_FOLDER'] = "photos"

@app.route("/", methods=['GET', 'POST'])
def index():
    global file_no
    if request.method == "GET":
        return render_template("index.html")
    else:
        file = open("suggestions.txt", "a")
        if 'file' in request.files:
            images = []
            uploaded_file = request.files.getlist('file')
            for fil in uploaded_file:
                extension = os.path.splitext(fil.filename)[1]
                fil.save(os.path.join(app.config['UPLOAD_FOLDER'], str(file_no) + extension))
                images.append(file_no)
                file_no += 1
            file.write("\nNOW BEGINS NEW SUGGESTION, IMAGES: " + str(images) + "\n")
        file.write(request.form.get("suggestions"))
        file.close()
        return render_template("end.html")
