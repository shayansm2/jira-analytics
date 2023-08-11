import pandas as pd

from DbConnection import DbConnection


class DbReader(object):
    def __init__(self, db_connection: DbConnection):
        self.dbConnection = db_connection
        self.chunkSize = 500

    def set_chunk_size(self, chunk_size: int):
        self.chunkSize = chunk_size
        return self

    def get_df(self, query: str) -> pd.DataFrame:
        query_result = []

        for chunks in pd.read_sql_query(sql=query, con=self.dbConnection, chunksize=self.chunkSize):
            query_result.append(chunks)

        return pd.concat(query_result, ignore_index=True)
