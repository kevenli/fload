from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


setup(
    name='fload',
    version='0.0.5',
    description='fload is a data processing toolkit.', 
    packages=find_packages(exclude=('tests', 'tests.*')),
    entry_points={
        'console_scripts': [
            'fload = fload.cmds.fload:main',
        ],
    },
    author='Keven Li',
    author_email='pbleester@gmail.com',
    url='http://github.com/kevenli/fload',
    long_description=long_description, 
    install_requires=read_file('requirements.txt'),
    long_description_content_type='text/markdown', 
)
