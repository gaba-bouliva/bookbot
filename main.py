def word_count(text):
  return len(text.split())

try:
  file = open("books/frankenstein.txt", "r")
  file_content = file.read()
  print(word_count(file_content))
except FileNotFoundError :
  print("invalid file name or filepath provided")
except Exception as e:
  print(e)