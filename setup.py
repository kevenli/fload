from setuptools import setup, find_packages


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


setup(
    name='fload',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fload = fload.cmds.fload:main',
        ],
        'fload_modules': [
            '_ = album_download'
        ]
    },
    install_requires=read_file('requirements.txt'),
)
