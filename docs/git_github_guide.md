# Git and GitHub: a beginner guide for this course

This guide assumes no previous experience with Git. Students use **GitHub Desktop**, not terminal
Git commands, for their normal work. The more technical setup is placed in the teacher appendix.

The aim is simple:

- the teacher maintains one canonical course repository;
- one student representative creates the group's own GitHub repository;
- students save only to their group repository;
- teacher updates can be copied into the group repositories;
- student work never changes the canonical repository.

## The five ideas students need

| Word | Plain-language meaning |
|---|---|
| repository | the project folder together with its saved history |
| clone | make the first copy of the group repository on your computer |
| commit | save a named checkpoint of your changes on your computer |
| push | send your commits to the group's GitHub repository |
| fetch/pull | receive commits that another group member has pushed |

You do not need to understand branches, remotes, rebasing or command-line Git to begin the course.

## How the course repositories are separated

```text
 Teacher's canonical repository
       course notebooks and updates
                    |
                    | teacher update
                    v
       Group A GitHub repository       Group B GitHub repository
       Group A's independent work      Group B's independent work
                    |                               |
              group members                     group members
```

The teacher shares only the canonical repository URL. One student representative creates the
**group repository** as a fork, invites the other members, and shares the group URL. The teacher
does not create or own the group repositories and students receive no write permission to the
canonical repository.

Each group chooses one **repository caretaker**. The caretaker helps coordinate work and receives
teacher updates; this can be a rotating role.

## Before the first class

Install:

1. [GitHub Desktop](https://desktop.github.com/).
2. [Visual Studio Code](https://code.visualstudio.com/).
3. Miniconda, Anaconda or another course-approved conda installation.

Open GitHub Desktop and sign in with the GitHub account that the teacher added to the group
repository. GitHub Desktop provides a graphical interface for cloning, committing, pulling and
pushing, so do not need to memorise Git commands.

## Create the group repository

Only one student representative performs this section:

1. Open the canonical repository link supplied by the teacher.
2. Select **Fork** in the upper-right area of the GitHub page.
3. Select **Create a new fork**.
4. Choose the representative's account as the owner and use a name that identifies the group.
5. Select **Create fork**.
6. In the new group fork, open **Settings → Collaborators → Add people**.
7. Invite every group member using their GitHub username.
8. Share the URL of this fork with the group.

GitHub calls this repository a *fork* because it begins as a connected copy of the canonical
repository. It belongs to the student representative and can receive canonical updates through
**Sync fork**. GitHub permits
[collaborators on repositories owned by personal accounts](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository).

The group fork of a public canonical repository is also public. Do not upload raw data, secrets,
personal information or confidential assessment material. If the group repository must be private,
use the alternative described in the
[teacher setup guide](git_github_teacher_setup.md#private-repository-alternative).

## First-time setup for every student

### 1. Open the group repository on GitHub

Use the group-fork link supplied by the student representative. Check that its owner and repository
name identify your group. Do not clone the teacher's canonical repository as your working
repository.

### 2. Clone it with GitHub Desktop

On the GitHub repository page:

1. Select **Code**.
2. Select **Open with GitHub Desktop**.
3. Choose a local folder that you can find again.
4. Select **Clone**.

Cloning is done only once on each computer. Afterwards, open the existing local repository in
GitHub Desktop; do not clone a new copy for every class.

### 3. Open the project in VS Code

In GitHub Desktop, select **Repository → Open in Visual Studio Code**. Always open this repository
root, not only the `notebooks/` directory.

### 4. Configure the Python environment

Open a VS Code terminal at the repository root and follow the environment instructions in the
root `README.md`. Select **Python 3 (icd-project)** as the notebook kernel.

### 5. Create the group's working notebook

Do not edit files under `notebooks/lessons/`. For W06S01, run:

```powershell
python scripts/start_group_notebook.py W06S01 <group-name>
```

Replace `<group-name>` with a short name agreed by the group. Work in the newly created notebook
under `notebooks/project/`.

## The normal student routine

Use this routine at the start and end of every work session.

### At the start: receive the group's latest work

1. Open the correct repository in GitHub Desktop.
2. Confirm that **Current branch** is `main`.
3. Select **Fetch origin**.
4. If the button changes to **Pull origin**, select it.
5. Wait until GitHub Desktop says the branch is up to date.

Do this before opening and editing the notebook. It reduces the chance that two versions of the
same file are created.

### During the session: work in the group-owned folders

Students normally edit:

- `notebooks/project/`;
- `docs/`;
- `reports/`;
- group-created modules under `src/`.

Do not edit `notebooks/lessons/`. Do not add raw data, generated outputs, passwords, tokens or the
local conda environment to GitHub.

Before saving a checkpoint, run:

```powershell
python scripts/verify_repository.py
```

For notebook work, also use **Restart Kernel → Run All** and address the first error.

### At the end: commit and push

Return to GitHub Desktop:

1. Read the list of changed files on the left.
2. Untick any file that should not be included.
3. Select individual files to inspect their changes.
4. In **Summary**, write a short description, for example `Complete W06 network checks`.
5. Select **Commit to main**.
6. Select **Push origin**.
7. Tell the group that the work is available.

A commit is a labelled checkpoint. A push uploads that checkpoint to the group's GitHub repository.
Saving a file in VS Code does neither of these things.

## A simple group coordination rule

For the first weeks, avoid having two people edit the same notebook at the same time.

1. One person announces that they are editing a notebook.
2. That person fetches and pulls before starting.
3. They finish a coherent piece of work, commit it and push it.
4. The next person fetches and pulls before taking over.

Different members may work at the same time when they are clearly editing different files, such as
one person writing the research plan and another writing a report. If GitHub Desktop reports a
conflict, stop and follow the help procedure below.

## Receiving an update from the teacher

The teacher announces when an update is available. Only the group caretaker performs the update.
Other students wait until the caretaker confirms it is complete.

### If the group repository is a GitHub fork

The caretaker uses the GitHub website:

1. Make sure all current group work has been committed and pushed.
2. Open the group's repository on GitHub.
3. Select **Sync fork** above the file list.
4. Review the incoming teacher commits.
5. Select **Update branch**.
6. Open GitHub Desktop and select **Fetch origin**, followed by **Pull origin**.
7. Run `python scripts/verify_repository.py`.
8. Tell the group that the update is ready.

If GitHub reports a conflict, do not choose files at random and do not force the update. Ask the
teacher for help.

### If the group repository is not a fork

The teaching team transfers the update to the group repository. Students only need to select
**Fetch origin** and **Pull origin** in GitHub Desktop after the teacher confirms the update.

## If something goes wrong

Do not panic: a Git problem rarely means that the work has disappeared.

### GitHub Desktop reports a conflict

1. Stop editing the affected files.
2. Do not select **Force push**, **Discard changes** or delete the repository.
3. Take a screenshot of the GitHub Desktop message.
4. In VS Code, save a separate copy of any important unsaved text outside the repository.
5. Ask the group caretaker or teacher for help.

Notebook conflicts are difficult because an `.ipynb` file is structured JSON. Prevention—one
person editing a notebook at a time—is safer than attempting an improvised repair.

### Push origin is rejected

Another member probably pushed first. Select **Fetch origin**, then **Pull origin**. If GitHub
Desktop reports a conflict, stop and ask for help. Never force-push course work.

### An unexpected file appears in the changed-files list

Leave it unticked and ask before committing it. Raw datasets, generated outputs, environments and
credentials should not be uploaded.

### The wrong repository is open

In GitHub Desktop, use **Current repository** to select the group's repository. Confirm the group
name before committing or pushing.

### Work was done in a lesson notebook

Do not discard it immediately. Save a copy, tell the teacher, and move the useful work to a group
notebook under `notebooks/project/` before restoring the lesson version.

## Student checklist

### Start

- Correct group repository open.
- `main` selected.
- **Fetch origin** completed.
- **Pull origin** completed if offered.
- Correct notebook under `notebooks/project/` open.
- `icd-project` kernel selected.

### Finish

- Notebook passes **Restart Kernel → Run All**.
- Repository verifier has no failures.
- Changed-file list reviewed.
- Clear commit summary written.
- **Commit to main** completed.
- **Push origin** completed.
- Group informed.

## Optional later workflow

Branches and pull requests are useful when groups are ready for parallel work and review, but they
are not required for the initial course workflow. Introduce them only after everyone can reliably
fetch, pull, review changes, commit and push with GitHub Desktop.

## Information for teaching staff

Repository publication, group creation and update integration are intentionally absent from this
student guide. They are documented separately in the
[teacher Git and GitHub setup guide](git_github_teacher_setup.md).

## Official help

- [Clone with GitHub Desktop](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop)
- [Commit and review changes in GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
- [Fetch, pull and push in GitHub Desktop](https://docs.github.com/en/desktop/working-with-your-remote-repository-on-github-or-github-enterprise/syncing-your-branch-in-github-desktop)
- [Synchronise a fork on the GitHub website](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/syncing-a-fork)

