from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

pkg_vars = {}

with open('pycfdi/_version.py') as f:
    exec(f.read(), pkg_vars)

setup(
    name='pycfdi',
    author='VECO',
    version=pkg_vars['__version__'],
    include_package_data=True,
    install_requires=install_requires,
)
