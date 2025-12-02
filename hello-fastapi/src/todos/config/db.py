from sqlmodel import SQLModel, create_engine
import os

connection_string = os.getenv('DB_URI')
# postgresql://karthiknadar1204:Fvph9DyfVm2L@ep-restless-credit-a1c7489o-pooler.ap-southeast-1.aws.neon.tech/dvfdsbbg?sslmode=require&channel_binding=require
print(connection_string)
engine = create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(engine)