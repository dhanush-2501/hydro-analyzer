import os
from setuptools import setup, find_packages

def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            quote_char = '"' if '"' in line else "'"
            return line.split(quote_char)[1]
    raise RuntimeError("Unable to find version string.")

setup(
        name='HyAn',
        version=get_version("HyAn/__init__.py"),
        packages=find_packages(),
        install_requires=[
                          "matplotlib==3.7.1",
                          "numpy==1.24.2",
                          "PySide6==6.4.2",
                          "scipy==1.10.1",
                          "setuptools==65.6.3", 
                        ],
        package_dir={'hydro-analyzer': 'HyAn'}
)
   