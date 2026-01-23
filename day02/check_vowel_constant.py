# usr = input("Enter a chaacter: ")
# # sug
# if usr in 'aeiouAEIOU':
#     print(f"{usr} is a vowel.")
# else:
#     print(f"{usr} is a consonant.")


usr = input("Enter a word: ")

for ch in usr:
    if ch.lower() in 'aeiou':
        print(f"{ch} is a vowel")
    else:
        print(f"{ch} is a consonant")
