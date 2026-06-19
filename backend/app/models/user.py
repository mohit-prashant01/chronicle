from datetime import datetime

from sqlalchemy import String 
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship
)

from app.db.base import Base


class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(
        primary_key=True,
        index=True
    )

    username:Mapped[str]=mapped_column(
        String(50),
        nullable=False
    )

    email:Mapped[str]=mapped_column(
        String(255),
        unique=True,
        nullable=True
    )


    password_hash:Mapped[str]=mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )


    posts=relationship(
        "Post",
        back_populates="owner"
    )