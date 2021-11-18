d = {'one': 1, 'two': 2, 'three': 3}

d['four'] = 4

print("dic ", d)
d.update({'five': 5, 'four': 4, 'one': 1, 'six': 6, 'three': 3,
          'two': 2})
print("new dic ", d)

print("five" in d)


# sorting dictionaries

sorted(list(d)) # sort keys

print('sort key ', d)

sorted(list(d.values())) # sort value

print('sort value ', d)

print()

print(sorted(list(d), key=d.__getitem__))

print([value for (key, value) in sorted(d.items())])

print()
print("--------------------------")

# dictionaries for text analysis
print()



def wordcount(fname):

    try:
        fhand = open(fname)
    except:
        print("File can't be opened")
        exit()

    count = dict ()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count


a = wordcount('hello.txt')
print(a)