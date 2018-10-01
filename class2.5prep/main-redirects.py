from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'

# Global variable called 'time_form'
time_form = """
    <style>
        .error {{ color:red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}'/>
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}'/>
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate"/>
    </form>
    """
@app.route('/validate-time')
def display_time_form():
# Request handler to display form + error messages after user has submitted form
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')

def is_integer(num):
# Takes in string and returns T/F if that value that be converted into an integer
    try:
        int(num)
        return True
    except ValueError: # If valueError happens within 'try' block
        return False


@app.route('/validate-time', methods=['POST'])
def validate_time():
# Get data out of request that user submitted by submitting the form
    hours = request.form['hours'] 
    minutes = request.form['minutes']
    # Syntax to get value of these fields out of flask request object (include Flast request import)

    hours_error = ''
    minutes_error = ''
    # Initialize if empty and if after validation they remain empty, that means there are no errors

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
        # If it doesn't validate, then wipe out the variable (='')                                                            
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''
   
    if not is_integer(minutes):
        minutes_error: 'Not a valid integer'
        minutes = ''
    else: 
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''
        
    if not minutes_error and not hours_error: # Only true if both error strings are empty
        time = str(hours) + ':' + str(minutes)
        #return redirect('/valid-time') ~ [Redirect to a different page of application instead of "Success message"]
        return redirect('/valid-time?time={0}'.format(time)) # Use index-based formatting string
        # To give the actual time, pass that info via a query parameter, query-string being generated for redirect location

    else:
    # Redisplay form with the error messages    
        return time_form.format(hours_error = hours_error, minutes_error = minutes_error, # Pass in the error messages 
            hours = hours, minutes = minutes) # Valid value stays in place b/c invalid = ''

@app.route('/valid-time') # Use to respond when we know we have a valid time
def valid_time():
    # Handle query string at redirect location
    time = request.args.get('time') # Get query parameters out of requests using this...
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)

app.run()