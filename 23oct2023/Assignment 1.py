"""
Task 1

✅ Count vowels and consonants in a String

aeiou

input = pramod
vol = 2
"""
name = input("Enter your name\n")
vowel_set = set("aeiouAEIOU")

def count_vowels(word):
    count_v = 0
    count_c = 0
    for i in word:
        if i in vowel_set:
            count_v=count_v+1
        else:
            count_c=count_c+1

    print(f"Total vowels is {count_v}")
    print(f"Total consonents is {count_c}")

count_vowels(name)