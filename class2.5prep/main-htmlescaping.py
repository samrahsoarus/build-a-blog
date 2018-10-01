from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """ 
<!doctype html>
<html>
    <body>
        <!–– form action="/hello" | This defaults to GET request, below is version for POST––>
        
        <form action="/hello" method="post">             
        <!––Submit form / send form data to a particular URL––>
        
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name"/>
            <input type="submit"/>
        
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name'] # Dictionary type object so use []
    return '<h1> Hello, ' + cgi.escape(first_name) + '</h1>'
    # Want to prevent users from adding html or javascript into the form box
    # 'Escape' = Turn HTML markup entered into form into other string characters that are not HTML
app.run()
