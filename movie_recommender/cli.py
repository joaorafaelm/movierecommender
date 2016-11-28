"""Program main file."""
import click
import json
from movie_recommender.recommender import RecommenderEngine, RecommenderModel


@click.command()
@click.argument('data', required=True, type=click.File('r'))
@click.argument('movies', required=True)
@click.option('--max-recommendations', default=5)
def main(data, movies, max_recommendations):
    """A simple item-based recommender system."""

    data = json.load(data)

    # As there are no ratings, using 1 as default value
    liked_movies = {x: 1 for x in movies.split(',')}

    user_based_model = RecommenderModel()

    for user in data.get('users'):
        user_based_model.add(
            identifier=user.get('user_id'),
            items=user.get('movies')
        )

    result = RecommenderEngine.get_recommendations(
        user_based_model, liked_movies, k=max_recommendations
    )

    for movie in result:
        click.echo('{id}\t{movie_name}'.format(
            id=movie[1],
            movie_name=data.get('movies').get(str(movie[1]))
        ))

if __name__ == '__main__':
    main()
    # data = {
    #     'movies': {
    #         '1': 'Harry Potter 1',
    #         '2': 'Harry Potter 2',
    #         '3': 'Twilight',
    #         '4': 'Lord of the Rings 1',
    #         '5': 'SW Episode I'
    #     },
    #     'users': [
    #         {
    #             'user_id': 1,
    #             'movies': [1, 2]
    #         },
    #         {
    #             'user_id': 2,
    #             'movies': [3]
    #         },
    #         {
    #             'user_id': 3,
    #             'movies': [1, 4, 5]
    #         },
    #         {
    #             'user_id': 4,
    #             'movies': [5]
    #         },
    #     ]
    # }
