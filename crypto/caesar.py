from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    textList = list(text)
    for i in range(len(textList)):
        textList[i] = rotate_character(textList[i], rot)
    return ''.join(textList)

def main():
    from sys import argv, exit

    if argv[1].isdigit():
        message = str(input("Type a message: "))
        rotation = int(argv[1])
        newMessage = encrypt(message, rotation)
        print(newMessage)
    else:
        exit()

if __name__ == "__main__":
    main()