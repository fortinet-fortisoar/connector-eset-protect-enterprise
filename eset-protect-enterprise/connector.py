""" Copyright start
  MIT License
  Copyright (c) 2024 Fortinet Inc
  Copyright end """


from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import operations_map
logger = get_logger('eset-protect-enterprise')


class EsetEnterprise(Connector):
    def execute(self, config, operation, params, **kwargs):
        action = operations_map.get(operation)
        return action(config, params)

    def check_health(self, config):
        try:
            logger.info('executing check health')
            return
        except Exception as exp:
            logger.exception(str(exp))
            raise ConnectorError(str(exp))
