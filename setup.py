#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

test_requirements = []

setup(
    author="Bit68",
    author_email="yusufadell.dev@bit68.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="automate sheets ",
    entry_points={
        "console_scripts": [
            "xlsx_automate=xlsx_automate.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="xlsx_automate",
    name="xlsx_automate",
    packages=find_packages(include=["xlsx_automate", "xlsx_automate.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/yusufadell/xlsx_automate",
    version="0.1.0",
    zip_safe=False,
)
