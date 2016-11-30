# Movie Recommender

A movie recommender system.

# Development

Run:

    $ pip install -r requirements.txt

Running tests:

    $ tox


# Installation

To install it as a package, run:

    $ pip install .


# Usage

To use it:

    $ movie-recommender [OPTIONS] <filename> <movies_ids>

filename: JSON file with data. Check tests/sample.json or movies.json.

movies_ids: list of ids separated by comma.

OPTIONS:
    --max-recommendations=INTEGER (Default: 5)
    --help


