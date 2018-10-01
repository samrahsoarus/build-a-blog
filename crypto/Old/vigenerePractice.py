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
    shiftNumberList = []
    originalMessageList = messageList[:]
    
    j = 0

    for i in range(messageLength):
        messageLetter = messageList[i]
        if messageLetter.upper() in alphaz:
            if j > keyLength:
                k = j % keyLength
                # shift = alphabet_position(keyList[k])
                shift = keyList[k]
            else:
                # shift = alphabet_position((keyList[j]))
                shift = keyList[j]
            messageList[i] = rotate_character(messageLetter, shift)
            shiftNumberList.append(shift)
        else:
            messageList[i] = messageLetter
            shiftNumberList.append("*")
        j += 1
    
    #return ''.join(messageList)
    return [originalMessageList, shiftNumberList, messageList]

def main():
    theLists = encrypt("The crow flies at midnight!", "boom")
    print("originalMessageList", theLists[0])
    print("shiftNumberList", theLists[1])
    print("messageList", theLists[2])

    #message = str(input("Type a message: "))
    #rotation = int(input("Rotate by: "))
    #newMessage = encrypt(message, rotation)
    #print(newMessage)

if __name__ == "__main__":
    main()