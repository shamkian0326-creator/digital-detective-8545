# Mission 6 — Work with versions and a pull request

## 1. Task / objective

Practise staging, committing and reviewing history. Use a branch and pull request to propose a change to the README.

## 2. Work completed

Checked status and history, created `update-about`, and added a **My Learning** section to the root README. Staged just `README.md`, made a commit, published the branch, and reviewed the proposed change before returning to `main`.

## 3. Commands / tools used

| Operation | Example | Purpose |
| --- | --- | --- |
| Initialize | `git init --initial-branch=main` | Creates the repository and sets its initial branch name. |
| Check status | `git status --short --branch` | Shows the branch and what files are changed or staged. |
| Stage | `git add -- README.md` | Selects the current version of the root README for the next snapshot. |
| Commit | `git commit -m "Add three takeaways to My Learning"` | Creates a named snapshot of the staged content. |
| Inspect history | `git log -3 --oneline` | Shows the latest three commit identifiers and subjects. |
| Create or list branches | `git switch -c update-about` and `git branch` | Creates and enters a new branch, or lists the available local branches. |
| Switch branches | `git switch main` | Changes to the main branch and updates the working files. |
| Publish | `git push -u origin update-about` | Sends the branch to GitHub and saves its upstream setting. |
| Retrieve | `git fetch origin` and `git pull --ff-only` | Fetch downloads remote objects and updates remote-tracking references. Pull also updates the current branch if it can fast-forward. |

GitHub CLI opened the pull request, showed the diff and checked its status.

## 4. My understanding

Staging collects the exact file changes for the next snapshot. Committing stores that snapshot in the branch history. A branch lets people make changes alongside work on the main line. A pull request gives them a shared view of the proposed changes where they can review and discuss changes before integration.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[Published branch](https://github.com/shamkian0326-creator/digital-detective-8545/tree/update-about) and [pull request #1](https://github.com/shamkian0326-creator/digital-detective-8545/pull/1). The pull request from `update-about` into `main` is open for review.

## 8. Commit details

`Document the branch and pull request workflow`. The checkpoint is listed in [this mission's GitHub history](https://github.com/shamkian0326-creator/digital-detective-8545/commits/main/mission-06-git-github/README.md).
