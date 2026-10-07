import os
import unittest
from unittest.mock import Mock, patch
from fastapi.testclient import TestClient
from backend.app import app

class GatewayTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.payload = {'amount': 100, 'originCurrency': 'USD', 'destCurrency': 'INR', 'recommendation': {'name': 'Example'}}
    def test_key_stays_in_backend_header(self):
        result = Mock()
        result.json.return_value = {'candidates': [{'finishReason': 'STOP', 'content': {'parts': [{'text': 'Modeled comparison.'}]}}]}
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'private-test-key'}), patch('backend.app.requests.post', return_value=result) as send:
            response = self.client.post('/api/review', json=self.payload)
        self.assertEqual(response.json(), {'answer': 'Modeled comparison.'})
        self.assertNotIn('private-test-key', send.call_args.args[0])
        self.assertEqual(send.call_args.kwargs['headers']['x-goog-api-key'], 'private-test-key')
    def test_missing_key_returns_safe_unavailable(self):
        with patch.dict(os.environ, {'GEMINI_API_KEY': ''}):
            self.assertEqual(self.client.post('/api/review', json=self.payload).status_code, 503)
    def test_upstream_errors_are_not_exposed(self):
        import requests
        with patch.dict(os.environ, {'GEMINI_API_KEY': 'test'}), patch('backend.app.requests.post', side_effect=requests.Timeout('private response')):
            response = self.client.post('/api/review', json=self.payload)
        self.assertEqual(response.status_code, 502)
        self.assertNotIn('private', response.text)
