import os
# user = os.environ["POSTGRES_USER"]
# password = os.environ["POSTGRES_PASSWORD"]
# host = os.environ["POSTGRES_HOST"]
# database = os.environ["POSTGRES_DB"]
# print(f"PORT : {os.environ['POSTGRES_PORT']}")

# port = int(os.environ['POSTGRES_PORT'])
DATABASE_CONNECTION_URI = f"postgresql+psycopg2://test:password@database:5432/todo_db"
