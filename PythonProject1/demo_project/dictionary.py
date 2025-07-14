# Count occurrences of words
sentence = "apple banana apple orange banana apple"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print("Word occurrences:", word_count)

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)

# Retrieve keys and values separately
sample_dict = {"name": "Alice", "age": 25}
print("Keys:", list(sample_dict.keys()))
print("Values:", list(sample_dict.values()))
