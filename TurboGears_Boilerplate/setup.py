from setuptools import setup, find_packages

setup(
    name='project_name',
    version='0.1',
    install_requires=['TurboGears2', 'SQLAlchemy'],
    packages=find_packages(),
    entry_points={
        'paste.app_factory': ['main = project_name:make_app'],
    },
)
