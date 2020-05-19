#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:53
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : initial_data.py
# @Software: PyCharm
import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
