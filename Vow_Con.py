s="heLlO"
vowel= []
const= []
for i in s:
    if i.lower() in ['a','e','i','o','u']:
        vowel.append(i)
    else:
        const.append(i)
print("vowels in given string are:", vowel)
print("Consonants in given string are:", const)
