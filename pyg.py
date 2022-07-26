import sys

def main():
  """Python practice"""
  sentence = input("Enter word\n")
  words = sentence.split(' ')
  pyg_sentence = ""
  for word in words:
    pyg_word = word[1:len(word)] + word[0].lower() + 'ay'
    pyg_sentence += pyg_word + ' '

  print(f"{pyg_sentence}")

if __name__ == "__main__":
  main()