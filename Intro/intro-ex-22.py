# 
# File: intro-ex-22.py
# Auth: Martin Burolla
# Date: 8/20/2021
# Desc: Morse Codify It
#

def main():
  userText = input('Enter text: ')
  print(convertTextToMorseCode(userText))

def convertMorseToText(morseCode):
  retval = ''
  morseToTextDict = {
    '*-'   : 'a', 
    '-***' : 'b',
    '-*-*' : 'c',
    '-**'  : 'd',
    '*'    : 'e',
    '**-*' : 'f',
    '--*'  : 'g',
    '****' : 'h',
    '**'   : 'i',
    '*---' : 'j',
    '-*-'  : 'k',
    '*-**' : 'l',
    '--'   : 'm',
    '-*'   : 'n',
    '---'  : 'o',
    '*--*' : 'p',
    '--*-' : 'q',
    '*-*'  : 'r',
    '***'  : 's',
    '-'    : 't',
    '**-'  : 'u',
    '***-' : 'v',
    '*--'  : 'w',
    '-**-' : 'x',
    '-*--' : 'y',
    '--**' : 'z'
  }
  return retval

def convertTextToMorseCode(text):
  retval = ''
  textToMorseDict = {
    'a' : '*-',
    'b' : '-***',
    'c' : '-*-*',
    'd' : '-**',
    'e' : '*',
    'f' : '**-*',
    'g' : '--*',
    'h' : '****',
    'i' : '**',
    'j' : '*---',
    'k' : '-*-',
    'l' : '*-**',
    'm' : '--',
    'n' : '-*',
    'o' : '---',
    'p' : '*--*',
    'q' : '--*-',
    'r' : '*-*',
    's' : '***',
    't' : '-',
    'u' : '**-',
    'v' : '***-',
    'w' : '*--',
    'x' : '-**-',
    'y' : '-*--',
    'z' : '--**'
  }
  for idx in range(len(text)):
    retval += (textToMorseDict[text[idx]] + ' ')
  return retval

if __name__ == "__main__":  
  main()
