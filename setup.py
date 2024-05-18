#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ZwaveNetLyzer",
    version="0.1.0",
    author="Moein Shafi",
    author_email="moeinsh@yorku.ca",
    description="A network analyzer tool for IoT Zwave networks traffic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahlashkari/Z-WaveNetLyzer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": ["zwave-netlyzer = ZwaveNetLyzer.__main__:main"]
    },
)
