from pathlib import Path

def hello_world():
    print("from haris.py: hello world")

def load_KAGGLE_API_TOKEN(dotenv_path = Path('./.env')) -> None:
    """[ DEPRECATED ] 
    Try to retain KAGGLE_API_TOKEN on a session.
    """
    from dotenv import load_dotenv
    from getpass import getpass

    dotenv_path.touch(exist_ok=True)
    def create_dotenv():
        with open(root, 'w') as f:
            f.write(f"KAGGLE_API_TOKEN={getpass("KAGGLE_API_TOKEN: ")}")

    with open(dotenv_path, 'r') as f:
        KAT_exist = False
        for line in f:
            line = line.strip()
            if 'KAGGLE_API_TOKEN' in line:
                KAT_exist = True
        if not KAT_exist: create_dotenv()

    load_dotenv()

if "__main__" == __name__:
    import subprocess
    from pathlib import Path

    def git_pull(path=Path().cwd()):
        subprocess.run(["git", "-C", str(path), "pull", "-q"], check=True)

    def git_clone(path=Path().cwd()):
        if not (path / ".git").exists():
            if path.exists():
                import shutil
                shutil.rmtree(path)
            path.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                ["git", "clone", "-b", "haris",
                "https://github.com/hariszidan-ui/ProjectARKA", str(path)],
                check=True,
            )
            git_pull()
        else: git_pull()