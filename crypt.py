import random


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key


def split(space, content):
    length = len(content)
    if length % space == 0:
        length = length / space
    elif length % space != 0:
        length = length - (length % space) / space
    split_content = []
    for x in range(1, int(length) + 1):
        split_content.append(content[(x - 1) * space: space * x])
    split_content = list(filter(lambda x: (x != ""), split_content))
    return split_content


def encrypt(content: str):
    content = content.split()
    encrypted_content = ""
    crypt_style = {'♥': ['os pq'], '\x01': ['ya ht'], '\x02': ['jm om'], '\x03': ['hl vr'], '\x04': ['vg nh'],
                   '\x05': ['fd ry'], '\x06': ['iz yt'], '\x07': ['pp ej'], '\x08': ['cz yg'], '\t': ['tt wn'],
                   '\n': ['np gh'], '\x0b': ['qr ox'], '\x0c': ['ya dz'], '\r': ['kf qi'], '\x0e': ['nh kt'],
                   '\x0f': ['ee az'], '\x10': ['bf zd'], '\x11': ['me lt'], '\x12': ['zi tr'], '\x13': ['em dh'],
                   '\x14': ['ob ia'], '\x15': ['hg ss'], '\x16': ['in om'], '\x17': ['jc lh'], '\x18': ['qw xr'],
                   '\x19': ['bn cs'], '\x1a': ['gw qx'], '\x1b': ['td ic'], '\x1c': ['dd uc'], '\x1d': ['ei zk'],
                   '\x1e': ['iz pf'], '\x1f': ['dn tn'], ' ': ['ap hm'], '!': ['ly xk'], '"': ['ky pg'],
                   '#': ['ik jr'], '$': ['tk zc'], '%': ['ss im'], '&': ['ot rr'], "'": ['yh vx'], '(': ['ue tf'],
                   ')': ['mk qq'], '*': ['wy eo'], '+': ['zl nu'], ',': ['zv nw'], '-': ['kp jy'], '.': ['zx gk'],
                   '/': ['sf xf'], '0': ['qr lh'], '1': ['cu tm'], '2': ['pj yt'], '3': ['wf qt'], '4': ['ne to'],
                   '5': ['zx hx'], '6': ['ow tp'], '7': ['wb uh'], '8': ['tb us'], '9': ['cd ku'], ':': ['rb xj'],
                   ';': ['gn ch'], '<': ['sk ib'], '=': ['gq op'], '>': ['lu bi'], '?': ['hd uv'], '@': ['zw sa'],
                   'A': ['cw vs'], 'B': ['sy xv'], 'C': ['zc en'], 'D': ['vt fd'], 'E': ['fk ah'], 'F': ['rv ph'],
                   'G': ['fh xi'], 'H': ['oo zh'], 'I': ['hz uz'], 'J': ['ia dx'], 'K': ['nj wn'], 'L': ['ht po'],
                   'M': ['ml vq'], 'N': ['sm ar'], 'O': ['vr rf'], 'P': ['hi yh'], 'Q': ['og ud'], 'R': ['nu yc'],
                   'S': ['rc lw'], 'T': ['iz iv'], 'U': ['nu yl'], 'V': ['ya hj'], 'W': ['zz lf'], 'X': ['io le'],
                   'Y': ['ye iz'], 'Z': ['rv tv'], '[': ['hj qa'], '\\': ['lu yd'], ']': ['ll su'], '^': ['ft jj'],
                   '_': ['xd it'], '`': ['nc re']}
    for i in content:
        for x in i:
            try:
                x = x.upper()
            except AttributeError:
                pass
            subset = crypt_style[x]
            subset = subset[0].split(" ")
            subset.append(random.randint(1000, 9999))
            subset = str(subset[0]) + str(subset[2]) + str(subset[1])
            encrypted_content += subset
        encrypted_content += " "
    return encrypted_content


def decrypt(content: str):
    content = content.split()
    decrypt_content = ""
    crypt_style = {'♥': ['os pq'], '\x01': ['ya ht'], '\x02': ['jm om'], '\x03': ['hl vr'], '\x04': ['vg nh'],
                   '\x05': ['fd ry'], '\x06': ['iz yt'], '\x07': ['pp ej'], '\x08': ['cz yg'], '\t': ['tt wn'],
                   '\n': ['np gh'], '\x0b': ['qr ox'], '\x0c': ['ya dz'], '\r': ['kf qi'], '\x0e': ['nh kt'],
                   '\x0f': ['ee az'], '\x10': ['bf zd'], '\x11': ['me lt'], '\x12': ['zi tr'], '\x13': ['em dh'],
                   '\x14': ['ob ia'], '\x15': ['hg ss'], '\x16': ['in om'], '\x17': ['jc lh'], '\x18': ['qw xr'],
                   '\x19': ['bn cs'], '\x1a': ['gw qx'], '\x1b': ['td ic'], '\x1c': ['dd uc'], '\x1d': ['ei zk'],
                   '\x1e': ['iz pf'], '\x1f': ['dn tn'], ' ': ['ap hm'], '!': ['ly xk'], '"': ['ky pg'],
                   '#': ['ik jr'], '$': ['tk zc'], '%': ['ss im'], '&': ['ot rr'], "'": ['yh vx'], '(': ['ue tf'],
                   ')': ['mk qq'], '*': ['wy eo'], '+': ['zl nu'], ',': ['zv nw'], '-': ['kp jy'], '.': ['zx gk'],
                   '/': ['sf xf'], '0': ['qr lh'], '1': ['cu tm'], '2': ['pj yt'], '3': ['wf qt'], '4': ['ne to'],
                   '5': ['zx hx'], '6': ['ow tp'], '7': ['wb uh'], '8': ['tb us'], '9': ['cd ku'], ':': ['rb xj'],
                   ';': ['gn ch'], '<': ['sk ib'], '=': ['gq op'], '>': ['lu bi'], '?': ['hd uv'], '@': ['zw sa'],
                   'A': ['cw vs'], 'B': ['sy xv'], 'C': ['zc en'], 'D': ['vt fd'], 'E': ['fk ah'], 'F': ['rv ph'],
                   'G': ['fh xi'], 'H': ['oo zh'], 'I': ['hz uz'], 'J': ['ia dx'], 'K': ['nj wn'], 'L': ['ht po'],
                   'M': ['ml vq'], 'N': ['sm ar'], 'O': ['vr rf'], 'P': ['hi yh'], 'Q': ['og ud'], 'R': ['nu yc'],
                   'S': ['rc lw'], 'T': ['iz iv'], 'U': ['nu yl'], 'V': ['ya hj'], 'W': ['zz lf'], 'X': ['io le'],
                   'Y': ['ye iz'], 'Z': ['rv tv'], '[': ['hj qa'], '\\': ['lu yd'], ']': ['ll su'], '^': ['ft jj'],
                   '_': ['xd it'], '`': ['nc re']}
    for i in content:
        encrypted_part = split(8, i)
        for x in encrypted_part:
            x = [x[0:2] + " " + x[6:8]]
            letter = get_key(x, crypt_style)
            decrypt_content += letter
        decrypt_content += " "
    return decrypt_content.lower()


k = int(input("choose 1 for encrypting and 2 for decrypting:"))
if k == 1:
    text = str(input("please enter the text to be encrypted:"))
    print(encrypt(text))
elif k == 2:
    text = input("please enter the text to be decrypted:")
    print(decrypt(text))
else:
    print("invalid option app terminated")
