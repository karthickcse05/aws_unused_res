import setuptools
from package import Package

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awsunusedresources",  # Replace with your own username
    version="0.1.6",
    author="Karthickcse05",
    author_email="Karthickcse05@gmail.com",
    description="A package for identifying unused resources in aws",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karthickcse05/aws_unused_res",
    packages=setuptools.find_packages(),
    include_package_data=True,
    cmdclass={
        "package": Package
    },
    install_requires=[
        "pandas==1.1.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.0',
)
