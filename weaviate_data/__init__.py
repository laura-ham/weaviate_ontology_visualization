import weaviate
from pathlib import Path


def load():
    dbs = {}
    weaviate_db_path = Path("weaviate_data")
    for db_dir in [db_dir for db_dir in weaviate_db_path.iterdir() if db_dir.is_dir()]:
        if db_dir.name == "__pycache__":
            continue
        db = weaviate.Database.slurp_by_file_name(str(db_dir / "schema.json"))
        dbs[db.name()] = db
    return dbs
