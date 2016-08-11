import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="axmlparser",
    version="0.0.2",
    author="acgmohu",
    author_email="acgmohu@gmail.com",
    description=("A parser for AndroidManifest.xml"),
    license="Apache",
    keywords="axml manifest",
    url="https://github.com/acgmohu/axmlparser",
    py_modules=["axmlparser"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
)
