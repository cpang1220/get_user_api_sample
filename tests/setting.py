from app import app
from flask_testing import TestCase


class Setting(TestCase):
    def create_app(self):
        """
        :return:
        """
        return app

    def setUp(self):
        """
        :return:
        """

    def tearDown(self):
        """
        :return:
        """
