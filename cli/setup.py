from setuptools import setup, find_packages

setup(
    name='my_cli_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'mycli=my_cli_project.cli:cli',
        ],
    },
)
