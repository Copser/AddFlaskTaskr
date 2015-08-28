from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


def test():
    """TODO: Docstring for test.
    :returns: TODO
    Building fabfile for automated deployment
    to github and heroku, updated test() to
    handle test fail.

    """
    with settings(warn_only=True):
        result = local("nosetests -v", capture=True)
    if result.failed and not confirm("Tests failed. Continue?"):
        abort("Aborted at user request.")


def commit():
    """TODO: Docstring for commit.
    :returns: TODO
    Code for add and commit code to GitHub

    """
    message = raw_input("Enter a git commit message: ")
    local("git add . && git commit -am '{}'".format(message))


def push():
    """TODO: Docstring for push.
    :returns: TODO
    Push commit code to GitHub

    """
    local("git push origin master")


def prepare():
    """TODO: Docstring for prepare.
    :returns: TODO

    """
    test()
    commit()
    push()
