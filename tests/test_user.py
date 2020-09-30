from tests.setting import Setting
import json
from unittest.mock import patch
import app.search_users as search_users


class TestUser(Setting):
    def test_get_users_living(self):
        """
        Test to retrieve users who are listed as living in a city
        :return:
        """
        with self.client:
            response = self.client.get(
                '/users/live/city'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'] == 'success')
            self.assertIsInstance(data['users'], list)

    def test_get_users_current_vicinity(self):
        """
        Test to retrieve users whose current coordinates are within 50 miles of a city
        :return:
        """
        with self.client:
            response = self.client.get(
                '/users/current/vicinity'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data['status'] == 'success')
            self.assertIsInstance(data['users'], list)

    @patch.object(search_users, 'get_user_data_by_live_place')
    @patch('app.const.HTTP_ERROR', True)
    def test_get_users_living_error(self, mock_get_user_data_by_live_place):
        """
        Test to retrieve users who are listed as living in a city with 404 error
        :return:
        """
        mock_api_result = {
            'message': 'user not found',
            'status_code': 404
        }
        mock_get_user_data_by_live_place.return_value = mock_api_result
        with self.client:
            response = self.client.get(
                    '/users/live/city'
                )
            self.assertTrue(mock_get_user_data_by_live_place.called)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data['status'] == 'HTTP error')
            self.assertTrue(data['message'] == 'user not found')

    @patch.object(search_users, 'get_all_user_data')
    @patch('app.const.HTTP_ERROR', True)
    def test_get_user_data_by_vicinity_error(self, mock_get_all_user_data):
        """
        Test to retrieve users whose current coordinates are within 50 miles of a city
        :return:
        """
        mock_api_result = {
            'message': 'user not found',
            'status_code': 404
        }
        mock_get_all_user_data.return_value = mock_api_result
        with self.client:
            response = self.client.get(
                    '/users/current/vicinity'
                )
            self.assertTrue(mock_get_all_user_data.called)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertTrue(data['status'] == 'HTTP error')
            self.assertTrue(data['message'] == 'user not found')
