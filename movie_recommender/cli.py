"""Program main file."""
import click


@click.command()
@click.argument('data', required=True, type=click.File('r'))
@click.argument('movies', required=True)
def main(data, movies):
    """A simple item-based recommender system."""
    click.echo('Howdy, I see u like {movies}'.format(movies=movies))


if __name__ == '__main__':
    main()
