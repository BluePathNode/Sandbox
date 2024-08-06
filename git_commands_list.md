
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
   git add file1.txt file2.txt file3.txt
   git add .  
   git add src/
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

19. **View a file's history:**
    ```bash
    git log -- <file>
    ```
    📜 See the commit history of a specific file.

20. **Search commit messages:**
    ```bash
    git log --grep="<search-term>"
    ```
    🔍 Find commits containing a specific keyword in the message.

21. **View the history of a line in a file:**
    ```bash
    git blame <file>
    ```
    🕵️‍♂️ See who made changes to each line of a file.

## 🗃️ Stashing Changes

22. **Stash your changes:**
    ```bash
    git stash
    ```
    👜 Save your changes temporarily.

23. **List stashes:**
    ```bash
    git stash list
    ```
    🗂️ See all your stashes.

24. **Apply the latest stash:**
    ```bash
    git stash apply
    ```
    📂 Reapply your stashed changes.

25. **Apply a specific stash:**
    ```bash
    git stash apply stash@{n}
    ```
    📂 Apply a specific stash from the list.

26. **Drop a stash:**
    ```bash
    git stash drop stash@{n}
    ```
    🗑️ Remove a specific stash.

27. **Pop the latest stash:**
    ```bash
    git stash pop
    ```
    📤 Apply and remove the latest stash.

## ⏪ Undoing Changes

28. **Unstage a file:**
    ```bash
    git reset HEAD <file>
    ```
    ⏸️ Remove a file from the staging area.

29. **Revert changes in a file:**
    ```bash
    git checkout -- <file>
    ```
    ↩️ Discard changes in your working directory.

30. **Reset to a previous commit (destructive):**
    ```bash
    git reset --hard <commit-hash>
    ```
    ⚠️ Revert your repository to an earlier state.

31. **Reset to a previous commit (safe):**
    ```bash
    git reset --soft <commit-hash>
    ```
    ⏪ Keep changes in working directory but move HEAD.

32. **Revert a specific commit:**
    ```bash
    git revert <commit-hash>
    ```
    🔄 Create a new commit that undoes the changes from a previous commit.

## 🚫 Ignoring Files

33. **Create a `.gitignore` file:**
    ```bash
    # Ignore all .log files
    *.log

    # Ignore the node_modules directory
    node_modules/
    ```
    🛡️ Tell Git which files to ignore.

## 🏷️ Tagging

34. **Create a new tag:**
    ```bash
    git tag <tag-name>
    ```
    🏷️ Mark important points in your project's history.

35. **Push a specific tag:**
    ```bash
    git push origin <tag-name>
    ```
    🚀 Share your tags with the remote repository.

36. **List tags:**
    ```bash
    git tag
    ```
    📋 See all tags in the repository.

37. **Delete a tag:**
    ```bash
    git tag -d <tag-name>
    ```
    🗑️ Remove a tag from the local repository.

38. **Delete a remote tag:**
    ```bash
    git push origin --delete <tag-name>
    ```
    🗑️ Remove a tag from the remote repository.

## 🕶️ Aliases

39. **Create useful Git aliases to save time:**
    ```bash
    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.ci commit
    git config --global alias.br branch
    ```
    🏎️ Speed up your workflow with shortcuts.

## 🔍 Checking Differences

40. **Check differences between working directory and staging area:**
    ```bash
    git diff
    ```
    🔍 See what changes are not yet staged.

41. **Check differences between staging area and the last commit:**
    ```bash
    git diff --cached
    ```
    🧐 Review changes that are staged for commit.

42. **Check differences between two commits:**
    ```bash
    git diff <commit-hash-1> <commit-hash-2>
    ```
    📊 Compare changes between two commits.

## 🗑️ Deleting Files

43. **Delete a file from the repository and stage the deletion:**
    ```bash
    git rm <file>
    ```
    🗑️ Remove a file from both your working directory and the repository.

44. **Commit the deletion with a message:**
    ```bash
    git commit -m "Delete <file>"
    ```
    💬 Commit the removal of the file with a message.

45. **Push the deletion to the remote repository:**
    ```bash
    git push
    ```
    📤 Update the remote repository to reflect the deletion.

## 🛠️ Advanced Commands

46. **Cherry-pick a commit:**
    ```bash
    git cherry-pick <commit-hash>
    ```
    🍒 Apply the changes from a specific commit to the current branch.

47. **Squash commits:**
    ```bash
    git rebase -i HEAD~<number-of-commits>
    ```
    🎯 Combine multiple commits into one.

48. **Bisect to find a bug:**
    ```bash
    git bisect start
    git bisect bad
    git bisect good <commit-hash>
    ```
    🔍 Use binary search to find the commit that introduced a bug.

49. **Add a submodule:**
    ```bash
    git submodule add <repository-url>
    ```
    📦 Include a repository inside another repository.

50. **Update submodules:**
    ```bash
    git submodule update --remote
    ```
    🔄 Update the submodules to the latest commit.

51. **Remove a file from Git tracking but keep it locally:**
    ```bash
    git rm --cached <file>
    ```
---