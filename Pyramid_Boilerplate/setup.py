from setuptools import setup

requires = [
    'pyramid',
    'waitress',
]

setup(
    name='project_name',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = project_name:main',
        ],
    },
)
