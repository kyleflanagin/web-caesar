def alphabet_position(letter):
    if (ord(letter) >= 97) and (ord(letter) <= 122): # lowercase
        return ord(letter)-97
    elif (ord(letter) >= 65) and (ord(letter) <= 90): # uppercase
        return ord(letter)-65
    else:
        pass


def rotate_character(char,rot):
    if (ord(char) >= 97) and (ord(char) <= 122): # lowercase
        return chr(97+(alphabet_position(char)+rot)%26)
    elif (ord(char) >= 65) and (ord(char) <=90): # uppercase
        return chr(65+(alphabet_position(char)+rot)%26)
    else:
        return char


def encrypt(text,rot):
    text_new = ""
    for pos in range(len(text)):
        text_new += rotate_character(text[pos],int(rot))
    return text_new
