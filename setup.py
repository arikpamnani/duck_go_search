from setuptools import setup

setup(
   name='duck-go',
   version='1.0',
   description='A command line utility for search on duckduckgo.com',
   author='Arik Pamnani',
   author_email='arikpamnani@gmail.com',
   packages=['duck-go'],  #same as name
   install_requires=['lxml', 'requests', 'urllib'], #external packages as dependencies
)
