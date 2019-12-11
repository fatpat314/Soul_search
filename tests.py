from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId

sample_id_list = ['hY7m5jjJ9mM','CQ85sUNBK7w']
sample_soul_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_soul = {
    'name': 'John',
    'price': '100'
}

sample_form_data = {
    'name': sample_soul['name'],
    'price': sample_soul['price']
}

class SoulsTest(TestCase):
    """Flask Tests."""
    def setUp(self):

        self.client = app.test_client()

        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage"""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_new(self):
        """Test new"""
        result = self.client.get('/souls/new')
        self.assertEqual(result.status, '200 OK')

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_soul(self, mock_find):
        '''Test showing a single soul'''
        mock_find.return_value = sample_soul

        result = self.client.get(f'/souls/{sample_soul_id}')
        self.assertEqual(result.status, '200 OK')


'''What am I not understanding about these tests?'''
    # # @mock.patch('pymongo.collection.Collection.update_one')
    # # def test_update_soul(self, mock_update):
    # #     result = self.client.post(f'/souls/{sample_soul_id}', data=sample_form_data)
    # #
    # #     self.assertEqual(result.status, '302 FOUND')
    # #     mock_update.assert_call_with({'_id': sample_soul_id}, {'$set': sample_soul})
    #
    # @mock.patch('pymongo.collection.Collection.delete_one')
    # def test_delete_soul(self, mock_delete):
    #     form_data = {'_method': 'DELETE'}
    #     result = self.client.post(f'/souls/{sample_soul_id}/delete', data=sample_form_data)
    #     self.assertEqual(result.status, '302 FOUND')
    #     mock_delete.assert_call_with({'_id': sample_soul_id})




if __name__ == '__main__':
    unittest_main()
