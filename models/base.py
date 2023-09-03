from typing import Any
from sqlalchemy.orm import DeclarativeBase
from models import metadata

class MixinAsDict:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Base(DeclarativeBase, MixinAsDict):
    metadata = metadata