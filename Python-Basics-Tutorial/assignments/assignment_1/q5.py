'''Write a function to generate all substrings of a string and return it as a list of strings. Let the function be
called generate_substrings(string) . For example, generate_substrings("alchemy")
returns ["a","al","alc","alch","alche","alchem","alchemy","l","lc",... etc] . There
should be no repititions in the list.'''
s = input('String for which substrings need to be generated: ')

def substring(s):
    length = len(s)
    c = []
    for i in range(length+1): # We just have to find all the unique combination of indexes.
        for j in range(i+1, length+1):
            c.append(s[i:j])
    return c

print(substring(s))
