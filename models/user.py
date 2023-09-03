from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, INTEGER

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(INTEGER(), 
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    