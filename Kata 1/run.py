INIT_LETTER = 'a'

def get_number(letter):
    value = ord(letter) - ord(INIT_LETTER) + 1
    return str(value) if 0 < value < 27 else None

def alphabet_position(phrase):
    ret = []
    for letter in phrase:
        value = get_number(letter.lower())
        if value:
            ret.append(value)
    return ' '.join(ret)
