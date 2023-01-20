# Print number of words + number of spaces in a sentence
statements = ["I am a boy", "I am a girl", "I am a man", "I am a woman"]

sentence_lengths = {}
for sentence in statements:
    word_count = sentence.count(" ")
    word_count += len(sentence.split(" "))
    sentence_lengths[sentence] = word_count

print(sentence_lengths)