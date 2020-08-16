import json

def view_word_examples(word, surrounding_chars, max_examples):
    with open('passage_info.json', 'r') as f:
        unique_words = json.load(f)
    word = word.lower()
    if word in unique_words:
        print('Found it.')
        f = open('passage.txt', 'r')
        min_entries = min(max_examples, len(unique_words[word]))
        for i in range(min_entries):
            start_char = unique_words[word][i][0]
            if start_char >= surrounding_chars:
                f.seek(start_char-surrounding_chars)
                text = f.read(2*surrounding_chars + len(word))
                print(text)
            else:
                f.seek(0)
                text = f.read(surrounding_chars + len(word)+start_char)
                print(text)
        f.close()
    else:
        print('Not Found.')


word = input('Enter the word to search: ')
surr_char = int(input('Enter surrounding chars: '))
view_word_examples(word, surr_char, 5)













#end of file
