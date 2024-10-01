from itertools import product

letters = 'ПРИВЫЧКА'
words = []
for p in product(letters, repeat=5):
    words.append(''.join(p))
words.sort()
count = 1
k = 0
for word in words:
    if count % 5 != 0:
        k += 1
    if count % 5 != 0 and len(set(word)) == 5 and 'А' not in word and 'И' not in word and 'Ы' not in word:
        print(k, count)
        break
    count += 1