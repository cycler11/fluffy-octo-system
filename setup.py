from setuptools import setup, find_packages

setup(
    name='library_app',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'library-app = app.cli:main'
        ]
    },
)