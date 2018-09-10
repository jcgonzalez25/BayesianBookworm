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
    def hasDashes(self):
      if "-" in self.word:
        return True
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
      if currentWord.hasDashes() == True:
        splitWords = re.split('-',currentWord.word)
        for splitee in splitWords:
          splitee = Word(splitee)
          if splitee.isValidLength() == True:
            updatedWords.checkAndUpdate(splitee.word)
      elif currentWord.isValidLength():
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
# TO DO:
  # get frequency from all 8 books 
  # 
if __name__ == "__main__":
    Austen1 = FileHandler("/u1/junk/cs617/Books/austen.em.txt")
    Austen2 = FileHandler("/u1/junk/cs617/Books/austen.pp.txt")
    Austen3 = FileHandler("/u1/junk/cs617/Books/austen.pe.txt")
    Austen4 = FileHandler("/u1/junk/cs617/Books/austen.ss.txt")
    Dickens1 = FileHandler("/u1/junk/cs617/Books/dickens.ge.txt")
    Dickens2 = FileHandler("/u1/junk/cs617/Books/austen.ht.txt")
    Dickens3 = FileHandler("/u1/junk/cs617/Books/austen.tc.txt")
    Dickens4 = FileHandler("/u1/junk/cs617/Books/austen.gt.txt")
    Austen1.readFile()
    
    #print(Austen1.dictionary)
