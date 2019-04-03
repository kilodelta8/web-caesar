from helpers import alphabet_position, rotate_character


def rot(text, rot):
    codedMessage = ""
    for ch in text:
        #x = rotate_character(ch, rot)
        codedMessage += rotate_character(ch, rot)
    return codedMessage


def main():
    try:
        from sys import argv
        key = argv[1]
        keyTwo = 0

        for x in key:
            if x.isdigit():
                keyTwo = x
            else:
                raise IndexError
    except IndexError:
        print("usage: python caesar.py n")
        exit()

    message = input("Type a message:")
    print(rot(message, int(keyTwo)))



if __name__ == "__main__":
    main()
