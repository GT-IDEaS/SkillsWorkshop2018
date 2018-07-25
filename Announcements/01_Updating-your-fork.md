Updating Your Fork of a Repository
==================================

You will undoubtedly notice at some point throughout the workshop that your
fork has become stale, i.e., it is slightly out-of-date with upstream (the
central repository, `GT-IDEaS/SkillsWorkshop2018`).  This will happen from
time-to-time, as we add new assignments, features, lectures, and accept pull
requests containing assignment submissions.  In order to incorporate the
changes to upstream into your `local` repository (on your laptop) and your
`origin` (your fork on GitHub), we'll need to use the command line;
unfortunately, the GitHub desktop client isn't fully-featured enough to do what
we need.  

In a terminal (either your native terminal emulator or the one opened by the
Desktop client under the menu option Repository -> View in Terminal), follow
along with the steps provided
[here](https://help.github.com/articles/syncing-a-fork/).  Once your `local`
repository has been updated, you can push these updates to your fork with
```
$ git push --force origin master
```
**Note 01**: The `$` in the above line and in the code snippets in the "Syncing a
fork" article indicate the terminal prompt, and should not be typed by you.

**Note 02**: If, after step 3, you encounter the error:
```
fatal: 'upstream' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
you will need to follow the steps
[here](https://help.github.com/articles/adding-a-remote/) to add the [central
workshop repository](https://github.com/GT-IDEaS/SkillsWorkshop2018) as a
remote to local.  

~ DS

