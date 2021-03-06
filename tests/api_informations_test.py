# -*- coding: utf-8 -*-
import sys, os, json, unittest, urllib
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/')
import app

class ApiInformationsTestCase(unittest.TestCase):
    def setUp(self):
        app.app.debug = False
        self.app = app.app.test_client()

    def test_create(self):
        content_body = {
            'content'  : 'content-1',
            'state'    : '2'
        }
        raw_response = self.app.post(
            '/informations/',
            content_type='application/json',
            data=json.dumps(content_body)
        )
        assert raw_response.status_code == 201
        response = json.loads(raw_response.data)
        assert response['result'] != ''
        assert response['result']['id'] != ''
        assert response['result']['state'] == 2
        assert response['result']['content'] == 'content-1'

    def test_invalid_create(self):
        content_body = {
            'state'    : '2'
        }
        raw_response = self.app.post(
            '/informations/',
            content_type='application/json',
            data=json.dumps(content_body)
        )
        assert raw_response.status_code == 400

    def test_index(self):
        raw_response = self.app.get(
            '/informations/'
        )
        assert raw_response.status_code == 200
        response = json.loads(raw_response.data)
        assert response['result'] != ''
        assert response['result'][0]['id'] is not None
        assert response['result'][0]['state'] is not None
        assert response['result'][0]['content'] is not None

    def test_read(self):
        content_body = {
            'content'  : 'content-2',
            'state'    : '1'
        }
        raw_response = self.app.post(
            '/informations/',
            content_type='application/json',
            data=json.dumps(content_body)
        )
        created = json.loads(raw_response.data)
        raw_response = self.app.get(
            '/informations/%d' % created['result']['id']
        )
        assert raw_response.status_code == 200
        response = json.loads(raw_response.data)
        assert response['result']['id'] == created['result']['id']
        assert response['result']['state'] == created['result']['state']
        assert response['result']['content'] == created['result']['content']

    def test_unknown_read(self):
        raw_response = self.app.get(
            '/informations/%d' % 1000000
        )
        assert raw_response.status_code == 404

    def test_update(self):
        content_body = {
            'content'  : 'content-3',
            'state'    : '2'
        }
        raw_response = self.app.post(
            '/informations/',
            content_type='application/json',
            data=json.dumps(content_body)
        )
        created = json.loads(raw_response.data)
        content_body = {
            'content'  : 'content-33',
            'state'    : '3'
        }
        raw_response = self.app.put(
            '/informations/%d' % created['result']['id'],
            content_type='application/json',
            data=json.dumps(content_body)
        )
        assert raw_response.status_code == 201
        response = json.loads(raw_response.data)
        assert response['result']['id'] == created['result']['id']
        assert response['result']['state'] == 3
        assert response['result']['content'] == 'content-33'

    def test_unknown_update(self):
        content_body = {
            'content'  : 'anything',
            'state'    : '3'
        }
        raw_response = self.app.put(
            '/informations/%d' % 1000000,
            content_type='application/json',
            data=json.dumps(content_body)
        )
        assert raw_response.status_code == 404

    def test_delete(self):
        content_body = {
            'content'  : 'content-4',
            'state'    : '3'
        }
        raw_response = self.app.post(
            '/informations/',
            content_type='application/json',
            data=json.dumps(content_body)
        )
        created = json.loads(raw_response.data)
        raw_response = self.app.delete(
            '/informations/%d' % created['result']['id']
        )
        assert raw_response.status_code == 204

    def test_unknown_delete(self):
        raw_response = self.app.delete(
            '/informations/%d' % 100000
        )
        assert raw_response.status_code == 404

if __name__ == '__main__':
    unittest.main()
