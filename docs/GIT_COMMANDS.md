# Experiment 1: Git Commands Cheat Sheet (practice and screenshot these)

## Setup
    git config --global user.name "Archita"
    git config --global user.email "you@email.com"
    git init
    git remote add origin https://github.com/<username>/stms.git

## Daily workflow
    git status
    git add .
    git commit -m "STMS-1: add task feature"
    git push -u origin main
    git pull

## Branching
    git branch
    git checkout -b feature/STMS-2-edit-delete
    git checkout main
    git merge feature/STMS-2-edit-delete
    git branch -d feature/STMS-2-edit-delete

## Inspect
    git log --oneline --graph --all
    git diff
    git show <commit-id>

## Undo / save work
    git stash
    git stash pop
    git revert <commit-id>
    git reset --soft HEAD~1
    git tag v1.0
    git push origin v1.0

## Merge conflict demo (do this once and screenshot it)
    git checkout -b branch-a
    # edit line 1 of README.md -> "Version A"
    git commit -am "STMS-12: version A"
    git checkout main
    git checkout -b branch-b
    # edit the SAME line -> "Version B"
    git commit -am "STMS-12: version B"
    git checkout branch-a
    git merge branch-b       # CONFLICT
    # open README.md, remove <<<<<<< ======= >>>>>>> markers, keep what you want
    git add README.md
    git commit -m "STMS-12: resolve merge conflict"
