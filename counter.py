
# letter_counter
text = open("tmp")
count = 0
for line in text:
    for i in line:
        if i.isalnum():
            count += 1
print(count)

#word_counter
text = open("tmp")
count = 0
for line in text:
    words = line.split()
    count += len(words)
print(count)



# most_used_word
text = open("tmp", "r")
counts = {}
for line in text:
    words = line.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
counts_max = max(counts, key = counts.get)
print(counts_max)

# most_used_letter
text = open("tmp")
counts = {}
for line in text:
    for i in line:
        if i.isalnum():
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
counts_max = max(counts, key = counts.get)
print(counts)
print(counts_max)


#sentence_counter
text = open("text")
count = 0
for line in text:
    for i in range(len(line) - 1):
        if i == "." and line[i + 1].isupper():
            count += 1
print(count)