basic git
======
Create empty Git repo in specified directory
```
git init
```
List which files are staged, unstaged, and untracked
```
git status
```
Stage all changes in <directory> for the next commit
```
git add <directory>
```
Commit the staged snapshot, but instead of launching a text editor, use <message> as the commit message
```
git commit -m "<message>"
```
Create a new connection to a remote repo
```
git remote add <name> <url>
```
Push the branch to <remote>, along with necessary commits and objects
```
git push <remote> <branch>
```
Fetch the specified remote’s copy of current branch and immediately merge it into the local copy.
```
git pull <remote>
```
pre-commit
======
documentation : https://pre-commit.com/
Installation
------------
```
pip install pre-commit
```

##Add a pre-commit configuration
create a file named .pre-commit-config.yaml
```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace

```

##install the git hook scripts
```
pre-commit install
```
 pre-commit will run automatically on git commit!
