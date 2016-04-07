import os
from setuptools import setup, find_packages


VERSION = '0.0.1'

install_requires = [
]

here = os.path.dirname(os.path.abspath(__file__))
# get documentation from the README and HISTORY
try:
    with open(os.path.join(here, 'README.rst')) as doc:
        readme = doc.read()
except:
    readme = ''

try:
    with open(os.path.join(here, 'HISTORY.rst')) as doc:
        history = doc.read()
except:
    history = ''

long_description = readme + '\n\n' + history

if __name__ == '__main__':
    setup(
        name='pyJetpackID',
        version=VERSION,
        description='Takes the Jetpack add-on manifest object, and returns the add-on ID.',
        long_description=long_description,
        keywords='mozilla firefox jetpack jpm addon extension utilities',
        author='Askeing Yen',
        author_email='askeing@gmail.com',
        url='https://github.com/askeing/pyJetpackID',
        packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
        package_data={},
        install_requires=install_requires,
        zip_safe=False,
    )
