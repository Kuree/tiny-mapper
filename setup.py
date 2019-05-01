from setuptools import setup

setup(
    name='tiny-mapper',
    version='0.0.1',
    description='Tiny mapper for CGRA',
    packages=["tiny_mapper"],
    license='BSD License',
    url='https://github.com/Kuree/tiny-mapper',
    author='Keyi Zhang',
    author_email='keyi@cs.stanford.edu',
    install_requires=["coreir", "igraph"],
    zip_safe=False,
)
