# Intro into Git

Common Git Commands:
```
git init
git clone <url>
git fetch —-all
git push origin <branch name>
git pull origin <branch name>
git remote add origin <url>
git add —-all
git branch
git checkout -b <new branch name>
git commit -m “your message”
git status
```
[Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet/)

# Exercises

### Ex 1. Setup SSH Keys
- This links your computer to your GitHub acccount
- Only needs to be done once
- Execute: `ssh-keygen`
- Copy and paste public key (`id_rsa.pub`) to GitHub (Account >> Settings >> SSH and GPG Keys)
- NEVER share your private key!

### Ex 2. Create Repo in GitHub and Clone Locally
- Create a new repo called py2 in GitHub
- Clone this repo to your local hard drive (new directory py2):
  - Create a directory (`mkdir`)
  - Change into directory (`cd`)
  - `git init`
  - `git clone <SSH URL>` (Not the HTTPS url)
  - Add a test.txt file, add text to file, save the file.
  - Stage the file: `git add --all`
  - Create a commit: `git commit -m "Add file"`
  - Push to GitHub: `git push origin master`

#### Ex 3. Create Code Locally, Create Repo in GitHub, Add Remote
- Create a new local directory
- Open VS Code: `code .`
- Create Python file: `app.py`
- Add code to `app.py`
- Create repo in GitHub
- Initialize local directory to be a git repo: `git init`
- Add remote: `git remote add origin <SSH URL>` (Not the HTTPS url)
- Stage: `git add --all`
- Commit: `git commit -m "first"`
- Push: `git push origin master` (might be `main` for you)

### Ex 4. Meaning of Life (MOL): Part I
- PreReq: Add students as collaborators to GitHub repo
- Create a local directory called `mol`
- Initialize this directory: `git init`
- Clone repo locally: `git clone git@github.com:mburolla/mol.git`
- CD into `mol` directory and launch VS Code: `code .`
- Run the Python `app.py`

### Ex 5. Meaning of Life (MOL): Part II
- Every student is assigned a number
- Each student adds their meaning of life for their assigned function:
```
def student1():
  return "I like dogs"
```
- Each student branches from master and creates a branch with their first name:
Example: `git checkout -b student-<your first name>`
- The student branch is pushed to GitHub
- The student creates a PR that requests their branch be merged into the master (aka main) branch
- The instructor reviews and merges all the PRs
- The students switch to the `master` branch on their local computer, pull the latest code, and run the app

