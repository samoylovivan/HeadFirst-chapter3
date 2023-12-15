
vowels = set('aeiou')

word = input('Provide a word to search for vowels: ')

# метод intersection() возвращает общие объекты (операция пересечения множеств);
# метод union() возвращает объедененное множество;
# метод difference() возвращает разность множеств;

found = vowels.intersection(set(word))

for vowel in found:
    print(vowel)
