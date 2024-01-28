from setuptools import setup, find_packages

setup(
    name='my-python-project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'toga',
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'my-python-project=src.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python project to display top 10 CPU consuming processes using Toga',
)