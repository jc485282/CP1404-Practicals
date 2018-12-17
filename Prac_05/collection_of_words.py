
words_to_count = input("Text: ")
words_to_count = words_to_count.split(" ")

counted_words = {}

for word in words_to_count:
    if word in counted_words:
        counted_words[word] += 1

    else:
        counted_words[word] = 1

longest_key = max(len(word) for word in counted_words)

for word in sorted(counted_words):
    print("{:<{}} : {}".format(word, longest_key, counted_words[word]))
