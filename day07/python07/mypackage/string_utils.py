def upper(s):
    return s.upper()


def lower(s):
    return s.lower()    

def info(**kwargs):
    return kwargs

def capitalize(s):
    return s.capitalize()

def title(s):
    return s.title()    


def reverse(s):
    return s[::-1]


def is_palindrome(s):
    return s == s[::-1]


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)   

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)    


def remove_whitespace(s):
    return ''.join(s.split())

def word_count(s):
    words = s.split()
    return len(words)   


def char_count(s):
    return len(s)   

def find_substring(s, substring):
    return s.find(substring)


def replace_substring(s, old, new):
    return s.replace(old, new)  


def split_string(s, delimiter=' '):
    return s.split(delimiter)


def join_strings(strings, delimiter=' '):
    return delimiter.join(strings)