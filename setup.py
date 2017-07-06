from setuptools import setup

setup(
   name='duck_go_search',
   version='1.0',
   description='A command line utility for search on duckduckgo.com',
   author='Arik Pamnani',
   author_email='arikpamnani@gmail.com',
   packages=['duck_go_search'],  
   install_requires=['lxml', 'urllib', 'requests'], 
   url='https://github.com/arikpamnani/duck_go_search',
)
