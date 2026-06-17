from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from app.db.base import Base

class Post(Base):
    __tablename__="posts"

    id:Mapped[int]=mapped_column(
        primary_key=True
    )

    title:Mapped[str]=mapped_column(
        String(255)
    )

    content:Mapped[str]

    owner_id:Mapped[int]=mapped_column(
        ForeignKey("users.id")
    )

    owner=relationship(
        "User",
        back_populates="posts"
    )