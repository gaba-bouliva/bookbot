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
  


try:
  file = open("books/frankenstein.txt", "r")
  file_content = file.read()
  print(word_count(file_content))
  print(character_count(file_content))
except FileNotFoundError :
  print("invalid file name or filepath provided")
except Exception as e:
  print(e)