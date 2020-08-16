f = open('passage.txt', 'r')
f.read()
print('Total number of characters:',f.tell())

unique_words = {}
position = 0
f.seek(position)
for line in f:
    for word in line.split(' '):
        word_mod = word.replace('.','').replace('(','').replace(')','').replace(',','').replace('\n','').lower()
        if word_mod not in unique_words:
            unique_words[word_mod] = []
        unique_words[word_mod].append([position, position+len(word_mod)-1])
        position += len(word) + 1
    position -= 1  # removing the space at end of line word
    position += 2  # for adding the new line character
print(unique_words)
position -= 2
print(position)

import json
with open('passage_info.json', 'w') as f:
    json.dump(unique_words, f)
print('passage_info.json saved.')















f.close()
