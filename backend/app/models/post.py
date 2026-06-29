from datetime import datetime
from sqlalchemy import (
    ForeignKey,
    String,
    Text,
    DateTime,
    Integer,
    func   
)

from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship
)

from app.db.base import Base


class Post(Base):
    __tablename__="posts"

    id:Mapped[int]= mapped_column(
        primary_key=True
    )

    title: Mapped[str]=mapped_column(
        String(255),
        nullable=False
    )

    content:Mapped[str]=mapped_column(
        Text,
        nullable=False
    )

    owner_id:Mapped[int]=mapped_column(
        ForeignKey("users.id")
    )

    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    reading_time:Mapped[int]=mapped_column(
        Integer,
        nullable=False,
        default=1
    )

    owner=relationship("User",back_populates='posts')