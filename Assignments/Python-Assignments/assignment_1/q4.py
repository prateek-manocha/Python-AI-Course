#4. Write a function check_substring(string1,string2) to check if string2 is a substring of
#string1 . For example "chem" is a substring of "alchemy" and "chemistry". It returns True or False.

s1 = input('Substring to be checked: ')
s2 = input('String in which substring is to be checked: ')

def check_substring(s1, s2):
    if s1 in s2:
        print('Substring found in String.')
    else:
        print('Substring not a part of String.')

check_substring(s1,s2)
