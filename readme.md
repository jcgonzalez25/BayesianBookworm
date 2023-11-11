# Guess The Author: Literary Analysis Using Bayes' Theorem

## Overview
**Guess The Author** is a sophisticated text analysis tool that applies Bayes' Theorem to discern the likely authorship of literary texts. Focused initially on works by Jane Austen and Charles Dickens, it paves the way for a new method in authorship attribution.

---

## 📚 Current Implementation

### Data Sources
The program ingests texts from the following novels, housed in the `Books/` directory:
- **Jane Austen**: _Emma (em)_, _Pride and Prejudice (pp)_, _Persuasion (pe)_, _Sense and Sensibility (ss)_
- **Charles Dickens**: _Great Expectations (ge)_, _Hard Times (ht)_, _A Tale of Two Cities (tc)_, _Oliver Twist (ot)_

### 📈 Word Frequency Analysis
A comprehensive dictionary is constructed to map word frequencies across these novels, providing a basis for authorship prediction:
```python
word_frequencies = {
    "officer": [220, 322]  # Austen: 220, Dickens: 322
}
```

### 🔍 Author Prediction
The `guess.py` script analyzes a passage to estimate the author, utilizing the frequency data in a Bayesian framework.

---

## 🔮 Future Enhancements

- **Expansion to More Authors**: Adaptability to include a diverse range of authors for broader literary analysis.
- **Algorithm Optimization**: Enhancements for processing efficiency with larger data sets.
- **User Interface Development**: Creation of a user-friendly platform for easy interaction and result interpretation.

---

This README is styled for a modern and visually appealing presentation, making the project's purpose, methodology, and future plans both clear and engaging.
