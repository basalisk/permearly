import nox


@nox.session(python=["3.8", "3.7"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


lintables = [
    "noxfile.py",
    "permearly/cli.py",
    "permearly/__init__.py",
]


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or lintables
    session.install("flake8")
    session.run("flake8", *args)


@nox.session(python=["3.8", "3.7"])
def black(session):
    args = session.posargs or lintables
    session.install("black")
    session.run("black", *args)
