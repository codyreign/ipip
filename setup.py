from setuptools import setup, find_packages
import os

# Read README safely
def read_readme():
    try:
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Intelligent pip package installer using AI to resolve package names"

setup(
    name="ipip",
    version="0.1.0",
    packages=find_packages(),
    author="Cody Serino (Zero)",
    author_email="iamtheoriginalzero@gmail.com",
    description="Intelligent pip package installer using AI to resolve package names",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ipip",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "requests>=2.25.0",
        "rich>=10.0.0",
        "packaging>=21.0",
    ],
    entry_points={
        "console_scripts": [
            "ipip=ipip.cli:main",
        ],
    },
)