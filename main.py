# подготовка текста к анализу    

text = input("Введите текст: ")
text = text.lower()

signs = "!,.;:'\|^<>?/"

for sign in signs:
    text = text.replace(sign,"")
text = text.split()
l_word = text[0]
s_word = text[0]

for word in text:
    if len(word) > len(l_word):
        l_word = word
    elif len(word) < len(s_word):
        s_word = word

# анализ текста

word_frequency = {}
char_frequency = {}

# вывод результатов

print("Количество разных слов:", len(set(text)))
print("Самое длинное слово:", l_word)
print("Самое короткое слово:", s_word)
# вывод частоты слов

for word in text:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
# вывод частоты символов  

for char in text:
  if char in char_frequency:
        char_frequency[char] = char_frequency[char] + 1
  else:
        char_frequency[char] = 1
print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")