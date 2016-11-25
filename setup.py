"""A simple item-based recommender system."""
from os.path import join, dirname
from setuptools import find_packages, setup


def get_requirements(filename):
    """
    Retrieve dependencies from file.

    Args:
        filename (str): name of the requirements file.
    Returns:
        list: list of packages.
    """
    try:
        return open(join(dirname(__file__), filename)).read().splitlines()
    except IOError:
        return []

dependencies = get_requirements('requirements.txt')

setup(
    name='movierecommender',
    version='0.1.0',
    url='https://github.com/joaorafaelm/python-movierecommender',
    license='BSD',
    author='Joao Rafael Martins de Oliveira',
    author_email='joaoraf@me.com',
    description='A simple item-based recommender system.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'movie-recommender = movie_recommender.cli:main'
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
