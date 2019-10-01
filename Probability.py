def __init__(self,austinWords,dickensWords,words):
  self.aTotalWords     = austinWords
  self.dTotalWords    = dickensWords
  self.wordData        = words
  self.wordProbability = dict()
    #word data is dictionary whose key is a word
    #returns an array
def getProbabilityDictionary(self):
  for word, WordCounts in self.wordData.items():
    a = WordCounts[0] / self.aTotalWords
    b = WordCounts[1] / self.dTotalWords
    self.wordProbability[word] = [a,b]
  return self.wordProbability
      