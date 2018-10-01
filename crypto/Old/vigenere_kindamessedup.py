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
    shiftLetterList = []
    shiftNumberList = []
    originalMessageList = messageList[:]
    
    #Figure out the shift for each letter in the text
    #
    # for i in range(messageLength):
    #     if messageList[i].upper() in alphaz:  
    #         if i >= keyLength:
    #             k = i % keyLength
    #             shiftLetterList.append(keyList[k])
    #         else:
    #             shiftLetterList.append(keyList[i])
    #     else:
    #         shiftLetterList.append("*")
    
    j = 0

    for i in range(messageLength):
        messageLetter = messageList[i]
        if messageLetter.upper() in alphaz:
            if j >= keyLength:
                k = j % keyLength
                letter = keyList[k]
                shift = alphabet_position(keyList[k])
                
            else:
                letter = keyList[j]
                shift = alphabet_position(keyList[j])
            
            messageList[i] = rotate_character(messageLetter, shift)
            shiftNumberList.append(shift)
            shiftLetterList.append(letter)
            # keyLetter = keyList[k]
            # shiftNumberList.append(keyLetter)
        else:
            messageList[i] = messageLetter
            shiftNumberList.append("*")
            shiftLetterList.append("*")
            j = j - 1
        
        j = j + 1
    
    return ''.join(messageList)
    #return [originalMessageList, shiftLetterList, shiftNumberList, messageList]

def main():
    print(encrypt("The crow flies at midnight!", "boom"))
    # print("originalMessageList", theLists[0])
    # print("shiftLettberList", theLists[1])
    # print("shiftNumberList", theLists[2])
    # print("messageList", theLists[3])

    #message = str(input("Type a message: "))
    #rotation = int(input("Rotate by: "))
    #newMessage = encrypt(message, rotation)
    #print(newMessage)

if __name__ == "__main__":
    main()