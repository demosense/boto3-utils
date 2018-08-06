import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

setup(name='demotimetable',
      version='1.0.0',
      description='Provides the common functionality for the timetable functionality that calculates if a given time '
                  'is on the ACTIVE or INACTIVE range.',
      author='Adrian Sanchez',
      author_email='adrian.sanchez@demosense.com',
      packages=find_packages('.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      )
