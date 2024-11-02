from setuptools import setup, find_packages

setup(
    name='My_Packages',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/MoXaDe23/My_Packages',
    author='NELSON MUGUME',
    author_email='nelsonmuhoozi@gmail.com'
    )