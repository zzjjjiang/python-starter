# 
# File: intro-ex-23.py
# Auth: Martin Burolla
# Date: 8/22/2021
# Desc: Morse to Text, Text to Morse
#

def main():
  while (True):
    inputString = input('Enter text: ').lower()
    if inputString[0] == '-' or inputString[0] == '*':
      text = convertMorseToText(inputString)
      print(f'Text: { text }')
    else:
      morseCode = convertTextToMorseCode(inputString)
      print(f'Morse Code: { morseCode }')

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
  
  morseCodeList = morseCode.split(' ')
  for code in morseCodeList:
    if code == '':
      retval += ' '
    else:
     retval += morseToTextDict[code]
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
    if (text[idx] == ' '):
      retval += ' '
    else:
      retval += (textToMorseDict[text[idx]] + ' ')
  return retval

if __name__ == "__main__":  
  main()
