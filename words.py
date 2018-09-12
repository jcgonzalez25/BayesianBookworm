
import sys
import re
#   /u1/junk/cs617/Books
class Word:
    def __init__(self,word):
        self.word = word.lower()
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
      if word in self.dict:
        self.dict[word] = self.dict[word] + 1
      else:
        self.dict[word] = 1
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
      if currentWord.hasDashes():
        splitWords = re.split('-',currentWord.word)
        for splitee in splitWords:
          splitee = Word(splitee)
          if splitee.isValidLength():
            updatedWords.checkAndUpdate(splitee.word)
      elif currentWord.isValidLength():
        updatedWords.checkAndUpdate(currentWord.word)
    return updatedWords


class FileHandler:
  def __init__(self,fileName):
    self.fileName   = fileName
    self.words      = None
    self.dictionary = None
    self.readFile()
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

class WordChart:
  def __init__(self,dictionaries):
    self.bookDictionaries = dictionaries
    self.wordChart        = dict()
    self.wordFrequencyOfEachBook = []
  def collectAndPrint(self):
    allWords = set([])
    for bookDictionary in self.bookDictionaries:
      allWords = allWords | set(bookDictionary.keys())
    for word in allWords:
      self.wordChart[word] = []
      for i in range(0,len(self.bookDictionaries)):
        try:
          self.wordChart[word].append(self.bookDictionaries[i][word])
        except KeyError:
          self.wordChart[word].append(0)
    print(self.wordChart)


class BookCollectionHandler:
  def __init__(self,bookPaths):
    self.bookPaths        = bookPaths
    self.bookDictionaries = []
    self.getDictionaryStats()
    self.wordCounterObjects = []
    #bookDictionaries is an array of FileHandlerObjects
  def getDictionaryStats(self):
    for book in self.bookPaths:
      bookFile = FileHandler(book)
      self.bookDictionaries.append(bookFile.dictionary)

  def CreateWordDictionary(self):
    chart = WordChart(self.bookDictionaries)
    chart.collectAndPrint()

if __name__ == "__main__":
    bookPaths = ["/u1/junk/cs617/Books/austen.em.txt",
	     "/u1/junk/cs617/Books/austen.pp.txt",
	     "/u1/junk/cs617/Books/austen.pe.txt",
	     "/u1/junk/cs617/Books/austen.ss.txt",
	     "/u1/junk/cs617/Books/dickens.ge.txt",
	     "/u1/junk/cs617/Books/dickens.ht.txt",
	     "/u1/junk/cs617/Books/dickens.tc.txt",
	     "/u1/junk/cs617/Books/dickens.ot.txt"]
    Books = BookCollectionHandler(bookPaths)
    Books.CreateWordDictionary()

    #print(Austen1.dictionary)
