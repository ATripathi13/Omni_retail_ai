from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define 4 separate Bases for strict isolation
ShopBase = declarative_base()
ShipBase = declarative_base()
PayBase = declarative_base()
CareBase = declarative_base()

DB_NAMES = {
    'shop_core': ShopBase,
    'ship_stream': ShipBase,
    'pay_guard': PayBase,
    'care_desk': CareBase
}

def get_engine(db_name):
    db_path = f"{db_name}.db"
    return create_engine(f"sqlite:///{db_path}", echo=False)

def get_session(db_name):
    engine = get_engine(db_name)
    Session = sessionmaker(bind=engine)
    return Session()

def init_dbs():
    for name, base in DB_NAMES.items():
        engine = get_engine(name)
        base.metadata.create_all(engine)
        print(f"Initialized {name} database.")
