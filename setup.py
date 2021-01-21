from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(name='finvizscrape',
      version='1.0.0',
      description='Scrape data to Finviz.com/screener.ashx',
      long_description=README,
      long_description_content_type="text/markdown",
      url='https://github.com/mavalente92/finvizscrape/',
      author='Matteo Valente',
      author_email='mavalente92@gmail.com',
      license='MIT',
      install_requires=[
          'requests',
          'bs4',
          'lxml',
          'pandas'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=['finvizscrape'])
