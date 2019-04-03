def alphabet_position(character):
    if character.isalpha():
        if character.islower():
            return (ord(character) - 97)
        elif character.isupper():
            return (ord(character) - 65)
    else:
        return ord(character)


def rotate_character(character, rot):
    if character == " ":
        return " "
    elif character.islower():
        return chr((ord(character) - 97 + rot) % 26 + 97)
    elif character.isupper():
        return chr((ord(character) - 65 + rot) % 26 + 65)
    elif not character.isalpha():
        return character
           
