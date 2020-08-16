def read_notes():
    user = input('Enter user name: ')
    f = open(user+'__notes.txt', 'r')
    word = input('Enter the word you are interested in: ')
    for line in f:
        orig_line = line
        for txt in line.split(' '):
            if txt == word:
                print(orig_line)
            continue
    f.close()

read_notes()
