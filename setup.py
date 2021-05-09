from setuptools import find_packages
from distutils.core import setup

install_requires = [
    'pymysql==0.9.3',
    'requests==2.24.0',
    'aiohttp==3.7.3',
    'DBUtils==2.0',
    'aioredis==1.3.1',
    'aiomysql==0.0.21',
    'redis==3.2.1'
]

excluded = ('CommonPart.gitignore',)

setup(
    name='CommonPart',
    version='0.3.0',
    author='afcentry',
    author_email='afcentry@163.com',
    url='https://github.com/afcentry',
    description='personal python frame',
    packages=find_packages(exclude=excluded),
    install_requires=install_requires,
    license='BSD License',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ],
)
