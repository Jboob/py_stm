#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 11:27
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : init_db.py
# @Software: PyCharm
from sqlalchemy.orm import Session

from app.db.base_class import Base


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(db.bind)

    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #     )
    #     user = crud.user.create(db, obj_in=user_in)  # noqa: F841
