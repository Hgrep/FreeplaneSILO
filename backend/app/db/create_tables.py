from app.db.base import Base
from app.db.session import engine

# Import models so they register with Base
from app.models.mindmap import Mindmap

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created")

if __name__ == "__main__":
    create_tables()
