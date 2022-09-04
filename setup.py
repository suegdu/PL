from setuptools import setup, find_packages
with open('README.md') as f:
    long_description = f.read()
def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements
setup(name='PL',
      version='1.0',
      description='Personal Python Package for Logging.(PL)',
      author='suegdu',
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='CC0-1.0 license',
      packages=find_packages(),
      author_email='suebusiness@proton.me',
      requires=read_requirements()
     )
