from flask import Flask, request, redirect
import helper
import validators

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    page = helper.menu
    return page

@app.route('/form')
def form():
    page = helper.menu + helper.form
    return page


@app.route('/form', method=["POST"])
def formSubmission():
    page = helper.menu

    if request.method == "POST":
        page = helper.menu

        username = request.form['username']
        password = request.form['password']
        
        if username == validator.validateUsername(username):
            page += "Form submitted"
            return page
        else:
            #return redirect('/form') --- How the book showed it
            page += helper.form.format(error = validator.validateUsername(username), username ='')
            return redirect(url_for('form'))




app.run()