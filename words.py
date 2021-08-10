import sys
from urllib.request import urlopen

def get_first_word(story_words):
  '''Returns the first word from a list of words this is a test'''
  return story_words[0]

def main(url):
  story = urlopen(url)
  story_words = []
  for line in story:
    line_words = line.decode('utf-8').split()
    for word in line_words:
      story_words.append(word)
  story.close()

  firstWord = get_first_word(story_words)
  print(firstWord)
  
if __name__ == "__main__":  
  url = sys.argv[1]
  main(url)
