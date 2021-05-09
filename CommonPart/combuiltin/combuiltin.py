# coding:utf-8
"""
系统通用内建模块
提供通用功能块
"""

import time
import datetime
import requests
import random
import aiohttp
import asyncio
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from CommonPart.commonvar.commonvar import CommonVar, ProxyUnit

# 禁用安全请求警告

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ComBuiltin:

    @staticmethod
    def get_current_time():
        """
        获取系统当前日期时间
        :return: 2020-02-02 08:00:00
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    @staticmethod
    def get_current_date():
        """
        获取系统当前日期
        :return: 2020-02-02
        """
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def get_timestamp13():
        """获取13位时间戳"""
        return int(round(time.time() * 1000))

    @staticmethod
    def get(url, **kwargs):
        """
        模拟发送GET请求
        url headers verify proxy timeout
        ifproxy: 是否使用代理访问  默认 False
        trytimes: 是否做请求失败尝试 默认不重试
        :return:
        """
        trytimes = kwargs.pop(CommonVar.trytimes) if CommonVar.trytimes in kwargs.keys() else 1
        if_proxy = kwargs.pop(CommonVar.ifproxy) if CommonVar.ifproxy in kwargs.keys() else False
        proxies = kwargs.get(CommonVar.proxies) if CommonVar.proxies in kwargs.keys() else None
        if CommonVar.global_proxy and if_proxy:  # 使用代理访问
            if not proxies:
                proxy = ComBuiltin.get(ProxyUnit.URL, verify=False, trytimes=3, timeout=3)
                if proxy:
                    proxy_info = proxy.json()
                    if not proxy_info[CommonVar.status]:
                        kwargs[CommonVar.proxies] = proxy_info[CommonVar.proxy]

        current_time, response = 1, None
        while current_time <= trytimes:
            try:
                response = requests.get(url, **kwargs)
                if response:
                    break
                else:
                    time.sleep(random.random())
                    continue
            except:
                current_time += 1
                continue
            finally:
                time.sleep(random.randint(1, 3) / 10)
        return response

    @staticmethod
    def post(url, **kwargs):
        """
        模拟发送POST请求
        url headers verify proxy timeout
        ifproxy: 是否使用代理访问  默认 False
        trytimes: 是否做请求失败尝试 默认不重试
        :return:
        """
        trytimes = kwargs.pop(CommonVar.trytimes) if CommonVar.trytimes in kwargs.keys() else 1
        if_proxy = kwargs.pop(CommonVar.ifproxy) if CommonVar.ifproxy in kwargs.keys() else False
        proxies = kwargs.get(CommonVar.proxies) if CommonVar.proxies in kwargs.keys() else None
        if CommonVar.global_proxy and if_proxy:  # 使用代理访问
            if not proxies:
                proxy = ComBuiltin.get(ProxyUnit.URL, verify=False, trytimes=3, timeout=1)
                if proxy:
                    proxy_info = proxy.json()
                    if not proxy_info[CommonVar.status]:
                        kwargs[CommonVar.proxies] = proxy_info[CommonVar.proxy]

        current_time, response = 1, None
        while current_time <= trytimes:
            try:
                response = requests.post(url, **kwargs)
                if response:
                    break
                else:
                    time.sleep(random.random())
                    continue
            except:
                current_time += 1
                continue
            finally:
                time.sleep(random.randint(1, 3) / 10)
        return response

    @staticmethod
    async def async_get_proxy():
        """
        异步请求本地代理池
        """
        while True:
            async with aiohttp.ClientSession() as session:
                async with session.get(ProxyUnit.URL) as resp:
                    if resp.status == 200:
                        proxy_info = await resp.json()
                        break
                    await asyncio.sleep(1)
        return proxy_info

    @staticmethod
    async def get_proxy():
        """
        异步请求本地代理池
        """
        while True:
            async with aiohttp.ClientSession() as session:
                async with session.get(ProxyUnit.URL) as resp:
                    if resp.status == 200:
                        proxy_info = await resp.json()
                        break
                    await asyncio.sleep(1)
        return proxy_info

    @staticmethod
    async def async_get(url, **kwargs):
        """
        模拟发送GET请求 异步实现
        url headers verify proxy timeout
        ifproxy: 是否使用代理访问  默认 False
        trytimes: 是否做请求失败尝试 默认不重试
        :return:
        """

        trytimes = kwargs.pop(CommonVar.trytimes) if CommonVar.trytimes in kwargs.keys() else 1
        if_proxy = kwargs.pop(CommonVar.ifproxy) if CommonVar.ifproxy in kwargs.keys() else False
        if CommonVar.global_proxy:
            if if_proxy:  # 使用代理访问
                proxy_info = await ComBuiltin.async_get(ProxyUnit.URL, verify=False, trytimes=3, timeout=1)
                kwargs[CommonVar.proxy] = proxy_info[CommonVar.proxy]
        current_time, response = 1, None
        while current_time <= trytimes:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, **kwargs) as resp:
                        if resp and resp.status == 200:
                            response = await resp.read()
                        break
            except Exception as e:
                current_time += 1
                continue
            finally:
                time.sleep(random.randint(1, 3) / 10)
        return response
