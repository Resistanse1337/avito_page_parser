import sqlite3


class AvitoDb:
    def __init__(self):
        self.connection = sqlite3.connect("avito.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS avito_ads(
                id INTEGER NOT NULL UNIQUE,
                name TEXT,
                price REAL,
                eur_price REAL,
                images TEXT,
                chars_names TEXT,
                chars_values TEXT,
                description TEXT,
                place TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
        """)
        self.connection.commit()

    def insert_row(self, row):
        self.cursor.execute(f"INSERT INTO avito_ads VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", [None] + row)
        self.connection.commit()

    def get_all_data(self):
        self.cursor.execute("SELECT * FROM avito_ads")
        return self.cursor.fetchall()

    def get_headers(self):
        self.cursor.execute("SELECT * FROM avito_ads")
        self.connection.row_factory = sqlite3.Row
        cursor = self.connection.execute('select * from avito_ads')
        keys = cursor.fetchone().keys()

        return keys

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    avito = AvitoDb()
    avito.insert_row(["test", 12.0, 1.0, "dsfsdfs|addasda", "123|43", "sdhfdusofosdfs", "dsfdsfs|234242|asdasda", "1erwrew"])
    all_data = avito.get_all_data()
    print(all_data)
    keys = avito.get_headers()
    print(keys)
    avito.close_connection()





