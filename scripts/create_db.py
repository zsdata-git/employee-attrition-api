from app.db.base import Base
from app.db.models import EmployeeRecord, PredictionRecord
from app.db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    create_tables()