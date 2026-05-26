# Spring 2026 Zero to ML Workshops
![Image created with `gpt-image-1`](./Banner.png)
_Image created with `gpt-image-1`_

## Contents
This repository contains all the lessons for WAT.ai's Spring 2026 Zero to ML workshop series. These workshops are intended for students without any coding experience. **We teach the following concepts**: 
1. The command line and package management
2. Version control, git, and github
3. Object oriented programming with Python
4. Data exploration and visualisation with Pandas
5. Creating chatbots with Langchain
6. Types of machine learning (supervised, unsupervised, RL)
7. Shallow ML models (regression, decision trees, etc.)
8. Perceptrons and basic neural networks

## Prerequisites
To get started, **you'll need a Bash command line interface (CLI) and git installed**. The CLI is what we'll use throughout the workshop series to run commands, run code that we write, and download the tools (packages) we need. git is a tool that allows you to download a copy of this repository (published by other people on the WAT.ai team) and make your own changes. We'll learn more about the CLI and git in the first two workshops.

Some recommended ways to get a CLI and git are listed below for different operating systems.

### Windows
The most professional option is to install Windows Subsystem for Linux (WSL2) and use an Ubuntu distribution. However, this involves more steps, especially on laptops from before 2019. Here is a [follow-along video](https://www.youtube.com/watch?v=vxTW22y8zV8), [official docs](https://learn.microsoft.com/en-us/windows/wsl/install), and [a Claude conversation on things you'll find confusing if you've never heard of a CLI or Linux](https://claude.ai/share/eb49ba23-9d12-4d8e-bcb7-6ce20e8bfe1e). 
- ⚠️ **Be careful if you get any errors related to 'virtualization'**. If this happens, you'll need to modify settings in your BIOS. **If you don't know what BIOS is, probably don't do this** as any mistakes made in BIOS settings can break your computer.

An alternative is to **simply use an emulated Linux CLI. This is fine for the first 4-5 workshops** if you'd like help installing WSL2 later. Some options are:
- [Replit on any browser](https://replit.com/)
- [Termux on your Android smartphone](https://play.google.com/store/apps/details?id=com.termux&pli=1)
- [iSH on your iPhone](https://apps.apple.com/us/app/ish-shell/id1436902243)

### MacOS
You can simply open the Terminal application (installed by default) to access a CLI. Then, install [Homebrew via instructions on their website](https://brew.sh/). Homebrew is a package manager for MacOS which lets you download tools we'll be using. Finally, run `brew install git` in the Terminal application to install git.

### Linux
Laugh at the others who have to do 'setup' and 'installation' and 'workarounds'. 😈

## Usage
To get started, install this repository by running the following command in your CLI. It downloads all the files from the Github repository into a folder (directory) on your computer.

This is a branch to submit your first pull request. Steps: 
1. Fork this repository by visiting [the main Github page for this repo](https://github.com/WAT-ai/F25-Zero-to-ML-Workshops) and clicking the Fork button on the top right. 
2. Wait for Github to take you to your forked repository. Then, clone it by running
```bash
git clone <forked-repo-url>
```
3. Switch to the `jokes` branch in your cloned repository by running: 
```bash
git checkout jokes
```
4. Create a file called `<firstname>-<lastinitial>.txt` and add a joke to it using `nano`: 
```bash
nano <firstname>-<lastinitial>.txt
```
5. Save and exit nano (Ctrl+O, Enter, Ctrl+X).
6. Commit and push your changes: 
```bash
git add <firstname>-<lastinitial>.txt
git commit -m "Added a joke"
git push origin jokes
```
7. To create a pull request, go to your forked repository website on Github. You should see a "Compare & pull request" button on the top right. Click it.
8. Add a description of your changes and click "Create pull request".
9. Make sure you target the `jokes` branch of the original repository and your forked repository (not `main`).

**Note:** this pull request seems trivial. In real life, you could fork open-source projects and make more substantial changes like new features or bug fixes. This is just a simple exercise to get you familiar with the process of contributing to open-source projects on GitHub. Remember - the **key steps are fork, clone, create a branch, make changes, commit, push, and create a pull request.**