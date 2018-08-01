Branching and the GitHub Flow
=============================

The fork-and-pull model of the GitHub workflow that we have been utilizing thus
far in the course is a powerful tool for social coding and community
involvement.  One very useful feature of this model, however, is both a
blessing and a curse: once a pull request from `origin/master` to has been
opened `upstream/master`, any new commits to your fork will automatically be
incorporated into your pull request.  This is great for when you want to add a
file to that PR or to modify some of its contents, but what if you want to have
a new PR that is wholly separate from the first (a.k.a., how do I submit my
Week02 assignment separately from Week01)?  

To do this, we need to talk about _branches_ and the GitHub flow.  These
concepts are central to how nearly all major software projects that use Git
operate, so they will also serve us well to employ.  A _branch_ can be thought
of as a particular snapshot of your repository's history, which allows you to
make new changes on top of that snapshot that are entirely separate from all
other changes made to the repository.  This allows us to do exactly what we
want, namely to develop separate features independently of one another.  The
_GitHub Flow_ is a model for combining branches and pull requests to create an
effective, collaborative development environment within a community.  For a
brief discussion on how the GitHub flow works, check out [this
page](https://guides.github.com/introduction/flow/), which is one of the
official [GitHub Guides](https://guides.github.com/).  

Once you've read through the guide on the GitHub flow, we're ready to discuss
how to use branches within our workshop.  Let's say, for example, my pull
request for Assignment 01 has been submitted, and one of the TAs has requested
that I make changes to it before they merge my PR.  In the meantime, however, I
want to be able to work on Assignment 02 without my new commits being placed
into my open pull request.  I can do this by working on a new branch for
Assignment 02.  

### Steps for Branch-and-PR Model

1. Make sure your `master` branch is up-to-date; you might need to follow the
steps discussed
[here](https://github.com/GT-IDEaS/SkillsWorkshop2018/blob/master/Announcements/01_Updating-your-fork.md)
2. Create and switch to a new branch for Assignment 02, using `git checkout -b`:
    ```
    $ git checkout -b assignment02
    ```
3. Work on your new branch, making and committing changes with `git add` and `git commit`
4. Push your changes on the new branch to your fork with `git push`:
    ```
    $ git push origin assignment02
    ```
    Here, `origin` refers to your fork, and `assignment02` is the branch on your fork
    to which you wish to push (exactly analogous to `git push origin master`, except
    we've switched out `master` for our branch, `assignment02`).
5. Open a pull request from your fork's `assignment02` branch,
`origin/assignment02`, to `upstream/master`.  GitHub may detect the new branch
and changes automatically and prompt you to open a PR to `upstream/master`, but
you can do so manually by following [these
steps](https://help.github.com/articles/creating-a-pull-request/) to change the
base of your pull request.

Now that we know how to use branching and the GitHub flow, you can keep your
work on different assignments separate!

~ DS

