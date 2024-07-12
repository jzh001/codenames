# Codenames

A codenames bot modelling the spymaster and operative.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

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
    conda activate your-environment-name
    ```

4. (Optional) If you need to update the environment with new dependencies, use:

    ```bash
    conda env update -f environment.yml --prune
    ```

## Usage

```bash
python run.py --power 5 --save 1 --epochs 10 --verbose 1
```
--power: Maximum number of guesses per turn, k (default 5)
--save: Save history in history.json if set to 1
--epochs: Number of game iterations
--verbose: 0 for less logging, 1 for more logging