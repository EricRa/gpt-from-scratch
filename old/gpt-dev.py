# Open input text file, get length, and print first 1k characters

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("length of dataset in characters: ", len(text))

print("First 1000 characters:")
print(text[:1000])

# Find the unique characters that occur in the text
chars = sorted(list(set(text)))
vocab_size = len(chars)
print("".join(chars))
print(vocab_size)


# Create a character to integer mapping
stoi = {ch:i for } #10:30 in video