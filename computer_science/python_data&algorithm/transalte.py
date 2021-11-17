
def translate(word):
    translation = ''

    for i in word:
        if i.lower() in 'aeiou':
            if i.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += i
    return translation

print(translate(input("Enter a word: ")))