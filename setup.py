from setuptools import setup, find_packages

setup(
    name='oreno-pj2',
    version='0.0.1',

    description="Oreno Sample Project",
    license='GPLv2',

    author='inokappa',
    author_email='xxxxxxxxxxxxxxxxx',

    packages=find_packages(
        exclude=['tests']
    ),

    test_suite='tests',

    install_requires=[
        'boto3'
    ],

    tests_require=[
        'moto'
    ],

    entry_points={
        'console_scripts': [
            'ec2 = ec2:main'
        ]
    },
)
