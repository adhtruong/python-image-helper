import setuptools

from image_helper import __version__

_PACKAGE = "image_helper"

# with open("README.md", "r") as fh:
#     long_description = fh.read()

long_description = ""

with open(f"{_PACKAGE}/_version.py") as f:
    exec(f.read())

setuptools.setup(
    name=_PACKAGE,
    version=__version__,
    author="Andrew Truong",
    description="A package to help render images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adhtruong/cairo_helper",
    packages=setuptools.find_packages(),
    install_requires=["pycairo"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
