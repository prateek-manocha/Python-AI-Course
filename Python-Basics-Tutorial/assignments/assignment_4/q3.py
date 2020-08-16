def record_notes():
    user = input('Enter the username: ')

    f = open(user+'__notes.txt', 'a')
    while True:
        note = input('Enter your note: ')
        if note == 'exit':
            break
        else:
            f.write(note)
            f.write('\n')
    f.close()

record_notes()

# today is sunday
