from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


AUTHOR_NAME = 'BISHWAJYOTI CHAUDHARY'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ["streamlit"]

setup(
    name = SRC_REPO,
    author=AUTHOR_NAME,
    author_email="bishwajyotichaudhary46@gmail.com",
    description="A learning pupose to create package for movies reccommendation",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    package =[SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS, 
    
)