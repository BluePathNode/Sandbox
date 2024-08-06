
# 🎉 Git Commands Cheat Sheet 🎉

## 🚀 Basic Commands

1. **Initialize a new Git repository:** 
   ```bash
   git init
   ```
   ✨ Start tracking your project with Git!

2. **Clone an existing repository:**
   ```bash
   git clone <repository-url>
   ```
   🌟 Make a copy of a remote repository on your local machine.

3. **Check the status of your working directory:**
   ```bash
   git status
   ```
   🕵️‍♂️ See which files have been modified.

4. **Add files to the staging area:**
   ```bash
   git add <file>
   git add .
   ```
   📥 Stage your changes for the next commit.

5. **Commit your changes with a message:**
   ```bash
   git commit -m "Your commit message"
   ```
   💬 Save your changes in the repository with a descriptive message.

## 🌳 Branch Management

6. **List all branches:**
   ```bash
   git branch
   ```
   📋 See all branches in your repository.

7. **Create a new branch:**
   ```bash
   git branch <branch-name>
   ```
   🌱 Start working on something new without affecting the main branch.

8. **Switch to a different branch:**
   ```bash
   git checkout <branch-name>
   ```
   🔄 Move to another branch.

9. **Create and switch to a new branch:**
   ```bash
   git checkout -b <branch-name>
   ```
   🚀 Create a new branch and start working on it immediately.

10. **Delete a branch:**
    ```bash
    git branch -d <branch-name>
    git branch -D <branch-name>
    ```
    🗑️ Clean up branches you no longer need.

## 📤 Pushing and Pulling

11. **Set up a remote repository:**
    ```bash
    git remote add origin <repository-url>
    ```
    🌐 Connect your local repository to a remote one.

12. **Push changes to a remote repository:**
    ```bash
    git push -u origin <branch-name>
    git push
    ```
    📤 Send your commits to the remote repository.

13. **Pull changes from a remote repository:**
    ```bash
    git pull
    ```
    📥 Get the latest changes from the remote repository.

## 🔄 Merging and Rebasing

14. **Merge a branch into the current branch:**
    ```bash
    git merge <branch-name>
    ```
    🌈 Combine changes from another branch.

15. **Rebase the current branch onto another branch:**
    ```bash
    git rebase <branch-name>
    ```
    🛠️ Reapply commits on top of another base tip.

## 🔍 Viewing History

16. **View commit history:**
    ```bash
    git log
    ```
    📜 See a list of all commits in the current branch.

17. **View commit history with a graph:**
    ```bash
    git log --graph --oneline --all
    ```
    🌳 Visualize your commit history.

18. **View changes made in a specific commit:**
    ```bash
    git show <commit-hash>
    ```
    🔍 Inspect the details of a particular commit.

## 🗃️ Stashing Changes

19. **Stash your changes:**
    ```bash
    git stash
    ```
    👜 Save your changes temporarily.

20. **List stashes:**
    ```bash
    git stash list
    ```
    🗂️ See all your stashes.

21. **Apply the latest stash:**
    ```bash
    git stash apply
    ```
    📂 Reapply your stashed changes.

## ⏪ Undoing Changes

22. **Unstage a file:**
    ```bash
    git reset HEAD <file>
    ```
    ⏸️ Remove a file from the staging area.

23. **Revert changes in a file:**
    ```bash
    git checkout -- <file>
    ```
    ↩️ Discard changes in your working directory.

24. **Reset to a previous commit (destructive):**
    ```bash
    git reset --hard <commit-hash>
    ```
    ⚠️ Revert your repository to an earlier state.

## 🚫 Ignoring Files

25. **Create a `.gitignore` file:**
    ```bash
    # Ignore all .log files
    *.log

    # Ignore the node_modules directory
    node_modules/
    ```
    🛡️ Tell Git which files to ignore.

## 🏷️ Tagging

26. **Create a new tag:**
    ```bash
    git tag <tag-name>
    ```
    🏷️ Mark important points in your project's history.

27. **Push a specific tag:**
    ```bash
    git push origin <tag-name>
    ```
    🚀 Share your tags with the remote repository.

## 🕶️ Aliases

28. **Create useful Git aliases to save time:**
    ```bash
    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.ci commit
    git config --global alias.br branch
    ```
    🏎️ Speed up your workflow with shortcuts.

## 🔍 Checking Differences

29. **Check differences between working directory and staging area:**
    ```bash
    git diff
    ```
    🔍 See what changes are not yet staged.

30. **Check differences between staging area and the last commit:**
    ```bash
    git diff --cached
    ```
    🧐 Review changes that are staged for commit.

## 🗑️ Deleting Files

31. **Delete a file from the repository and stage the deletion:**
    ```bash
    git rm <file>
    ```
    🗑️ Remove a file from both your working directory and the repository.

32. **Commit the deletion with a message:**
    ```bash
    git commit -m "Delete <file>"
    ```
    💬 Commit the removal of the file with a message.

33. **Push the deletion to the remote repository:**
    ```bash
    git push
    ```
    📤 Update the remote repository to reflect the deletion.
