import unittest, mock

import dnschain
from dnschain.server import Server


class TestServerInstantiation(unittest.TestCase):

    @mock.patch('dnschain.server.httplib.HTTPConnection')
    def setUp(self, mock_connection):
        self.mock_connection = mock_connection
        self.assertTrue(dnschain.server.httplib.HTTPConnection is self.mock_connection)
        self.dnschain_server = Server("0.0.0.0", "FAKEFINGERPRINT")

    def test_invalid_address(self):
        pass

    def test_invalid_fingerprint(self):
        pass

    def test_invalid_domain_name(self):
        pass

    def test_valid_address_and_fingerprint(self):
        pass


class TestServerLookup(unittest.TestCase):

    @mock.patch('dnschain.server.json.loads')
    @mock.patch('dnschain.server.httplib.HTTPConnection')
    def setUp(self, mock_connection, mock_json_loads):
        self.mock_connection = mock_connection
        self.assertTrue(dnschain.server.httplib.HTTPConnection is self.mock_connection)
        self.dnschain_server = Server("0.0.0.0", "FAKEFINGERPRINT")
        self.dnschain_server.lookup("greg")

    def test_validrequest(self):
        print self.mock_connection

    def test_handle_nonascii_response(self):
        pass

    def test_no_match(self):
        pass


#class MaybeSubClassingIsTheCleanestWayForward 

if __name__ == '__main__':
    unittest.main()
