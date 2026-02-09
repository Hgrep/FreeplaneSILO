from sqlalchemy import Column, String, Text
from app.db.base import Base
import uuid


class Mindmap(Base):
    __tablename__ = "mindmaps"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    xml_content = Column(Text, nullable=False)
