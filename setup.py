from setuptools import setup, find_packages

setup(
    name='ximea-examples',
    version='0.1',
    description='ximea camera api examples.',
    author='Piotr Malinski',
    author_email='riklaunim@gmail.com',
    url='https://github.com/riklaunim/ximea-examples',
    setup_requires=['pytest-runner'],
    package_dir={'': 'pyqt'},
    packages=find_packages(where='pyqt'),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
    ],
)
