# 分开创造对象的过程 和 使用对象的过程
import sqlalchemy as sa
import json 

class DatabaseConnection: 
    def __init__(self, host:str, port:int, user:str, password:str) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        
    def connect(self) -> sa.Engine: 
        engine = sa.create_engine(f'mysql://{self.user}:{self.password}@{self.host}:{self.port}')
        print(f"Connected to {self.host} on port {self.port}")
        return engine
        
def connection_factory(db_type) -> DatabaseConnection: 
    with open("Factory-Pattern/configs/db_configs.json") as f: 
        df_configs = json.load(f)
        
    return DatabaseConnection(**df_configs[db_type])

if __name__ == "__main__": 
    db = connection_factory("istock_db")
    engine = db.connect() # 假的链接数据，但是注释对应位置后可以看到连接成功的信息