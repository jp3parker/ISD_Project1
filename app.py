from flask import Flask, render_template, json
import codecs

#test

app = Flask(__name__)

with codecs.open("static/data/movies.json", "r", encoding="utf-8") as moviesFile:
    data = moviesFile.read();


@app.route('/')
def page_example():  # put application's code here
    return render_template("Intro.html")


@app.route('/Movie_Page.html')
def page_2():
    return render_template("Movie_Page.html", MOVIES=data)


@app.route('/Actors_Page.html')
def page_3():
    return render_template("Actors_Page.html")


if __name__ == '__main__':
    app.run()
