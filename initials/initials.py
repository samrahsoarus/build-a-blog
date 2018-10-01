def get_initials(fullname):
    namelist = fullname.split(" ")
    first = namelist[0]
    last = namelist[1]
    firstL = first[:1].upper()
    lastL = last[:1].upper()
    initials = firstL + lastL
    return initials

def main():
    fullname = input("What is your full name? ")
    print(get_initials(fullname))

if __name__ == '__main__':
    #main()
    string1 = 'waleed'
    print dir(string1)
