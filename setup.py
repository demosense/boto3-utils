import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6 is not supported')

setup(name='boto3_utils',
      version='1.0.0',
      description='Python package for some functionality related with AWS Boto3 SDK, specially useful in AWS Lambda.'
                  'The functionality does an atomic operation to avoid connexion interruptions, also downloads the '
                  'zip data on RAM to avoid disk size limits',
      author='Adrian Sanchez',
      author_email='adrian.sanchez@demosense.com',
      packages=find_packages('.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      )
