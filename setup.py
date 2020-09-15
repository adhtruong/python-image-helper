import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

long_description = ""

setuptools.setup(
    name="cairo_helper",  # Replace with your own username
    version="0.0.1",
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
