def alphabet_position(letter):
    alphaz = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    upperLetter = letter.upper()
    return alphaz.index(upperLetter)

def rotate_character(char, rot):
    alphaz = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    try:
        ogPosition = alphabet_position(char)
        newPosition = ogPosition + rot
        if newPosition >= 26:
            newPosition = newPosition % 26
        if char.upper() == char:
            newChar = alphaz[newPosition]
        else:
            newChar = alphaz[newPosition].lower()
    except:
        newChar = char
    return newChar

def encrypt(text, rot):
    textList = list(text)
    for i in range(len(textList)):
        textList[i] = rotate_character(textList[i], rot)
    return ''.join(textList)

def main():
    message = str(input("Type a message: "))
    rotation = int(input("Rotate by: "))
    newMessage = encrypt(message, rotation)
    print(newMessage)

if __name__ == "__main__":
    main()