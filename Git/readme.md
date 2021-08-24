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

### Ex 2. Create Repo & Upload File
- Create a new repo called py2 in GitHub
- Clone this repo to your local hard drive (new directory py2):
	
  - Create a directory (`mkdir`),
  - Change into directory (`cd`)
  - `git init`
  - `git clone` <SSH URL> (Not the HTTPS url)
  - Add a test.txt file, add text to file, save the file.
  - Stage the file: `git add --all`
  - Create a commit: `git commit -m "Add file"`
  - Push to GitHub: `git push origin master`

### Ex 3. 

