## Git

##### Git version control commands:

* Copy repository ```git clone <Repository-URL>```
* Add file to commit process: ```git add <filename>```
* Commit changes: ```git commit -m "This is the description"```
* To combine add and commit messages use ```git commit -am "This is the description"```
* ```git status``` provides details
* ```git log``` provides a history of commits
* ```git push``` sends commits to a remote Repository
* ```git fetch``` downloads the latest branch from the origin (remote git eg: GitHub)
* ```git merge origin/master``` update local to match the remote repository
* ```git pull``` Combines git fetch & merge - collects latest commits and catches up changes from a remote repository
* ```git merge``` combines changes across two branches

##### Git Branching
When working on a new feature to a stable version of the code.  It is wise to branch the project so that the stable version can be maintained while the feature is developed.  This is also useful when working with others on the same project.
* ```git branch``` displays the current branches and which one is active.
* ```git branch <name>``` adds a new branch with the given name
* ```git checkout <name>``` moves the currently active branch to the named branch
* When trying to push a new branch to GitHub where the branch doesn't exist the error *'fatal: The current branch feature has no upstream branch'*.  To create the new branch on GitHub use the command ```git push --set-upstream origin <name>```

##### Git Forking
Taking an independent copy of a repository.  In order to request a merge back into the master branch you issue a "Pull Request".  This is done on GitHub and discussion and feedback can occur between collaborators at this stage

### Misc commands

1. **touch** command can be used to create new files ie:
```touch hello.html```  
2. open atom here:
  ```atom .```
