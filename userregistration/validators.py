def validateUsername(username):
    
    if username == "": or  or len(username) > 5:
        return "Username is empty!"
    if " " in username:
        return "No spaces allowed!"
    if not username.isalpha():
        return "Letters only!"
    if len(username) > 5:
        return "Up to 5 characters only!"
    
    return True
    