from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


setup(
    name='fload',
    version='0.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fload = fload.cmds.fload:main',
        ],
    },
    install_requires=read_file('requirements.txt'),
)
