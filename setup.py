from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="opus-greennet",
    version="0.0.1",
    author="Schmaik",
    author_email="schmaikv3@gmail.com",
    description="A package to interact with the OPUS greenNet API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DerSchmaik/opus_grennnet_wrapper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)