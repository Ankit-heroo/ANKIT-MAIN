from setuptools import setup
from Cython.Build import cythonize

setup(
    name="main",
    ext_modules=cythonize("main.pyx", compiler_directives={'language_level': '3'}),
)