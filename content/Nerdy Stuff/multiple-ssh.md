Title: How I Manage Multiple SSH Keys for GitHub Accounts
Date: 2016-12-09
Tags: ssh; github

I'm working on a new website ([big6e](https://big6e.github.io)) for which I'm again using the free hosting services of 
GitHub. Thus, locally I now have 2 directories that are clones of repos from 2 different GitHub accounts. Since I use 
ssh to push changes, I had to figure out how to manage this.

I used [this](https://gist.github.com/jexchan/2351996) to configure multiple ssh keys. There's a step, a rather 
important one, kind of buried in the comments, so I'll rewrite the commands here. I'm going to start completely over 
since the names of my key pairs aren't consistent. Might as well make it clean, right?! 

1. Create new ssh key pairs
```
$ ssh-keygen -f ~/.ssh/git-edwardmurphy -t rsa -C "for git user edwardmurphy"
$ ssh-keygen -f ~/.ssh/git-big6e -t rsa -C "for git user big6e"
```

2. Add new keys
```
$ ssh-add ~/.ssh/git-edwardmurphy
$ ssh-add ~/.ssh/git-big6e
```

3. For each new key pair, copy the public key to the settings in GitHub account
```
$ cat ~/.ssh/git-edwardmurphy.pub
$ cat ~/.ssh/git-big6e.pub

4. Modify/create a configuration file in the ssh directory
```
$ nano ~/.ssh/config

Host github.com-edwardmurphy
HostName github.com
User git
IdentityFile ~/.ssh/git-edwardmurphy

Host github.com-big6e
HostName github.com
User git
IdentityFile ~/.ssh/git-big6e
```  

5. For each local repo, remove the remote repo and add a new remote repo as in this example
```
$ cd ~/ghpages/output
$ git remote remove origin
$ git remote add origin git@github.com-edwardmurphy:edwardmurphy/edwardmurphy.github.io
```


