menu = """
<ul>
    <li> <a href="/"> Home </a> </li>
    <li> <a href="/form"> Form </a> </li>
</ul>
<hr>
"""

# Username input, that accepts only 5 characters and no integers

form = """
    {error}<br>
    <form action="/form_submit" method="post">
        <label for="username"> Username: </label>
        <input id="username" type="text" name="username" placeholder=" Choose a username">
        
        <br>
        
        <label for="password"> Password: </label>
        <input id="password" type="text" name="password" placeholder=" Choose a password">

        <br>

        <button type="submit">
            Submit form
        </button>
        <button type="reset"> Erase Form </button>
    </form>