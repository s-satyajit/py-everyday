para = "hello world hello"

freq = {}

for word in para.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)