from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

version = SourceFileLoader('version', 'stpmex/version.py').load_module()

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='stpmex',
    version=version.__version__,
    author='Cuenca',
    author_email='dev@cuenca.com',
    description='Client library for stpmex.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cuenca-mx/stpmex-python',
    packages=find_packages(),
    include_package_data=True,
    package_data=dict(stpmex=['py.typed']),
    python_requires='>=3.6',
    install_requires=[
        'pyopenssl>=19.1,<19.2',
        'clabe>=1.2,<1.3',
        'pydantic>=1.5,<1.6',
        'dataclasses>=0.6;python_version<"3.7"',
        'requests>=2.24,<2.25',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
