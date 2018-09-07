#!
import sys
import re
#   /u1/junk/cs617/Books
class Word:
    def __init__(self,word):
        self.word = word
    def isDoubleLined(self):
      if self.word[-1:] == '-':
          return True
    def hasDoubleDashes(self):
      if "--" in self.word:
        return True
      else:
        return False
    def isValidLength(self):
      if len(self.word) >= 5 and len(self.word) <= 9:
        return True
      else:
        return False
    def combine(self,wordTwo):
      self.word = self.word + wordTwo
      self.word = self.word.replace("-","")

class Dictionary:
    def __init__(self):
        self.dict = dict()
    def checkAndUpdate(self,word):
      if self.dict.get(word) == None:
        self.dict[word] = 1
      else:
        self.dict[word] = self.dict[word] + 1
    def getDictionaryStats(self):
      return self.dict

class Filter:
  def NonWords(words):
    words = re.split('[^A-Za-z-]',words)
    words = filter(None,words)
    return list(words)

  def doubleLinedWords(words):
    #Dictionary is my own personal Dictionary object
    #Method also returns dictionary with stats of each word
    updatedWords = Dictionary()
    flag         = 0
    dashedWord   = ''
    for idx, word in enumerate(words):
      if flag == 1:
        flag = 0
        if currentWord.isValidLength():
          updatedWords.checkAndUpdate(currentWord.word)
        continue
      currentWord = Word(word)
      if currentWord.isDoubleLined():
        currentWord.combine(words[idx + 1])
        flag = 1
        continue
      if currentWord.hasDoubleDashes():
        splitWords = currentWord.word.split('--')
        for word in splitWords:
          word = Word(word)
          if word.isValidLength() == True:
            updatedWords.checkAndUpdate(word.word)
      if currentWord.isValidLength():
        updatedWords.checkAndUpdate(currentWord.word)
    return updatedWords


class FileHandler:
  def __init__(self,fileName):
    self.fileName  = fileName
    self.words     = None
    self.dictionary = None
  def readFile(self):
    try:
      with open(self.fileName, "r") as fileData:
        self.words = self.organizeIntoDict(fileData)
    except IOError:
      print(self.fileName + " Not Found\n")
  def organizeIntoDict(self,data):
    fileData            = data.read()
    words               = Filter.NonWords(fileData)
    finalDictionary     = Filter.doubleLinedWords(words)
    self.dictionary     = finalDictionary.getDictionaryStats()

if __name__ == "__main__":
    F = FileHandler(sys.argv[1])
    F.readFile()
    print(F.dictionary)
