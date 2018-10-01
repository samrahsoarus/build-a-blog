from flask import Flask, request, redirect
import cgi
import os      # Needed for jinja
import jinja2  # Needed for jinja

# Initialize the jinja2 template engine within Flast application
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# Make a new file system path by joining the location we are currently in with the templates directory
# Name of folder that current file lives in = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
# Loader knows where the files live in the folder system and can fetch and load them into the app's
# memory when we need them... Tell it to load templates from our templates directory
# To HTML escape, use 'autoescape=True'

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    # [return form] ~ Replace with jinja template functionality
    template = jinja_env.get_template('hello_form.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(name=first_name)

app.run()
