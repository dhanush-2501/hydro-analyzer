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
        package_dir={'hydro-analyzer': 'HyAn'}
)
   