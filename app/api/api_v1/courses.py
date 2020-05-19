#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 22:07
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 课程 API
# @File    : courses.py
# @Software: PyCharm

from fastapi import APIRouter

router = APIRouter()


@router.get('/get_course_byId', name='获取课程信息', description='获取课程信息')
def get_course_byId(userId):
    return {'userId:', userId}


@router.get('/get_course_list', name='获取所有课程')
def get_course_list(userId):
    return {'userId:', userId}
