import codecs
import io
import os
import re
import sys
import webbrowser
import platform

try:
    from setuptools import setup
except:
    from distutils.core import setup


NAME = "quantaxis_run"
"""
名字，一般放你包的名字即可
"""
PACKAGES = ["quantaxis_run"]
"""
包含的包，可以多个，这是一个列表
"""

DESCRIPTION = "QUANTAXIS:Quantitative Financial Strategy Framework"
KEYWORDS = ["quantaxis", "quant", "finance", "Backtest", 'Framework']
AUTHOR_EMAIL = "yutiansut@qq.com"
AUTHOR = 'yutiansut'
URL = "https://github.com/yutiansut/quantaxis_run"


LICENSE = "MIT"

setup(
    name=NAME,
    version='1.0',
    description=DESCRIPTION,
    long_description='automatic run quantaxis program',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=['celery==3.1.25', 'quantaxis>=1.1.10.dev2'],
    # entry_points={
    #     'console_scripts': [
    #         'quantaxis=QUANTAXIS.QACmd:QA_cmd',
    #         'quantaxisd=QUANTAXIS.QAWeb.QA_Web:main',
    #         'quantaxisq=QUANTAXIS.QAFetch.QATdx_adv:bat',
    #         'qarun=QUANTAXIS.QACmd.runner:run'
    #     ]
    # },
    # install_requires=requirements,
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)
