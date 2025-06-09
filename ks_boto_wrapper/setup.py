from setuptools import setup, find_packages

setup(
    name="ks_boto_wrapper",
    version="0.1.0",
    description="A wrapper library for boto3 utilities",
    author="Aswin Pratapsingh",
    author_email="pratapsinghaswin@gmail.com",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "pydantic",
        "requests"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)