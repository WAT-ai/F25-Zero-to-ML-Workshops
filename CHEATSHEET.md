# GitHub Cheat Sheet
*Your pocket guide to saving, sharing, and fixing code.*


## The Daily Workflow
*Do this every time you sit down to work.*

### 1. Start Your Day (Sync)
Always get the latest changes from the team before you start coding.
```bash
git checkout main          # Go to the main branch
git pull origin main       # Download updates from GitHub

```

### 2. Start a New Task (Branch)

Never work directly on `main`. Create a safe space for your changes.

```bash
# Create and switch to a new branch
git checkout -b feat/my-new-feature

```

### 3. Save Your Work (Stage & Commit)

Think of this like "Saving" in a video game.

```bash
git status                 # Check which files you changed (Red = Modified)
git add .                  # Stage ALL changes (Turn them Green)
git commit -m "Add login button"  # Save the snapshot with a message

```

### 4. Share Your Work (Push)

Upload your save file to the cloud (GitHub).

```bash
git push origin feat/my-new-feature

```

*(If it's your first push on this branch, Git might ask you to run a command to set 'upstream'. Just copy-paste what it tells you!)*

---

## Panic Buttons

| I want to... | Command | Explanation |
| --- | --- | --- |
| **Undo file changes** | `git checkout -- filename.py` | **Safe.** Discards changes in a specific file. Returns it to the last committed state. |
| **Unstage a file** | `git reset HEAD filename.py` | **Safe.** You added a file by accident but haven't committed it yet. Takes it out of the "Box". |
| **Undo last commit** | `git reset --soft HEAD~1` | **Safe.** Undoes the "Save", but **keeps your code**. Great for fixing a typo in the commit message. |
| **Destroy recent work** | `git reset --hard HEAD~1` | **⚠️ DANGER.** Completely deletes the last commit and all work associated with it. **Cannot be undone.** |

---

## Checking Your Status

| Command | What it shows |
| --- | --- |
| `git status` | **The Dashboard.** Shows which branch you are on and which files are modified/staged. |
| `git log --oneline` | **The History.** Shows a simple list of past commits (IDs and messages). |
| `git diff` | **The Microscope.** Shows the exact lines of code you changed but haven't added yet. |
| `git branch` | **The Map.** Lists all local branches. The one with `*` is where you are now. |

---

## Key Concepts

* **Repository (Repo):** The folder where your project and its history live.
* **Remote (Origin):** The version of your repo that lives on GitHub.
* **Stage:** Moving a file from "Draft" to "Ready to Commit".
* **Commit:** Permanently saving the staged files to the history.
* **Merge Conflict:** When two people change the exact same line of code. You have to open the file and choose which version to keep.

```

```
