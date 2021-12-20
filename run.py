import requests
import schedule
from flask import Flask, render_template  # untuk mengakses template

app = Flask(__name__)


def indo():
    api_url = "https://api.kawalcorona.com/indonesia"  # mengirim ke alamat api
    # konversi hasil dari format json ke dictionary
    rstl = requests.get(api_url).json()
    return rstl


r_indo = schedule.every(2).seconds.do(indo)  # update data setiap dua detik
data_indo = indo()


@app.route("/")
def index():
    return render_template("index.html", data_indo=data_indo)


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/kontak")
def kontak():
    return render_template("kontak.html")


@app.route("/profil")
def profil():
    return render_template("profil.html")


@app.route("/berita1")
def berita1():
    return render_template("berita1.html")


@app.route("/berita2")
def berita2():
    return render_template("berita2.html")


@app.route("/berita3")
def berita3():
    return render_template("berita3.html")


@app.route("/berita4")
def berita4():
    return render_template("berita4.html")


@app.route("/berita5")
def berita5():
    return render_template("berita5.html")


@app.route("/berita6")
def berita6():
    return render_template("berita6.html")


@app.route("/berita7")
def berita7():
    return render_template("berita7.html")


@app.route("/berita8")
def berita8():
    return render_template("berita8.html")


if __name__ == "__main__":
    app.run(debug=True)  # penjalanan program
