# Analyze a sentence input by the user
sentence = input("input: ")
# Count the number of words in the sentence
word_count = len(sentence.split())
# Output the results
print(f"Total words: {word_count}")

# Find the longest word and its length
longest_word = max(sentence.split(), key=len)
# Output
print(f"Longest word: {longest_word} ({len(longest_word)} letters)")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Title case: {sentence.title()}")
print(f"Reversed: {sentence[::-1]}")