# Workshop 4: Pandas and Data Processing
![Pandas banner](./PandasBanner.png)
_Get started with data manipulation using Python's most powerful data analysis library!_

(Note: you should already have completed Workshop 3 on Python basics and have Python, pip, venv, and VSCode set up)

## Overview
Welcome to Workshop 4! Today we're diving into **pandas** - Python's essential library for data analysis and manipulation. You'll learn how to load, clean, analyze, and visualize data like a data scientist.

By the end of this workshop, you'll be able to work with real datasets, perform complex data operations, and extract meaningful insights from data. 🧪

## What is Pandas?

Pandas is a powerful Python library that makes working with structured data (like spreadsheets or databases) incredibly easy. Think of it as a more powerful version of Excel - you can:
- Load data from CSV files, Excel sheets, databases, and more
- Clean messy data and handle missing values
- Filter, sort, and group data in sophisticated ways
- Perform calculations and statistical analysis
- Create visualizations to understand your data

Pandas is used by data scientists, analysts, and researchers worldwide for everything from business analytics to scientific research.

## Setup Instructions

### Prerequisites
You must have completed Workshop 3 and have Python, pip, venv, and VSCode installed.

### Step 1: Create a Virtual Environment
Create a fresh virtual environment specifically for this data analysis workshop.

```bash
# Create a virtual environment
python -m venv pandas-env

# Activate the virtual environment
source pandas-env/bin/activate
```

You should see `(pandas-env)` appear in your terminal prompt when the environment is active.

### Step 2: Install Required Libraries
Instead of installing packages one by one, we'll use a `requirements.txt` file - a standard way to manage project dependencies in Python.

#### What is requirements.txt?
A `requirements.txt` file lists all the Python packages your project needs, along with their specific versions. This ensures that:
- Everyone working on the project uses the same package versions
- You can easily recreate the same environment on different computers
- Your code runs consistently across different setups

The file contains one package per line, like:
```
pandas==2.0.3
matplotlib==3.7.2
jupyter==1.0.0
```
Note that the `==` symbols specify exact versions to perfectly reproduce the environment. Often, you might see `>=` or `<=` to indicate minimum or maximum versions so there's some flexibility for different devices. 

⚠️ In professional settings, more precise tools like [Docker](https://www.youtube.com/watch?v=Ud7Npgi6x8E) or [Conda](https://www.youtube.com/watch?v=YJC6ldI3hWk) are used for "environment management" (making sure two people on different computers can always work with the same setup). Though these are too complicated for us to set up on everyone's computers, which is why we're using `venv` as a much simpler alternative.

#### Install from requirements.txt
```bash
# Install all packages listed in requirements.txt
pip install -r requirements.txt
```

This single command will install pandas, matplotlib, jupyter, and any other dependencies needed for this workshop. Don't forget the `-r` flag which tells pip to read from the file.

### Step 3: Open the Pandas Notebook
1. Open VS Code in your project folder: `code .`
2. Make sure the Jupyter extension is installed (you should have this from Workshop 3)
3. Open `pandas.ipynb` by double-clicking it in the VS Code file explorer

### Step 4: Select Your Kernel
When you open the notebook:
1. Click "Select Kernel" in the top-right of the notebook
2. Choose "Python Environments..."
3. Select "Python (pandas-env)" from the list

You should now be able to run cells using Shift+Enter or the play button.

## Troubleshooting

### Common Issues and Solutions

**"requirements.txt not found"**
- Make sure you're in the correct directory where the requirements.txt file is located
- Check that the file exists: `ls requirements.txt`

**Package installation fails**
- Make sure your virtual environment is activated (you should see `(pandas-env)` in your terminal)
- Try upgrading pip first: `pip install --upgrade pip`
- If still failing, install packages individually: `pip install pandas matplotlib jupyter`

**Import errors when running notebook cells**
- Verify packages are installed: `pip list` should show pandas, matplotlib, etc.
- Make sure you selected the correct kernel (pandas-env) in the notebook
- Try restarting the kernel: click the restart button in the kernel selector

**Kernel connection issues**
- Restart VS Code completely
- Reactivate your virtual environment: `source pandas-env/bin/activate`
- Reinstall ipykernel: `pip install ipykernel`

**Data files not loading**
- Check that any CSV or data files are in the same directory as your notebook
- Verify file paths in your code match the actual file locations
- Use forward slashes (/) in file paths, even on Windows

### Alternative Setup: Kaggle

If you're having trouble with local setup:

1. **Kaggle**: Upload `pandas.ipynb` to [kaggle.com](https://www.kaggle.com) - pandas is pre-installed

Both platforms provide fully configured environments with pandas and other data science libraries ready to use.

## Getting Started

Once your environment is set up:
1. Open `pandas.ipynb` and start learning data manipulation
2. Work through the examples and exercises in the notebook
3. Experiment with the provided datasets
4. Try modifying the code to explore different aspects of the data
5. Complete all the hands-on exercises to reinforce your learning

## When You're Done

After completing the pandas workshop:

```bash
# Deactivate your virtual environment
deactivate

# Move to the next workshop on LangChain
git checkout workshop-5
```

You can also return to the main page:
```bash
git checkout main
```