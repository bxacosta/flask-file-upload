from flask import Flask, request
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

FILE_EXTENSIONS = ["mp3", "flac"]
UPLOAD_FOLDER = '/home/xavier'


def file_extension(filename):
    return os.path.splitext(filename)[1][1:]


def allowed_file(filename):
    return '.' in filename and file_extension(filename).lower() in FILE_EXTENSIONS


@app.route("/file", methods=['POST'])
def file():
    if "file" not in request.files:
        return "file is required", 400

    file = request.files["file"]

    if file.filename == "":
        return "file not selected", 400

    if file and allowed_file(file.filename):
        filename = "file1.{}".format(file_extension(file.filename))

        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return "file has been saved", 200
    else:
        return "file type is not allowed", 400


if __name__ == "__main__":
    app.run(port=8080)