from setuptools import setup, find_packages

setup(
    name="ks_openai",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic"
    ],
    description="A simple Python wrapper for OpenAI-like API",
    author="Raj Aryan",
    author_email="raj@klopudstac.com",
    url="https://github.com/yourusername/ks_openai",
)
