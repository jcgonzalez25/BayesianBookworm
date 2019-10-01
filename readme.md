# Guess The Author 
## Implementing Bayes Theorem
## Implementation
* Program reads words from both authors `austen` and `dickens` found in `Books/`
```
    bookPaths = ["Books/austen.em.txt",
	     "Books/austen.pp.txt",
	     "Books/austen.pe.txt",
	     "Books/austen.ss.txt",
	     "Books/dickens.ge.txt",
	     "Books/dickens.ht.txt",
	     "Books/dickens.tc.txt",
	     "Books/dickens.ot.txt"]
```
* Each word from these books is split into most common word frequency dictionary where a key will be the word and value will be the two authors word frequency
```
["officer"] = [220,322]
```
* officer was written 220 by austen and 322 by dickens
### With this data we could run `guess.py` that is passed a file of a passage in which guesses the author who wrote this
## Future Implmentation
* implement for any author