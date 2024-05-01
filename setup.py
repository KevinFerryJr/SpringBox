from setuptools import setup, find_packages

with open("README.md", "r") as f:
	long_description = f.read()

setup(
	name='SpringBox',
	version='0.0.1',
	packages=find_packages(),
	install_requires=[],
	author='Kevin Ferry Jr.',
	author_email='kevinferrydesign@gmail.com',
	description='A minimal physics module, primarily written for use with the "Jiggle" module.',
	url='https://github.com/KevinFerryJr/JiggleEngine',
)