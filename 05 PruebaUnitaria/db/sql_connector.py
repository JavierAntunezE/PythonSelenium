import pyodbc

class SqlConnector:
    def __init__(self, server, database, user, password):
        self.conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};DATABASE={database};UID={user};PWD={password}"
        )
        self.connection = None

    def connect(self):
        self.connection = pyodbc.connect(self.conn_str)
        return self.connection

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()
