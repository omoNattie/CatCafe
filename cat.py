import os
import catboys as catboy
import requests
from pathlib import Path
from flask import Flask, render_template, request

FOLDER = os.path.join('static', 'cat_boys')

url = catboy.img()
img_data = requests.get(url)
open("catboy.jpg", "wb").write(img_data.content)
Path("catboy.jpg").rename("./static/cat_boys/catboy.jpg")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'catboy.jpg')
    print(request.method)

    if request.method == 'POST':
        if request.form.get('NewCat') == 'NewCat':
            url = catboy.img()
            print(url)
            img_data = requests.get(url)
            open("catboy.jpg", "wb").write(img_data.content)
            Path("catboy.jpg").rename("./static/cat_boys/catboy.jpg")
        else:
            return "no"
    elif request.method == 'GET':
        print(" ")

    return render_template("index.html", owo_image=full_filename)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
