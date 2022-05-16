from app import myobj_
from flask import Flask, render_template, flash, redirect, url_for, request

@myobj_.route("/", methods = ['GET', 'POST']) #Utilized the same routes.py methods as our website
def main():
    name = "George"
    city_names = ["Paris", "London", "Rome", "Tahiti"]

    if request.method == 'POST':
        flash(request.form['cityForm'])
        return redirect(url_for('main'))
    return render_template("home.html", name = name, city_names = city_names)