from setuptools import setup


def readme():
    with open('README.rst') as file:
        return file.read()

setup(
    name='confluence_python_cli',
    version='0.1.0',
    description='REST API for confluence',
    long_description=readme(),
    url='http://github.com/funkwerk/confluence-python-cli',
    author='Remy from github.com/RaymiiOrg, Stefan Rohe',
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Environment :: Console',
        'Operating System :: OS Independent',
    ],
    keywords='confluence rest api',
    include_package_data=True,
    scripts=['confluence.py'],
)
