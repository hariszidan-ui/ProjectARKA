from pathlib import Path

def load_KAGGLE_API_TOKEN(dotenv_path = Path('./.env')) -> None:
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
    pass