import unicodedata

def strip_accents(text):

    text = unicodedata.normalize("NFD",text).encode("ascii","ignore").decode("utf-8")
    return str(text)


def cipher(sentence,shift_value):
    translated = "" #new empty string of soon to be transformed string
    
    if sentence == "":
        return ""
    sentence = strip_accents(sentence)
    for char in sentence: 
        if char.isalpha():
            ascii_num = ord(char) #get the ascii rep of the character
            ascii_num += shift_value # add the shifted value
            
            #handle index rapping
            if char.isupper():
                if ascii_num > ord("Z"):
                    ascii_num -= 26
                elif ascii_num < ord("A"):
                    ascii_num += 26
            elif char.islower():
                if ascii_num > ord("z"):
                    ascii_num -= 26
                elif ascii_num < ord("a"):
                    ascii_num += 26
            translated += chr(ascii_num)
        else:
            translated += char
    return str(translated)