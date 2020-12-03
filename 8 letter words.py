words = []

with open("8 letter words.txt", "r") as f:
    for line in f:
        for word in line.strip().split(" "):
            if word[0] != "#":
                words.append(word)


# sort all words' letters so that they can be compared

sorted_words = []

for word in words:
    sorted_words.append(sorted(word))

sorted_words_done = set([])

count = 0
for i, sorted_word in enumerate(sorted_words):
    if (str(sorted_word) not in sorted_words_done) and sorted_words.count(sorted_word) > 4:
        count += 1
        sorted_words_done.add(str(sorted_word))
        #print(words[i])
        print([words[i] for i, w in enumerate(sorted_words) if w == sorted_word])

print(count)
