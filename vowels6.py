
vowels = []
found = {}
for ch in 'aeiou':
    vowels.append(ch)
    
word = input('Provide a word to search for vowels: ')

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1
        
for k, v in sorted(found.items()):
    print(k, ':', v)
