#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import glob
import sys
import os

setup(
    name="semterm",
    packages=["semterm"],
    version="0.0.1",
    license="UNLICENSED",
    description="Semantic terminal",
    author="mirmik",
    author_email="netricks@protonmail.com",
    url="https://github.com/mirmik/semantic-terminal",
    classifiers=[],
    package_data={
        "semterm": [
            "dialogs/*",
        ]
    },
    #package_data={"semterm": ["img/*"]},
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["semterm=semterm.__main__:main"]},
)
