import os

from flask import Flask, render_template, request
from PIL import Image
from werkzeug.utils import secure_filename

import module as md

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = 'static/uploads/'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            result = md.image_processing(image_path)
            print(result)
            return render_template("index.html")
        else:
            return render_template("index.html", error="Silahkan upload gambar dengan format JPG")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
