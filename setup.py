from setuptools import setup, find_packages

PACKAGE = "githubact"
NAME = "githubact"
DESCRIPTION = ""
AUTHOR = "Paulo Ferraz"
AUTHOR_EMAIL = "paulosgf@proton.me"
URL = "https://github.com/paulosgf/githubact"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Framework :: Django",
],
zip_safe=False,    
)
