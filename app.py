from flask import Flask, redirect, url_for, render_template, request
from wit import Wit
import random


app = Flask(__name__)
app.secret_key = 'my secret and not your secret'
access_token = "HVUC73T6EPFJINGNIO5ECWFTZI55M7JP"
client = Wit(access_token)


@app.route('/')
def index():
    return render_template("index.html", error="")


@app.route('/home', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        expression = request.form['expression']
        response = client.message(expression)
        sentiments = ""
        if bool(response['traits']):
            sentiments = response['traits']['sentiments'][0]['value']
        if sentiments == "":
            return render_template("index.html", error="Sorry! Something went wrong! Please try again with a different phrase.")
        if sentiments == "anger":
            return anger()
        if sentiments == "fearful":
            return fearful()
        if sentiments == "peaceful":
            return peaceful()
        if sentiments == "happy":
            return happy()
        if sentiments == "upset":
            return upset()
        if sentiments == "surprised":
            return surprised()
        if sentiments == "disgusted":
            return disgusted()
        if sentiments == "loved":
            return loved()
    else:
        return redirect(url_for('index'))


def anger():
    with open("quotes/anger.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/anger.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="angry", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def fearful():
    with open("quotes/fearful.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/fearful.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="fearful", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def peaceful():
    with open("quotes/peaceful.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/peaceful.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="peaceful", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def happy():
    with open("quotes/happy.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/happy.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="happy", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def upset():
    with open("quotes/upset.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/upset.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="upset", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def surprised():
    with open("quotes/surprised.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/surprised.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="surprised", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def disgusted():
    with open("quotes/disgusted.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/disgusted.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="disgusted", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


def loved():
    with open("quotes/loved.txt") as fp:
        Lines = fp.readlines()
        Lines = set(Lines)
        quotes = random.sample(Lines, 4)
    list = [quotes[0], quotes[1], quotes[2], quotes[3]]
    list_sorted = sorted(list, key=len)
    with open("videos/loved.txt") as fp:
        avid = fp.readlines()
        video = random.choice(avid)
    return render_template("home.html", mood="loved", quote1=list_sorted[0], quote2=list_sorted[1],
                           quote3=list_sorted[2], quote4=list_sorted[3], video=video)


if __name__ == "__main__":
    app.run()
