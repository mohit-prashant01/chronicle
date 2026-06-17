from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from app.db.base import Base

class User(Base):
    __tablename__ = "users"

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
        nullable=False
    )

    posts=relationship(
        "Post",
        back_populates="owner"
    )