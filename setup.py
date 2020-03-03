"""Setup File for the deepdepict package."""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Smaranjit Ghose",
    author_email="smaranjitghose@protonmail.com",
    name='deepdepict',
    license="MIT",
    description='An open source project to create a Python package that contains easy plugins for common data structures and algortihms using Python',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/smaranjitghose/pyalgocheat',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['numpy','open_cv'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
