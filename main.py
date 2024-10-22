def word_count(text):
  return len(text.split())

def character_count(text):
  char_counter = {}

  for char in text:
    if char.lower() in char_counter:
      char_counter[char.lower()] += 1 
    else:
      char_counter[char.lower()] = 1

  return char_counter

total_words = None
char_counts = None

try:
  file = open("books/frankenstein.txt", "r")
  file_content = file.read()
  total_words = word_count(file_content)
  char_counts = character_count(file_content)
except FileNotFoundError :
  print("invalid file name or filepath provided")
  exit(1)
except Exception as e:
  print(e)
  exit(1)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{total_words} words found in the document\n")

# special_chars = ["\n", "\t", "\r", " "]
alphabet_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v","w", "x", "y", "z"]



for character in char_counts:
  if character in alphabet_chars:
    print(f"The '{character}' character was found {char_counts[character]} times")

print("--- End report ---")
