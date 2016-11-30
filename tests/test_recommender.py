# coding=utf-8
"""Test Recommender Engine and Model."""
import pytest
import unittest
from movie_recommender.recommender import euclidean_distance
from movie_recommender.recommender import RecommenderEngine, RecommenderModel


class TestRecommender(unittest.TestCase):
    """Recommender test based class"""

    _model = None
    _data = {
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

    @pytest.mark.first
    def test_recommender_model(self):
        """Validate base model."""

        self._model = RecommenderModel()
        for user in self._data.get('users'):
            self._model.add(
                identifier=user.get('user_id'),
                items=user.get('movies')
            )

        self.assertEqual(type(self._model), RecommenderModel)

        # validate if data structure is consistent with data
        self.assertEqual(
            sorted(list(map(int, list(self._model.get('1'))))),
            self._data['users'][0]['movies']
        )

        # validate item insertion
        self._model.add(identifier='6', items={'1': 5.0})
        self.assertEqual(self._model.get('6'), {'1': 5.0})

    @pytest.mark.second
    def test_recommendations_model(self):
        """Validate recommendations."""

        self._model = RecommenderModel()
        for user in self._data.get('users'):
            self._model.add(
                identifier=user.get('user_id'),
                items=user.get('movies')
            )

        max_recommendations = 3
        result = RecommenderEngine.get_recommendations(
            self._model, {'1': 1}, k=max_recommendations
        )

        self.assertLessEqual(len(result), max_recommendations)

        recommended_movies_ids = sorted([x[1] for x in result])
        self.assertEqual(recommended_movies_ids, ['2', '4', '5'])

    def test_similarity_func(self):
        """Validate similarity between two users(considering rating values)"""

        # Less similarity
        self.assertLess(
            euclidean_distance({'1': 5.0}, {'1': 3.0}),
            1
        )

        # max similiarity value: 1
        self.assertEqual(
            euclidean_distance({'1': 5.0}, {'1': 5.0}),
            1
        )

        # no similiarity
        self.assertEqual(
            euclidean_distance({'1': 5.0}, {'2': 5.0}),
            0
        )
