# Workshop 1B: Command Line Interfaces and Package Management
![Terminal with colorful output](./CLIBanner.png)
_Welcome to the command line - your new superpower!_

## Package Managers: Your Supermarket of Tools

Imagine you want to cook a complex recipe. Instead of going to different stores to buy each ingredient individually, you go to one supermarket that has everything organized and ready. **Package managers are like that supermarket for software** - they handle finding, downloading, and installing programs for you. 

Also, let's say you buy a food processor, but you also need to buy replacement blades for it to work. This is called a 'dependency'. Package managers automatically track dependencies for you so that any tools you download come with other prerequisites taken care of.

### System Package Managers

Think of system package managers as the "app store" for your operating system. You need `sudo` (superuser do) to give permissions to install these packages:

```bash
# Update the list of available packages (checks what's new but doesn't download)
sudo apt update

# Install a package (downloads and sets it up)
sudo apt install package-name

# Remove a package (uninstalls it)
sudo apt remove package-name

# Search for packages (find software by keyword)
apt search keyword
```

**Note for macOS users:** Replace `apt` with `brew` in all commands above. The concepts are identical!

## Exercise 3: Fun Package Installation Party 🎉

Let's install some entertaining packages to get comfortable with package managers:

1. **Update your package list first:**
   ```bash
   sudo apt update
   ```

2. **Install some fun packages:**
   ```bash
   sudo apt install cowsay fortune-mod lolcat
   ```

3. **Try out your new toys:**
   ```bash
   # Make a cow say something
   cowsay "Hello from the command line!"
   
   # Get a random quote
   fortune
   
   # Combine them with a pipe!
   fortune | cowsay
   
   # Add colors to any text
   echo "Rainbow text!" | lolcat
   fortune | cowsay | lolcat
   ```

4. **Explore command options:**
   ```bash
   # See what animals cowsay can use
   cowsay -l
   
   # Try a different animal
   cowsay -f dragon "Roar"
   
   # Get help on any command
   cowsay --help
   ```

**Challenge:** Try creating a chain of commands that generates a fortune, displays it with cowsay using a random animal, colors it with lolcat, and saves it to a file!

## Python and Package Management

Now let's talk about Python specifically. You might wonder: "Why do we need special Python package managers when we already have system package managers?"

**Here's the problem:** Imagine you're working on two different projects. Project A needs version 1.0 of a library, but Project B needs version 2.0 of the same library. With system-wide installation, you can only have one version installed! It's like trying to have both iOS 15 and iOS 16 on the same phone - they conflict.

**The solution:** Virtual environments! Think of them as separate, isolated boxes where each project can have its own versions of everything without interfering with other projects.

### Understanding Python Commands

First, let's see that `python3` is just another command you can run:

```bash
# Run Python directly (interactive mode)
python3

# Exit Python (or press Ctrl+D)
exit()

# Run Python code directly from command line
python3 -c "print('Hello from Python!')"

# Check Python version
python3 --version
```

### Virtual Environments with venv

Let's break down what these commands actually do:

```bash
# Create a virtual environment
# python3: Run Python
# -m venv: Use the venv module (m stands for module)
# my-ml-project: Name of the folder to create for this environment
python3 -m venv my-ml-project

# Activate the virtual environment
# source: Run the script in the current session
# This script changes your environment to use the virtual environment's Python
source my-ml-project/bin/activate

# You'll see (my-ml-project) appear in your prompt - that means it's active!

# Now when you run python3, you're using the environment's Python
python3 -c "print('I am running in a virtual environment!')"

# Deactivate when you're done (goes back to system Python)
deactivate
```

### Installing Python Packages with pip

Once you have a virtual environment active, you can install packages that only exist in that environment:

```bash
# Install a package (only in the active virtual environment)
pip install package-name

# Install multiple packages at once (stick to small, useful ones while learning)
pip install requests colorama

# List what's installed in this environment
pip list

# Show detailed information about a package
pip show numpy

# Uninstall a package
pip uninstall package-name

# Save your environment's packages to a file (like a shopping list)
pip freeze > requirements.txt

# Install packages from someone else's requirements file
pip install -r requirements.txt
```

## Exercise 4: Python Environment Setup 🐍

Let's create a proper Python environment and run some code:

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv my-first-env
   source my-first-env/bin/activate
   # Notice (my-first-env) appears in your prompt!
   ```

2. **Verify you're in the environment:**
   ```bash
   python3 -c "print('Hello from my virtual environment!')"
   python3 --version
   ```

3. **Install a small, fun package:**
   ```bash
   pip install cowsay  # This is a tiny, fun package - perfect for learning!
   pip list  # See what's installed
   ```

4. **Use Python from the command line:**
   ```bash
   python3 -c "import cowsay; cowsay.cow('Python is awesome!')"
   ```

5. **Create a simple Python script using a text editor:**
   
   While you can append to files with `>>`, for writing code it's better to use a text editor. `nano` is a simple, beginner-friendly editor built into most systems:
   
   ```bash
   nano hello.py
   ```
   
   In nano, type this Python code:
   ```python
   print('This is my first Python script!')
   import cowsay
   cowsay.cow('Scripts are cool!')
   ```
   
   To save and exit nano: Press `Ctrl+X`, then `Y` to confirm, then `Enter` to save.

6. **Run your script:**
   ```bash
   python3 hello.py
   ```

7. **Save your environment setup:**
   ```bash
   pip freeze > requirements.txt
   cat requirements.txt  # See what was saved
   ```

8. **Practice deactivating and reactivating:**
   ```bash
   deactivate
   # Notice (my-first-env) disappears from your prompt
   
   source my-first-env/bin/activate
   # It's back!
   ```

9. **Clean up when you're done (optional):**
   ```bash
   deactivate  # Make sure you're out of the environment first
   rm -rf my-first-env  # Delete the entire virtual environment folder
   # Now it's completely gone - you'd need to recreate it to use it again
   ```

**Challenge:** Can you create a second virtual environment with different packages and switch between them?

## Troubleshooting Common Issues

### Virtual Environment Issues
- Make sure you activated the environment (look for the name in parentheses in your prompt)
- Check that you're using the right Python version
- Try recreating the environment if things get messy

### Package Installation Fails
- Update your package manager first (`sudo apt update`)
- Check your internet connection
- Some packages might have different names or not be available

## What's Next?

Congratulations! You've just learned the fundamental skills that will power everything else we do in this workshop series. The command line might feel awkward at first, but with practice, it becomes second nature.

In our next workshop, we'll dive into **version control with git and GitHub**, where you'll learn how to:
- Track changes in your code
- Collaborate with others
- Never lose your work again
- Contribute to open-source projects

### Homework (Optional but Recommended):
1. Look up a fun Linux command to play with
2. Experiment with combining commands using pipes (`|`) and redirection (`>`)
3. Create virtual environments and install some fun python package to play with.

### Resources for Further Learning:
- [Command Line Crash Course](https://learnpythonthehardway.org/python3/appendixa.html)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- Install `tldr` for quick command examples: `sudo apt install tldr` then run `tldr ls`

Remember: **Everyone was a beginner once!** The command line is a skill that will serve you throughout your programming journey. Don't worry if it feels overwhelming at first - you're building a superpower! 💪

---

*See you at Workshop 2: Version Control, Git, and GitHub!* 🚀

To switch to the second workshop, run 
```bash
git checkout workshop-2
```

To go back to the main page, run
```bash
git checkout main
```