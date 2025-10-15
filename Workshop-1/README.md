# Workshop 1: Command Line Interfaces and Package Management
![Terminal with colorful output](./CLIBanner.png)
_Welcome to the command line - your new superpower!_

## Overview
Welcome to your first Zero to ML workshop! Our focus here is the **command line interface (CLI)**. This is a text-based way to interact with your computer instead of pointing and clicking with a mouse. It might look intimidating at first, but it's a lot more flexible and every developer uses CLIs at some point. 

We'll also explore **package managers**, which help you easily install and manage tools you'll need while developing any kind of software. By the end of this workshop, you'll be comfortable navigating your filesystem, installing packages, and setting up Python environments 🚀

## What is a Command Line Interface (CLI)?
The CLI is a way to interact with your computer by writing instead of clicking on icons and menus. Think of it as texting your computer - you type a command, press Enter, and the computer responds.

### Why Use the CLI?
- **Speed**: Once you learn the commands, it's often faster than using a graphical interface
- **Remote access**: You can control computers remotely through the CLI without having to sit next to the computer with a mouse.
- **Automation**: You can write scripts that combine commands to automate repetitive tasks. 

Ex: I once wrote a script combining 700 lines of individual commands to launch my employer's investing app on Microsoft Azure. Imagine me trying to click on 700 different icons in exactly the right order every time instead! 😱

## Basic CLI Commands

Let's start with the most fundamental command - seeing what's in your current location AKA directory:

```bash
# List files/folders in current directory
ls
```

Most CLI commands can be modified with **flags** (also called options). Flags start with a dash (`-`) and change how the command behaves. Think of them like settings or preferences for that command.

```bash
# Basic command - just shows file and folder names
ls

# Add the -l flag for "long format" - shows more details like file sizes and dates
ls -l

# Add the -a flag for "all" - shows hidden files too (files starting with .)
ls -a

# Flags can have longer equivalents that start with two dashes
ls --all

# Combine flags together - shows all files in long format
ls -la
```

The pattern is: `command -f`, `command -flag1 -flag2`, or `command -flag1flag2`

### Navigation Commands
```bash
# Show your current folder (print working directory)
pwd

# Change directory (like opening different folders)
cd Documents
cd ..          # Go up one level (like clicking "back" in a file explorer)
cd ~           # Go to your home directory 
cd /           # Go to the root directory (contains all other folders)

# Absolute filepaths specify a folder starting from the root
cd /home/user/Documents

# Relative filepaths specify a folder starting from the current folder
cd /home
cd ./user

```

### Getting Help When You're Stuck

The CLI has built-in help systems. This or AI models are quick ways to recall which options you need for any command

```bash
# Get a manual page for any command (press 'q' to quit)
man ls

# We'll install this later, but tldr has shorter examples than man
tldr ls

# Quick help - many commands have this built-in
ls --help
ls -h

# Check what version of a command you have
# (usually to check things installed properly)
ls --version
```

## Exercise 1: Your First CLI Adventure 🗺️

Let's practice these basic commands! Follow along step by step:

1. **Find out where you are:**
   ```bash
   pwd
   ```

2. **See what's around you:**
   ```bash
   ls
   ls -l
   ls -la
   ```

3. **Create your workshop workspace:**
   ```bash
   mkdir practice
   ```

4. **Move into your new folder:**
   ```bash
   cd practice
   pwd  # Confirm you moved
   ```

5. **Try the help system:**
   ```bash
   ls --help  # See all the options for ls
   ```

**Challenge:** Figure out two flags you need for the `ls` command to see the size of each file in human-readable format in a directory.

## Working with Files and Directories

Now let's learn to create and manipulate files:

```bash
# Create a new directory (like making a new folder)
mkdir my-data-folder

# Create a new empty file (like creating a blank document)
touch hello.txt

# List everything to see your creations
ls -la
```

### Downloading Files from the Internet

Two common commands for downloading files from the Internet are `curl` and `wget`. The difference between them is mainly in the flags you use with each.

```bash
# Fetch the content on a webpage with curl
curl http://wttr.in/Toronto

# Download a file with wget (saves with original name)
wget http://wttr.in/Toronto

# Download and save with a different name using curl
curl -o my-data.csv https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv
```

### Viewing and Manipulating Files

```bash
# Display entire file content (like opening a text file)
cat Toronto

# Display file content page by page (good for large files)
less my-data.csv  # Press 'q' to quit, use arrows to scroll

# Display first few lines (preview the beginning)
head my-data.csv

# Display last few lines (see the end)
tail my-data.csv

# Copy files (like copy-paste)
cp hello.txt hello-backup.txt

# Move/rename files (like cut-paste or renaming)
mv hello.txt greeting.txt

# Remove files (WARNING: PERMANENT - no recycling bin)
rm greeting.txt
```

## CLI Operators: Connecting Commands Together

The real power of CLI comes from connecting commands together using **operators**. Think of math operators like addition or subtraction that make individual numbers more useful.

### The Pipe Operator (`|`)
The pipe takes the output of one command and feeds it as input to another command, like a assembly line:

```bash
# Count how many lines are in a file with the word count command and the lines flag
cat my-data.csv | wc -l

# See the first 5 lines and count how many words are in them
head -5 my-data.csv | wc

# Get help and search for specific words
ls --help | grep "size"  # grep is like ctrl+F

# Sidenote: You can also use grep to search all files in a directory by specifying a search term to Ctrl+F, a location, and the recursive flag. 
grep "search-term" ./ -r
```

### Output Redirection (`>` and `>>`)
These operators let you save command output to files instead of displaying it on screen:

```bash
# Save the output to a file (overwrites existing content)
ls -la > file-list.txt
cat file-list.txt  # See what was saved

# Append output to a file (adds to existing content) - useful for quick additions
echo "This is a new line" >> file-list.txt
cat file-list.txt
```

### Text Editors for Writing Code

While you can append to files with `>>`, when writing actual code, it's much better to use a **text editor**. You might have heard of popular ones like VSCode. Today, we'll use simpler ones like `nano`.

```bash
# nano is a simple, beginner-friendly text editor
nano filename.py

# Basic nano controls:
# Ctrl+X : Exit (it will ask if you want to save)
# Ctrl+O : Save without exiting
# Ctrl+K : Cut/delete a line
# Ctrl+U : Paste the cut line
```

### Input Redirection (`<`)
This feeds the contents of a file as input to a command:

```bash
# Count lines in a file (alternative way)
wc -l < my-data.csv
```

### Command Chaining (`&&` and `||`)
These let you run multiple commands in sequence:

```bash
# Run second command only if first succeeds (AND logic)
mkdir new-folder && cd new-folder && pwd

# Run second command only if first fails (OR logic)
ls nonexistent-file.txt || echo "File not found!"

# Chain multiple operations
touch test.txt && echo "File created" && ls test.txt
```

## Exercise 2: Data Exploration

1. **Get the weather report and find appearances of the word 'sunny'** using `grep` and `curl http://wttr.in/Toronto`. Sidenote: `http://wttr.in/Toronto` is what we call an API (application programming interface). It's like normal URLs that you visit in your browser, except it returns data instead of websites.  

2. **Count how many times the word 'sunny' appears in the weather report** using `grep`, `wc`, and `curl http://wttr.in/Toronto`. Hint: You'll need the `-w` flag for `wc`

3. **Challenge: show how often every word is used in the weather report**. Hint: `curl http://wttr.in/Toronto | tr -cs '[:alpha:]' '\n'` uses the translate command `tr` to translate the raw text into individual words (you can search up the details of the flags if youd' like). You can then use the `sort` and `uniq` commands to sort and count the unique words.

## Common CLI Tips and Tricks

### Shortcuts to Save Time:
- **Tab completion**: Start typing a filename or command and press Tab to auto-complete
- **History**: Use the up/down arrow keys to navigate through previous commands
- **Ctrl+C**: Stop a running command (like hitting the "stop" button)
- **Ctrl+L**: Clear the screen (same as typing `clear`)
- **Ctrl+A**: Move cursor to beginning of line
- **Ctrl+E**: Move cursor to end of line

### Wildcards (Pattern Matching):
```bash
# List all .txt files
ls *.txt

# List all files starting with 'data'
ls data*

# Copy all Python files to a folder
cp *.py my-scripts/
```

## Troubleshooting Common Issues

### "Command not found"
- Make sure you spelled the command correctly
- The package might not be installed
- Check if you're in the right directory

### "Permission denied"
- You might need `sudo` for system-wide installations
- Check file/directory permissions with `ls -l`


-----
For the next part on package managers, open the file called `SetupPython.md` to install the tools you need and then `PackageManagers.md` for the workshop content. 