from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='Gabriel Athènes',
    author_email='gabriel.athenes@polytechnique.edu',

    py_modules=['my_pip_package'],
)
