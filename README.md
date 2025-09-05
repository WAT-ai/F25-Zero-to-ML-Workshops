# Workshop 3: Python Basics
![Python logo](./PythonBanner.png)
_Get started with Python programming!_

(Note: you should already have installed VSCode via `SetupVSCode.md` in the `workshop-3` branch and installed Python, pip, venv, and Bash from prior workshops)

## Overview
Welcome to Workshop 3! Today we're learning about **Python basics** - the fundamental concepts and syntax that every Python programmer should know. We'll cover variables, data types, control structures, functions, and more.

By the end of this workshop, you'll have a solid understanding of Python and be able to write your own simple scripts. 💪

# Python Jupyter Notebooks Setup Guide

This repository contains interactive Python notebooks that teach programming fundamentals. Follow this guide to set up your development environment and start learning.

## What are Jupyter Notebooks?

Jupyter notebooks are interactive documents that combine code, explanations, and outputs in a single file. They're perfect for learning programming because you can:
- Run code step-by-step and see results immediately
- Mix code with explanations and notes
- Experiment with examples without affecting other parts
- Save your progress as you work through exercises

Each `.ipynb` file in this repository is a Jupyter notebook containing lessons and exercises.

## Setup Instructions

### Option 1: VS Code (Recommended)

#### Prerequisites
You must have followed past workshops to install a Bash CLI via Mac/WSL2, python, pip, venv, and VSCode. 

#### Step 1: Create a Virtual Environment
A virtual environment keeps your project dependencies isolated from other Python projects.

```bash
# Create a virtual environment
python -m venv jupyter-env

# Activate the virtual environment
source jupyter-env/bin/activate
```

You should see `(jupyter-env)` appear in your terminal prompt when the environment is active.

#### Step 2: Install Required Packages
```bash
# Install Jupyter kernel support
pip install ipykernel
```

#### Step 3: Open Notebooks in VS Code
1. Open VS Code in your project folder: `code .`
2. Install the Jupyter extension:
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Jupyter" by Microsoft
   - Install it

3. Open any `.ipynb` file by double-clicking it in the VS Code file explorer

#### Step 4: Select Your Kernel
When you open a notebook, VS Code will ask you to select a kernel:
1. Click "Select Kernel" in the top-right of the notebook
2. Choose "Python Environments..."
3. Select "Python (jupyter-env)" from the list

You should now be able to run cells using Shift+Enter or the play button.

### Option 2: Kaggle (Alternative if VS Code isn't working)

If you're having trouble with local setup, you can use Kaggle's free online environment:

1. Go to [kaggle.com](https://www.kaggle.com) and create a free account
2. Navigate to "Code" → "Notebooks"
3. Click "New Notebook"
4. Upload the `.ipynb` files in this branch using the "Import notebook" option
5. The environment is ready to use - no setup required!

Kaggle provides a fully configured Python environment with all common packages pre-installed.

## Troubleshooting

### Common Issues and Solutions

**"Python is not recognized" or "python: command not found"**
- Make sure Python is installed and added to your system PATH
- Try using `python3` instead of `python` on macOS/Linux

**VS Code can't find your kernel**
- Make sure your virtual environment is activated when installing ipykernel
- Try restarting VS Code after installing the Jupyter extension
- Manually select the Python interpreter: Ctrl+Shift+P → "Python: Select Interpreter" → choose your virtual environment

**Cells won't run or show "kernel not found"**
- Click the kernel selector in the top-right of the notebook
- Choose "Select Another Kernel..." → "Python Environments" → select your virtual environment
- If your environment isn't listed, make sure you've run the `pip install ipykernel` command. Try `pip3` if that command isn't found.

**Import errors for common packages**
- Activate your virtual environment: `source jupyter-env/bin/activate` (macOS/Linux).
- Install missing packages: `pip install package-name`
- Restart your kernel: Click "Restart" in the kernel selector

**VS Code Jupyter extension not working**
- Update VS Code to the latest version
- Reinstall the Jupyter extension
- Try the "Developer: Reload Window" command (Ctrl+Shift+P)

**Virtual environment issues**
- Make sure you're in the correct directory when creating the environment
- If activation isn't working, try using the full path to the activate script
- Delete and recreate the environment if it becomes corrupted

### Still Having Issues?

1. **Use Kaggle**: Upload your notebooks to Kaggle for a zero-setup solution
2. **Google Colab**: Upload `.ipynb` files to [colab.research.google.com](https://colab.research.google.com)
3. **Check Python installation**: Run `python --version` to verify Python is properly installed

## Getting Started

Once your environment is set up:
1. Open `python-basics-part1.ipynb` to start with fundamentals
2. Work through the notebooks in order: Part 1 → Part 2 → Part 3. There's an optional `buggy_script.py` file to debug if you want to learn about [step-through debugging](https://www.youtube.com/watch?v=7qZBwhSlfOo).
3. Run each code cell using Shift+Enter
4. Complete the exercises in each notebook
5. Experiment with the examples - breaking things is part of learning!

## Tips

- **Run cells in order**: Notebooks are designed to be executed sequentially
- **Experiment freely**: Copy cells and modify them to test your understanding
- **Read error messages**: They contain valuable information about what went wrong
- **Ask for help**: If you're stuck, the error messages usually point you in the right direction

--------------------

When you're done, run `deactivate` to exit the virtual environment. Then, proceed to the next workshop on common ML libraries (mainly Langchain).
```bash
git checkout workshop-4
```

You can also go back to the main page with
```bash
git checkout main
```