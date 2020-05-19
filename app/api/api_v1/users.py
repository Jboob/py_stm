#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 17:50
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : users.py
# @Software: PyCharm

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps

router = APIRouter()


@router.get('/get_user_info', name='获取用户信息',
            description='获取用户信息', response_model=schemas.User)
def get_user_info(userName, db: Session = Depends(deps.get_db)):
    user = crud.user.get_by_userName(db, userName)
    return user


@router.post("/create_user", response_model=schemas.User, name='创建用户')
def create_user(*,
                db: Session = Depends(deps.get_db),
                user_in: schemas.UserCreate):
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.post("/update_user", response_model=schemas.User, name='修改用户')
def update_user(*, db: Session = Depends(deps.get_db),
                user_id: int,
                user_in: schemas.UserUpdate):
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user


@router.post("/delete_user", response_model=str, name='删除用户')
def delete_user(user_id: int, db: Session = Depends(deps.get_db)):
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="用户不存在",
        )
    crud.user.remove(db, db_obj=user)
    user = crud.user.get(db, id=user_id)
    msg = '删除失败'
    if not user:
        msg = '删除成功'
    return msg
