"""
The setup for installation of the BikesData package.
Helpful resource:
https://docs.python.org/3.6/distutils/setupscript.html
"""
from setuptools import setup

setup(
    name="Dynamodb",
    version=0.1,
    description="Easy querries from Amazon dynamoDb",
    author="Liga Oz",
    keywords="Dublin bikes ddb data getter",
    packages=["dbb"],
)
