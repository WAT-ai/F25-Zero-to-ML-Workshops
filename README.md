## Jokes

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