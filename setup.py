from distutils.core import setup
from pycfdi import __version__

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='pycfdi',
    author='VECO',
    version=__version__,
    include_package_data=True,
    install_requires=install_requires,
)
