# Teacher setup for Git and GitHub

This document contains the repository-administration steps that students are not expected to
perform. The student-facing workflow is in the [beginner guide](git_github_guide.md).

## Recommended teaching model

Students should interact only with their group repository through GitHub Desktop. The teaching
team creates and maintains only the canonical repository. One representative from each group
creates the group repository, invites the other students and acts as the initial caretaker. The
teacher does not need to create repositories group by group.

Choose one repository arrangement before distributing links:

| Arrangement | Best when | How updates reach groups |
|---|---|---|
| Student-created fork | the canonical repository and group work may be public | caretaker uses **Sync fork** on GitHub |
| Student-created private repository | group work must be private | caretaker performs the one-time setup and later update command, with teacher support if needed |

## Publish the canonical repository

Before publishing, check `.gitignore`, run `python scripts/verify_repository.py`, and verify that
source data without redistribution rights, generated outputs, local environments and credentials
are absent from the staged files.

If the project folder is not already a Git repository:

```powershell
git init -b main
git add .
git diff --staged
git commit -m "Create course project repository"
```

Create an empty GitHub repository without an automatically generated README, licence or
`.gitignore`. Then connect and publish the existing history:

```powershell
git remote add origin <teacher-repository-url>
git remote -v
git push -u origin main
```

If `origin` already exists, inspect it with `git remote get-url origin`. Change an incorrect URL
with `git remote set-url origin <teacher-repository-url>` instead of adding a duplicate remote.

## Arrangement A: student-created fork

This is the recommended beginner arrangement when public group repositories are acceptable:

1. The teacher publishes the canonical repository and shares its URL.
2. One student representative in each group selects **Fork → Create a new fork**.
3. The representative creates the fork in their own account and gives it a group-specific name.
4. The representative opens **Settings → Collaborators → Add people** and invites the group.
5. The representative shares the group-fork URL with the other members.
6. Students clone the group fork with GitHub Desktop.
7. When an update is announced, the caretaker uses **Sync fork → Update branch** on GitHub.

No group-by-group repository action is required from the teacher. A personal repository can have
multiple collaborators, including on GitHub Free.

Fork availability and permissions depend on repository visibility, organisation settings and the
GitHub plan. Review the current [GitHub fork model](https://docs.github.com/en/pull-requests/reference/forks)
before choosing this arrangement. Private forks may not provide the same independence as public
forks.

## Private repository alternative

Public forks are unsuitable when student work must remain private. In that case, the group
representative—not the teacher—creates an empty private repository on GitHub, invites the group
members, and performs this one-time setup:

```powershell
git clone <teacher-repository-url> <group-project-folder>
Set-Location <group-project-folder>
git remote rename origin upstream
git remote add origin <group-repository-url>
git remote -v
git push -u origin main
```

The expected relationship is:

```text
origin    -> group repository    (teacher and group can push)
upstream  -> canonical repository (teacher updates originate here)
```

Ordinary students clone only the private group repository with GitHub Desktop. They do not need to
add or understand `upstream`. This alternative asks the caretaker to perform a small amount of
command-line setup, so use it only when the privacy requirement outweighs the simpler fork
workflow.

## Publish a teacher update

In the canonical repository:

```powershell
git status
python scripts/verify_repository.py
git add <intended-paths>
git diff --staged
git commit -m "Describe the teaching update"
git push origin main
```

Announce which lesson or setup files changed and whether groups must update the conda environment.
Avoid changing group-owned paths in the canonical repository.

### Deliver the update to a fork

The group caretaker opens the group fork on GitHub and selects **Sync fork → Update branch**. If
GitHub reports a conflict, the caretaker stops and asks the teaching team to resolve it.

### Deliver the update to a private group repository

The group caretaker uses the configured local copy. The teacher may guide the caretaker but does
not need to own or create the repository:

```powershell
git switch main
git pull --ff-only origin main
git fetch upstream
git log --oneline HEAD..upstream/main
git merge upstream/main
python scripts/verify_repository.py
git push origin main
```

Students then receive the completed update with **Fetch origin** and **Pull origin** in GitHub
Desktop. They never perform the upstream merge themselves.

## Conflict policy

Ownership boundaries are the primary prevention mechanism: teachers edit lesson sources and
groups edit their project copies. If an update conflicts:

1. Do not force-push.
2. Preserve any uncommitted student work before attempting a repair.
3. Inspect `git status` and resolve ordinary text files deliberately.
4. Treat notebook conflicts as teacher-assisted repairs; `.ipynb` files are structured JSON.
5. Run the repository verifier and the relevant notebooks before pushing the resolution.
6. Use `git merge --abort` if the resolution is unclear and assistance is needed.

## Release check

Test important canonical releases in a disposable folder:

```powershell
git clone <teacher-repository-url> <temporary-test-folder>
Set-Location <temporary-test-folder>
python scripts/verify_repository.py
conda env create -f environment.yml
conda activate icd-project
python -m pip install -e .
python -m ipykernel install --user --name icd-project --display-name "Python 3 (icd-project)"
```

Supply the documented raw data locally, rerun the verifier, and use **Restart Kernel → Run All**.
Remove the test folder only after confirming that it is the disposable clone.

## Official references

- [Adding existing local code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Managing remote repositories](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories)
- [Inviting collaborators to a personal repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository)
- [Synchronising a fork](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/syncing-a-fork)
- [Resolving and aborting merges](https://git-scm.com/docs/git-merge)

