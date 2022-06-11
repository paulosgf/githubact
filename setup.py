from distutils.core import setup

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
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(
   PACKAGE,
   only_in_packages=False
   ),
    classifiers=[
        "Development Status :: 0 - Dev",
        "Environment :: CI/CD Test",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: None",
    ],
    zip_safe=False,
)
