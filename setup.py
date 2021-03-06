import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tglog",
    version="4.0",
    author="Stanislas du Rivau",
    author_email="sdurivau25@gmail.com",
    description="Log errors in a log.txt file and receive them by telegram.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdurivau25/tglog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)