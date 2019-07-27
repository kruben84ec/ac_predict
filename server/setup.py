from setuptools import setup, find_packages

setup(
    name='sv',
    version='0.1',
    py_modules=['sv'],
    install_requires=[
        'numpy',
        'matplotlib',
        'sklearn',
        'flask',
        'flask_restfull',
        'flask_mysqldb',
        'pymysql',
        'requests',
        'gunicorn',
        'keras',
        'tensorflow',
        'flask_cors'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
