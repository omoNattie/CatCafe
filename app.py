from crypt import methods
import catboys as catboy
import nekos as catgirl
import os
import requests
from pathlib import Path
from flask import Flask, render_template, request, url_for, redirect

FOLDER = os.path.join('static', 'cats')

catboy_url = catboy.img()
catboy_data = requests.get(catboy_url)
open("catboy.jpg", "wb").write(catboy_data.content)
Path("catboy.jpg").rename("./static/cats/catboy.jpg")

catgirl_url = catgirl.img("neko")
catgirl_data = requests.get(catgirl_url)
open("catgirl.jpg", "wb").write(catgirl_data.content)
Path("catgirl.jpg").rename("./static/cats/catgirl.jpg")

avatar_url = catgirl.img("avatar")
avatar_data = requests.get(avatar_url)
open("avatar.jpg", "wb").write(avatar_data.content)
Path("avatar.jpg").rename("./static/cats/avatar.jpg")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER


@app.errorhandler(404)
def bad_request(e):
    return redirect(url_for('error'))

@app.route('/')
def main():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/catboys', methods=['GET', 'POST'])
def catboys():
    full_catboy_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'catboy.jpg')
    print(request.method)

    if request.method == 'POST':
        if request.form.get('NewCat') == 'More CatBoys!':
            catboy_url = catboy.img()
            print(catboy_url)
            catboy_data = requests.get(catboy_url)
            open("catboy.jpg", "wb").write(catboy_data.content)
            Path("catboy.jpg").rename("./static/cats/catboy.jpg")
        else:
            return render_template("home.html")

    return render_template("catboys.html", catboy_image=full_catboy_filename)


@app.route('/catgirls', methods=['GET', 'POST'])
def catgirls():
    full_catgirl_filename = os.path.join(app.config['UPLOAD_FOLDER'], "catgirl.jpg")

    if request.method == 'POST':
        if request.form.get('NewCatG') == 'More CatGirls!':
            catgirl_url = catgirl.img("neko")
            catgirl_data = requests.get(catgirl_url)
            open("catgirl.jpg", "wb").write(catgirl_data.content)
            Path("catgirl.jpg").rename("./static/cats/catgirl.jpg")
        else:
            return render_template("home.html")

    return render_template("catgirls.html", catgirl_image=full_catgirl_filename)


@app.route('/avatars', methods=["GET", "POST"])
def avatars():
    full_avatar_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'avatar.jpg')

    if request.method == 'POST':
        if request.form.get('NewAvatar') == 'More Avatars!':
            avatar_url = catgirl.img("avatar")
            avatar_data = requests.get(avatar_url)
            open("avatar.jpg", "wb").write(avatar_data.content)
            Path("avatar.jpg").rename("./static/cats/avatar.jpg")
        else:
            return render_template("home.html")

    return render_template('avatars.html', avatar_image=full_avatar_filename)

@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
