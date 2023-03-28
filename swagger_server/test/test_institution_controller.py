# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.request_institution_upd import RequestInstitutionUpd  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInstitutionController(BaseTestCase):
    """InstitutionController integration test stubs"""

    def test_add_institution(self):
        """Test case for add_institution

        Agrega una nueva instituciÃ³n
        """
        body = RequestInstitutionAdd()
        response = self.client.open(
            '/rest/globalhitss-api/v1.0/institution',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_institution(self):
        """Test case for delete_institution

        Elimina una instituciÃ³n
        """
        response = self.client.open(
            '/rest/globalhitss-api/v1.0/institution/{institutionId}'.format(institution_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_institution(self):
        """Test case for get_institution

        Lista instituciones
        """
        response = self.client.open(
            '/rest/globalhitss-api/v1.0/institution',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_institution_by_id(self):
        """Test case for get_institution_by_id

        Busca una instituciÃ³n por ID
        """
        response = self.client.open(
            '/rest/globalhitss-api/v1.0/institution/{institutionId}'.format(institution_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_institution(self):
        """Test case for update_institution

        Actualiza una instituciÃ³n existente
        """
        body = RequestInstitutionUpd()
        response = self.client.open(
            '/rest/globalhitss-api/v1.0/institution',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
