# Project 7: Guided Project (Machine Learning)

**Author:** Tammy Mims  
**Date:** February 20, 2026

---

## Project Summary

This project is a guided exploration of machine learning concepts using Python and Jupyter. The setup uses modern Python packaging with `pyproject.toml` and dependency management via `uv`. The environment is configured for Python 3.14.2, and all required data science packages are installed for reproducible analysis.


## Project Planning

Two languages:

- This file is written in **Markdown**, a simple markup language for presenting text.
- Our analytics logic is written in **Python**, a scripting language for implementing logic.

When we first encounter a **new and unknown data set**, we want to explore: run some quick checks, view the distributions, see if the data is clean (or if there are many missing values or outliers).

In this module, we will create a guided project.
There is no specification - we introduce some topics including machine learning as we work through the module.
The project will include Jupyter. 


```
git push
```
## Project Setup (Windows / PowerShell, local computer C:)

1. **Clone the repository:**
  Open a terminal in your `Repos` folder and run:

  ```shell
  git clone https://github.com/tmims71-ctrl/datafun-07-ml
  cd datafun-07-ml
  ```

2. **Open in VS Code:**
  ```shell
  code .
  ```

3. **Install recommended extensions:**
  When prompted, accept Extension Recommendations (click **Install All**).

4. **Set up the Python environment:**
  - Open a terminal in the root project folder.
  - If using `uv` (recommended):
    ```shell
    uv self update
    uv python pin 3.14
    uv sync --extra dev --extra docs --upgrade
    ```
  - If using `pip`:
    ```shell
    pip install -r requirements.txt
    ```
  - Or, for modern dependency management, use:
    ```shell
    pip install .
    ```



5. **Launch JupyterLab:**
  ```shell
  jupyter lab
  ```

   - Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.
   - Run the following commands, one at a time, hitting ENTER after each:

    ```shell
    uv self update
    uv python pin 3.14
    uv sync --extra dev --extra docs --upgrade
    ```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Optional (recommended): install and run pre-commit checks (repeat the git `add` and `commit` twice if needed):

```shell
```

## Requirements

Project dependencies are managed in `pyproject.toml` for modern Python packaging. The main packages used are:

- jupyterlab
- numpy
- pandas
- pyarrow
- matplotlib
- seaborn
- scipy
  
### Key Setup Steps Completed

- Created and configured `pyproject.toml` for dependency management
- Installed dependencies (`jupyterlab`, `numpy`, `pandas`, `pyarrow`, `matplotlib`, `seaborn`, `scipy`) using `uv sync`
- Selected Python 3.14.2 environment in VS Code for consistency
- Verified environment and package installation
- Updated README with project details and setup instructions
- Ready to launch JupyterLab and begin analysis

---

## Reminders Notes

Default README.md created with creation of repostory

Project cloned to local computer C:\Repos.

Added .gitignore from a list recommended by Github, selected one compatible with Python

Created and activated a local virtual environment (.venv).

Installed required packages.

Added requirements.txt (legacy) and pyproject.toml (modern Python packaging)


---

## Recent Code Updates

- Refactored `ch10/snippets_py/10_16.py`:
  - Moved all import statements to the top of the file (PEP 8 compliance)
  - Removed duplicate and leftover code (such as repeated imports and lambda definitions)
  - Replaced lambda function with a proper def function
  - Ensured all code that uses variables (like `nyc`) is placed after those variables are defined
  - Added print statements to show DataFrame info and results
  - Organized script so it runs smoothly and produces clear output and plots
- Added demonstration/test code to `ch10/snippets_py/salariedcommissionemployee.py` so it prints example output when run directly
- Provided guidance and fixes for running, cleaning, and understanding scripts and Jupyter notebooks in the project

---
