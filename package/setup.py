from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_package.module:function',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_package_name',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
