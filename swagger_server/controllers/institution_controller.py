import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.request_institution_upd import RequestInstitutionUpd  # noqa: E501
from swagger_server import util


def add_institution(body):  # noqa: E501
    """Agrega una nueva instituciÃ³n

    Agrega una nueva instituciÃ³n # noqa: E501

    :param body: Crea una nueva instituciÃ³n
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = RequestInstitutionAdd.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_institution(institution_id):  # noqa: E501
    """Elimina una instituciÃ³n

    Elimina una instituciÃ³n # noqa: E501

    :param institution_id: Institution id to delete
    :type institution_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_institution():  # noqa: E501
    """Lista instituciones

    Lista instituciones # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_institution_by_id(institution_id):  # noqa: E501
    """Busca una instituciÃ³n por ID

    Busca una instituciÃ³n por ID # noqa: E501

    :param institution_id: Busca una instituciÃ³n por ID
    :type institution_id: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def update_institution(body):  # noqa: E501
    """Actualiza una instituciÃ³n existente

    Actualiza una instituciÃ³n existente # noqa: E501

    :param body: Actualiza una instituciÃ³n existente
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = RequestInstitutionUpd.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
