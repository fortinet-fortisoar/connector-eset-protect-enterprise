""" Copyright start
  MIT License
  Copyright (c) 2024 Fortinet Inc
  Copyright end """


from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations_map, authenticate
logger = get_logger('eset-protect-enterprise')


class EsetEnterprise(Connector):
    def execute(self, config, operation, params, **kwargs):
        connector_info = {"connector_name": self._info_json.get('name'),
                          "connector_version": self._info_json.get('version')}

        action = operations_map.get(operation)
        return action(config, params, connector_info)

    def check_health(self, config):
        connector_info = {"connector_name": self._info_json.get('name'),
                          "connector_version": self._info_json.get('version')}
        try:
            logger.info('executing check health')
            authenticate(config, connector_info)
            return True
        except Exception as exp:
            logger.exception(str(exp))
            raise ConnectorError(str(exp))
