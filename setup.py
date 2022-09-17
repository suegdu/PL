from setuptools import setup, find_packages



def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements
setup(
    name="PL",
    author="suegdu",
    author_email="suebusiness@proton.me",
    url="https://github.com/suegdu/PL",
    description="Personal Python Package for Logging.",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=read_requirements(),
    version="1.2.0",
    #install_requires=[
    #    "setuptools>=45.0",
    #],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
)
