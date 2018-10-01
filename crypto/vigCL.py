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

def encrypt(message, key):
    alphaz = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    messageList = list(message)
    keyList = list(key)
    messageLength = len(messageList)
    keyLength = len(keyList)
    j = 0
    for i in range(messageLength):
        messageLetter = messageList[i]
        if messageLetter.upper() in alphaz:
            if j >= keyLength:
                k = j % keyLength
                shift = alphabet_position(keyList[k])
                
            else:
                shift = alphabet_position(keyList[j])
            messageList[i] = rotate_character(messageLetter, shift)
        else:
            messageList[i] = messageLetter
            j = j - 1
        j = j + 1
    return ''.join(messageList)

def lettersOnly(entry):
    alphaz = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    entryList = list(entry)
    entryLength = len(entryList)
    for i in range(entryLength):
        entryLetter = entryList[i]
        if entryLetter.upper() in alphaz:
            answer = True
        else:
            answer = False
    return answer

def main():
    from sys import argv, exit
    theKey = argv[1]
    if lettersOnly(theKey) == True:
        thePhrase = str(input("Type a message: "))
        newMessage = encrypt(thePhrase, theKey)
        print(newMessage)
    else:
        print("usage: python vigenere.py keyword")
        print("Arguments:")
        print("-keyword : The string to be used as a 'key' to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.")
        exit()

if __name__ == "__main__":
    main()