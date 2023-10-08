import sqlalchemy as db

class Database():
    def __init__(self, url:str) -> None:
        self.engine = db.create_engine(url)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.table = db.Table("dht_device", self.metadata, autoload_with=self.engine)

    def insert_dht(self, temperature:int, humidity:int, timestamp:int):
        query = db.insert(self.table).values(
            temperature = temperature,
            humidity = humidity,
            timestamp = timestamp
        )
        self.connection.execute(query)
        self.connection.commit()

    def select_one_dht(self) -> {int, str, str, str}:
        query = db.select(self.table).order_by(db.desc(self.table.columns.id))
        return self.connection.execute(query).fetchone()

    def select_many_dht(self, limit:int=20) -> [{int, str, str, str}]:
        query = db.select(self.table).order_by(db.desc(self.table.columns.id)).limit(limit)
        return self.connection.execute(query).fetchall()

database = Database("sqlite:///database.sqlite")
