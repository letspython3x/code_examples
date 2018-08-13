def argot(word):
    if word.endswith('ay'):
        word = word[:-2]
        word = word[-1] + word[:-1]
    else:
        pass
    return word


print(argot('raytabletay'))