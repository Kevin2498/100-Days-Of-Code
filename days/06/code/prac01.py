# Get data from DB and store it in S3

class DragonFlyIntegration():
    def __init__(self, source_name, secret_creds, sql_query, s3_path):
        self._source_name = source_name
        self._secret_creds = secret_creds
        self._sql_query = sql_query
        self._s3_path = s3_path
    
    def get_db_creds(self):
        abc = self._secret_creds
        return abc

    def get_data_from_db(self, conn):
        print(f"Using connection {conn} connecting with db and by using {self._sql_query} getting data")
        pass

    def convert_data_to_parquet(self, data):
        print(f"Converting {data} to parquet")
        pass

    def upload_file_to_s3(self):
        print(f"Uploading parquet data at {self._s3_path}")
