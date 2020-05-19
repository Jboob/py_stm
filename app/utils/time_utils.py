#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 16:37
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : time_utils.py
# @Software: PyCharm
import time
from datetime import datetime

from numpy import long


def get13timestamp():
    datetime_object = datetime.now()
    now_timetuple = datetime_object.timetuple()
    now_second = time.mktime(now_timetuple)
    mow_millisecond = long(now_second * 1000 + datetime_object.microsecond / 1000)
    return str(mow_millisecond)
