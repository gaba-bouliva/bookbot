try:
  file = open("books/frankenstein.txt", "r")
  file_content = file.readlines()
  print(file_content)
except FileNotFoundError :
  print("invalid file name or filepath provided")
except Exception as e:
  print(e)