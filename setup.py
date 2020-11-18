#!/usr/bin/env python

import re
from setuptools import find_packages, setup

# parameter variables
install_requires = []
package_data = {}

# determine requirements
with open('requirements.txt') as f:
    requirements = f.read()
for line in re.split('\n', requirements):
    if line and line[0] == '#' and '#egg=' in line:
        line = re.search(r'#\s*(.*)', line).group(1)
    if line and line[0] != '#':
        install_requires.append(line.strip())


package_data = {
    '': ['Makefile', '*.md']
}


if __name__ == '__main__':

    setup(
        name='chalice-local',
        version='0.1.1',
        description=' Small wrapper script to use AWS Chalice with LocalStack ',
        author='Waldemar Hummer',
        author_email='waldemar.hummer@gmail.com',
        url='https://github.com/localstack/localstack',
        scripts=['bin/chalice-local', 'bin/chalice-local.bat'],
        packages=find_packages(exclude=('tests', 'tests.*')),
        package_data=package_data,
        install_requires=install_requires,
        test_suite='tests',
        license='Apache License 2.0',
        zip_safe=False,
        classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Testing',
        ]
    )
