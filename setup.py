# setup.py

from setuptools import setup, find_packages

setup(
    name="library_management_system",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
    ],
    entry_points={
        "console_scripts": [
            "library-management=main:main",
        ],
    },
)
