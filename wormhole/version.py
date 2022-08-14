# Quick python file to define the version

# If gitpython is installed and the repo is directly from git, use the git version
try:
    import git
    repo = git.Repo(search_parent_directories=True)  # type: ignore
    __version__ = f"development-{repo.head.object.hexsha[:7]}"  # type: ignore
except Exception as e:
    __major__ = 1
    __minor__ = 0
    __patch__ = 0
    __version__ = f"{__major__}.{__minor__}.{__patch__}"
