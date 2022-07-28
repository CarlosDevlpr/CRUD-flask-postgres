from datetime import datetime
from typing import Any

from pydantic import BaseModel as BaseModelPY
from sqlalchemy import func
from sqlalchemy.sql import expression
from sqlalchemy.sql.schema import Column
from sqlalchemy.types import Boolean, DateTime, Integer
from src import db

class errorSchema(BaseModelPY):
    error: Any
    code: int

#Uma base com colunas essencias para diveras tabelas, inclusive as de usuário
class BaseEntity(db.Model):
    __abstract__: True

    id: int = Column(
        Integer,
        primary_key = True,
        index = True)

    created_on: datetime = Column(
        DateTime(timezone=True), 
        default=func.now(),
        server_default=func.now()
    )

    updated_on: datetime = Column(
        DateTime(timezone=True), 
        default=func.now(),
        server_default=func.now(),
        server_onupdate=func.now(),
        onupdate=func.now()
    )

    deleted: bool = Column(
        Boolean,
        server_default=expression.false(),
        default=False,
        nullable=False
    )

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, deleted={self.deleted}, created_on={self.created_on})"
        
