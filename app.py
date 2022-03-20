from flask import Flask, render_template, json
import codecs

#test

app = Flask(__name__)


with codecs.open("static/data/movies.json", "r", encoding="utf-8") as moviesFile:
    data = moviesFile.read();


@app.route('/')
def homePage():  # put application's code here
    return render_template("Intro.html", MOVIES=data)


@app.route('/Movie_Page.html')
def moviesPage():
    return render_template("Movie_Page.html", MOVIES=data)


@app.route('/Actors_Page.html')
def actorsPage():
    return render_template("Actors_Page.html", MOVIES=data)


if __name__ == '__main__':
    app.run()
