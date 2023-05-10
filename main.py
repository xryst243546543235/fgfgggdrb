# This is a sample Python script.
from urllib import request


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template ,request
from random import choice
app = Flask(__name__)
@app.route('/ttt', methods=["POST", "GET"])
def add_post():
    if request.method == "POST":
        print(request.form['password'])
        a=request.form['password']
        return render_template('ttt.html',a=a)
    return render_template('ttt.html')

if __name__ == '__main__':
        app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
