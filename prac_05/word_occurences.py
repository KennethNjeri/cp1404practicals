"""
Word Occurrences
Estimate: 30 minutes
Actual: 35 minutes
"""

WORD_TO_COUNT = {}
text = input("Text: ")
words = text.split()

for word in words:
    if word in WORD_TO_COUNT:
        WORD_TO_COUNT[word] += 1
    else:
        WORD_TO_COUNT[word] = 1

unique_words = sorted(WORD_TO_COUNT.keys())
longest_word_length = max(len(word) for word in unique_words)

for word in unique_words:
    print(f"{word:<{longest_word_length}} : {WORD_TO_COUNT[word]}")

