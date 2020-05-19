#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:37
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : crud_user.py
# @Software: PyCharm
import time

from app.crud.base import CRUDBase
from app.models.user import User

from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.time_utils import get13timestamp


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    # 根据用户名查询
    def get_by_userName(self, db: Session, userName: str) -> Optional[User]:
        return db.query(User).filter(User.userName == userName).first()

    # 创建一个用户
    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            userName=obj_in.userName,
            userPass=get_password_hash(obj_in.userPass),
            email=obj_in.email,
            mobile=obj_in.mobile,
            regTime=get13timestamp(),
            loginTime=get13timestamp(),
            is_active=obj_in.is_active,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # 更新用户信息
    def update(
            self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["userPass"]:
            hashed_password = get_password_hash(update_data["userPass"])
            del update_data["userPass"]
            update_data["userPass"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    # 删除用户
    def remove(self, db: Session, db_obj: User
               ) -> User:
        db.delete(db_obj)
        db.commit()
        return

    def authenticate(self, db: Session, *, userName: str, password: str) -> Optional[User]:
        user = self.get_by_userName(db, userName=userName)
        if not user:
            return None
        if not verify_password(password, user.userPass):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active


user = CRUDUser(User)
