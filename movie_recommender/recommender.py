"""Recommender base classes and methods."""


def euclidean_distance(person_1, person_2):
    """Returns a distance-base similarity score for person1 and person2.

    Args:
        person_1 (dict): Dictionary with identifier => rating
        person_2 (dict): Dictionary with identifier => rating

    Returns:
        float: Similarity between person_1 and person_2
    """

    # if they have no items in common, return 0
    if len({item: 1 for item in person_1 if person_2.get(item)}) == 0:
        return 0

    # Add up the squares of all differences
    sum_of_squares = sum(
        [
            pow(
                person_1[item] - person_2[item], 2
            ) for item in person_1 if person_2.get(item)
        ]
    )

    return 1 / (1 + sum_of_squares)


class RecommenderModel(object):
    items = {}

    def add(self, identifier, items):
        """Add item into list of item.
        Args:
            identifier (string): data identifier
            items (list, dict): items with or without ratings.
        """
        ratings = self.items.get(str(identifier), {})
        if isinstance(items, (list, tuple,)):
            ratings.update({str(i): 1 for i in items})
        elif isinstance(items, dict):
            ratings.update(items.copy())

        self.items.update({
            str(identifier): ratings
        })

    def get(self, identifier):
        """Returns item from item list
        Args:
            identifier (int, string): item identifier.
        Returns:
            dict: dictionary with item ratings.
        """
        return self.items.get(identifier)

    def iteritems(self):
        """
        Returns items from dictionary.
        This method will use more memory in python 2.x, as it builds a
        temporary list instead of a generator.
        """
        return self.items.items()


class RecommenderEngine(object):

    @staticmethod
    def get_recommendations(
            item_model, person,
            similarity=euclidean_distance, k=5
    ):
        """
        Get recommendations for an item by using a weighted average
        of every other user's rankings.

        Args:
            item_model (RecommenderModel): Model containing items.
            person (dict): dictionary of ratings. (default rating value: 1)
            similarity (function): Similarity function.
            k (int): maximum number of recommendations.
        Returns:
            list: List of items containing respective similarity value.
        """
        totals = {}
        similarity_sum = {}

        for item in item_model.iteritems():
            sim = similarity(person, item[1])

            # ignore similarities of zero or lower
            if sim <= 0:
                continue

            for rating in item[1]:

                # only consider items that are not in  the list
                if person == 0 or not person.get(rating):

                    # Similarity * score
                    totals.setdefault(rating, 0)
                    totals[rating] += item[1][rating] * sim

                    # Sum of similarities
                    similarity_sum.setdefault(rating, 0)
                    similarity_sum[rating] += sim

        # Normalized list
        rankings = [
                (total / similarity_sum[rating], rating) for rating, total in
                totals.items()
            ]

        rankings.sort()
        rankings.reverse()

        return rankings[:k]

if __name__ == '__main__':
    data = {
        'movies': {
            '1': 'Harry Potter 1',
            '2': 'Harry Potter 2',
            '3': 'Twilight',
            '4': 'Lord of the Rings 1',
            '5': 'SW Episode I'
        },
        'users': [
            {
                'user_id': 1,
                'movies': [1, 2]
            },
            {
                'user_id': 2,
                'movies': [3]
            },
            {
                'user_id': 3,
                'movies': [1, 4, 5]
            },
            {
                'user_id': 4,
                'movies': [5]
            },
        ]
    }

    # import json
    # with open('movies.json') as data_file:
    #     data = json.load(data_file)

    user_based_model = RecommenderModel()
    for user in data.get('users'):
        user_based_model.add(
            identifier=user.get('user_id'),
            items=user.get('movies')
        )
    result = RecommenderEngine.get_recommendations(user_based_model, {'4': 1})
    movies = [data.get('movies').get(str(i[1])) for i in result]

    print(movies)

