from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import text
from app.models import *

from app.core.config import settings

engine = create_engine(settings.DB_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():

    SQLModel.metadata.create_all(engine)
    print("✅  All tables created")


def drop_db_and_tables():
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))
        conn.commit()


# migration initial db
if __name__ == "__main__":
    create_db_and_tables()
