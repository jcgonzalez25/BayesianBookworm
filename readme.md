# BayesianBookworm: Unraveling Authorship with Bayesian Analysis

## Overview
**BayesianBookworm** is an innovative text analysis tool that harnesses the power of Bayes' Theorem to determine the probable authorship of literary texts. Initially focusing on the works of Jane Austen and Charles Dickens, this project introduces a novel approach to authorship attribution.

---

## 📚 Current Functionality

### Data Foundation
The program analyzes texts from the following novels, located in the `Books/` directory:
- **Jane Austen**: _Emma (em)_, _Pride and Prejudice (pp)_, _Persuasion (pe)_, _Sense and Sensibility (ss)_
- **Charles Dickens**: _Great Expectations (ge)_, _Hard Times (ht)_, _A Tale of Two Cities (tc)_, _Oliver Twist (ot)_

### 📈 Word Frequency Analytics
A sophisticated dictionary maps word frequencies across these novels, forming the backbone for authorship prediction:
```python
word_frequencies = {
    "officer": [220, 322]  # Austen: 220, Dickens: 322
}
```

### 🔍 Identifying the Author
The `guess.py` script employs this frequency data within a Bayesian framework to estimate the author of a given text passage.

---

## 🔮 Planned Enhancements

- **Incorporating More Authors**: Broadening the scope to include various authors for a more comprehensive literary analysis.
- **Enhanced Algorithm Efficiency**: Optimizing the processing capabilities for handling larger datasets.
- **User Interface Development**: Crafting an intuitive interface for effortless user interaction and result visualization.

---

BayesianBookworm represents a groundbreaking step in literary analytics, merging statistical methods with classical literature to unveil the hidden patterns in authorial styles.
