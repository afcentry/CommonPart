# _*_ coding:utf-8 _*_
"""
----------------------------------
filename:  dbnode
author:    afcentry
date:      2021/5/6
description:CommonPart数据库链接创建以及可用性检验节点
----------------------------------
"""
from dbutils.pooled_db import PooledDB
import pymysql, aiomysql
import redis, aioredis

from CommonPart.combuiltin.combuiltin import ComBuiltin


class MysqlUtils:
    """
    数据库链接池操作系列
    """

    def __init__(self, max_con=1, **kwargs):
        self.pool = None
        self.create_pool(max_con=max_con, **kwargs)

    def create_pool(self, max_con=1, **kwargs):
        """
        max_con:链接池创建sql链接数量
        host:主机名称
        user:用户名
        passwd:密码
        db:数据库
        port:端口
        charset:编码格式
        """
        self.pool = PooledDB(pymysql, max_con, **kwargs)

    @property
    def conn(self):
        """
        从链接池获取数据库链接
        """
        try:
            con = self.pool.connection()
        except Exception as e:
            print("[{}] 数据库链接获取错误.[{}]".format(ComBuiltin.get_current_time(), e))
            con = None
        return con


class RedisUtils:
    """
    redis操作类
    """

    def __init__(self, **kwargs):
        self.pool = None
        self.create_pool(**kwargs)

    def create_pool(self, **kwargs):
        """
        host:主机
        port:端口
        db:数据库
        password:密码
        """
        self.pool = redis.ConnectionPool(**kwargs)

    @property
    def conn(self):
        """
        从redis链接池获取连接
        """
        try:
            con = redis.Redis(connection_pool=self.pool)
        except Exception as e:
            print("[{}] redis链接获取错误.[{}]".format(ComBuiltin.get_current_time(), e))
            con = None
        return con


class AsyncRedisUtils:
    """
    redis异步操作类
    """

    def __init__(self):
        self.redis_pool = None

    async def create_pool(self, host, port, db, password, loop, minsize=1, maxsize=5):
        """
        host:主机
        port:端口
        db:数据库
        password:密码
        loop:事件循环器
        """
        self.redis_pool = await aioredis.create_pool(
            (host, port, db, password),
            minsize=minsize,
            maxsize=maxsize,
            loop=loop
        )
        """
        usage:
        async with request.app.redis_pool.get() as redis:
            await redis.execute('set', 'my-key', 'value')
            val = await redis.execute('get', 'my-key')
        """
        return self.redis_pool


class AsyncMysqlUtils:
    """
    mysql异步操作类
    """

    def __init__(self):
        self.pool = None

    async def create_pool(self, **kwargs):
        # host='127.0.0.1', port=3306,user='root', password='',db='mysql', loop=loop
        self.pool = await aiomysql.create_pool(**kwargs)
        """
        usage:
        async with pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 42;")
                value = await cur.fetchone()
                print(value)
        """
        return self.pool
