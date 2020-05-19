#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 17:37
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : login.py
# @Software: PyCharm
from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.models.user import User

router = APIRouter()


@router.post('/user_login')
def login(userName, userPass, db: Session = Depends(deps.get_db)):
    user = crud.user.authenticate(db, userName=userName, password=userPass)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.userName, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/login/test-token", response_model=schemas.User)
def test_token(current_user: User = Depends(deps.get_current_user)) -> Any:
    return current_user
