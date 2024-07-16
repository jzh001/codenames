# Codenames

A codenames bot modelling the spymaster and operative. 

Article: https://towardsdatascience.com/hacking-codenames-with-glove-embeddings-0cf928af0858

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

### Prerequisites

Make sure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed on your machine. You can install Miniconda or Anaconda based on your preference.

### Setting Up the Environment

1. Clone the repository:

    ```bash
    git clone https://github.com/jzh001/codenames.git
    cd codenames
    ```

2. Create a new conda environment using the provided `environment.yml` file:

    ```bash
    conda env create -f environment.yml
    ```

3. Activate the newly created environment:

    ```bash
    conda activate codenames
    ```

4. (Optional) If you need to update the environment with new dependencies, use:

    ```bash
    conda env update -f environment.yml --prune
    ```

## Usage

```bash
python run.py --power 5 --save 1 --epochs 10 --verbose 1
```

--save: Save history in history.json if set to 1 (default 1)

--epochs: Number of game iterations (default 1)

--verbose: 0 for less logging, 1 for more logging (default 1)

--candidates: Number of candidates suggested (default 20)

--negatives: Number of negatives suggested (default 20)

--append: 0 for overwrite, 1 for append data (default 0)

--good: Number of good words (default 9)

## Data
- Codenames word data obtained from https://github.com/Gullesnuffs/Codenames/blob/master/wordlist-eng.txt
- GloVe embedding data obtained from Gensim (Paper: Pennington, J., Socher, R., & Manning, C. (2014). Glove: Global vectors for word representation. Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP). https://doi.org/10.3115/v1/d14-1162)