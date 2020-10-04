import setuptools

_PACKAGE = "image_helper"

with open("README.md", "r") as fh:
    long_description = fh.read()


with open(f"./{_PACKAGE}/_version.py") as f:
    exec(f.read())


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name=_PACKAGE,
    version=__version__,  # noqa: F821
    author="Andrew Truong",
    description="A package to help render images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adhtruong/python-image-helper",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
