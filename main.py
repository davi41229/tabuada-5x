from flask import render_template, url_for, redirect, request
from app import tabuada, os


@tabuada.route("/")
def home():
    return render_template("index.html")

@tabuada.route("/mult1")
def mult1():
    mult1 = 5 * 0
    resultado = mult1 
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult2")
def mult2():
    mult2 = 5 * 1
    resultado = mult2
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult3")
def mult3():
    mult3 = 5 * 2
    resultado = mult3
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult4")
def mult4():
    mult4 = 5 * 3
    resultado = mult4
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult5")
def mult5():
    mult5 = 5 * 4
    resultado = mult5
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult6")
def mult6():
    mult6 = 5 * 5
    resultado = mult6
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult7")
def mult7():
    mult7 = 5 * 6
    resultado = mult7
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult8")
def mult8():
    mult8 = 5 * 7
    resultado = mult8
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult9")
def mult9():
    mult9 = 5 * 8
    resultado = mult9
    return render_template("index.html", resultado=resultado)

@tabuada.route("/mult10")
def mult10():
    mult10 = 5 * 9
    resultado = mult10
    return render_template("index.html", resultado=resultado)


@tabuada.route("/mult11")
def mult11():
    mult11 = 5 * 10
    resultado = mult11
    return render_template("index.html", resultado=resultado)



if __name__ == "__main__":
    port = int(os.getenv("PORT"), "5000")
    tabuada.run(host="0.0.0.0", port=port)

