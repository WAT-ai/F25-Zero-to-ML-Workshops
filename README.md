# Workshop 1 (Command Line Interface)
![Image created with `gpt-image-1`](./Banner.png)
_Image created with `gpt-image-1` to suit our theme_

## Contents
This repository contains all the lessons for WAT.ai's Fall 2025 Zero to ML workshop series. These workshops are intended for students without any coding experience. **We teach the following concepts**: 
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

```bash
git clone https://github.com/WAT-ai/F25-Zero-to-ML-Workshops.git
``` 

Next, you need to 'open' the downloaded folder (directory). In the past, you've done this with 'file explorer' applications. Now, you'll do it with the change directory (cd) command in the CLI. To open the downloaded directory, run: 

```bash
cd F25-Zero-to-ML-Workshops
```

Finally, you're ready to start the first workshop! We've organised different workshops' content in different 'branches' of this repository. These are basically like different 'versions' of the folder you've downloaded. You can switch between (AKA 'check out') different branches by entering the following command in your CLI:

```bash
git checkout <branch-name>
```

We'll learn more about branches soon. For now, know that you can open the first workshop by running:

```bash
git checkout workshop-1
```

You can also come back to this main branch by running:

```bash
git checkout main
```

We'll see you at the first workshop soon!