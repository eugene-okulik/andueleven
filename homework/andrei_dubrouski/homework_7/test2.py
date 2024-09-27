words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def key_repeat(words):
    for key, value in words.items():
        print(key * value)

key_repeat(words)
