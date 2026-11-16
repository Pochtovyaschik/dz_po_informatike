from urllib import request

from flask import *

from databases import Database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
    else:
        return render_template("LOGIN.html", error = "error")
    try:
        result = db.search()
        for row in result:
            if name != "" and password != "":
                if row[2] == "password":
                    return render_template("diddy.html", person=name)
                else:
                    return render_template("LOGIN.html")
            else:
                return '<p>DIDDY</p>'
    except(ValueError) as e:
        return render_template("LOGIN.html")

@app.route('/diddy')
def diddy():
    return render_template("diddy.html")



if 1 == 1:
    db = Database("localhost", "root", "admin", "academy")
    app.run(host='localhost', port=5000)