import sqlalchemy as db

from sqlalchemy import Table, Column, Integer

if __name__ == "__main__":
    engine = db.create_engine("sqlite:///database.sqlite")
    metadata = db.MetaData()

    table = Table("dht_device", metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("temperature", Integer, nullable=False),
        Column("humidity", Integer, nullable=False),
        Column("timestamp", Integer, nullable=False)
    )

    metadata.create_all(engine)
