from connectors.core.connector import ConnectorError, get_logger
import requests

logger = get_logger('eset-protect-enterprise')


def authenticate(config):
    try:
        username = config.get("server_username")
        password = config.get("server_password")
        base_url = config.get("base_url")
        auth_url = f"{base_url}/oauth/token"
        auth_data = {"grant_type":"password", "username": username, "password": password, "refresh_token": "refresh_token"}
        headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(auth_url, data=auth_data, headers=headers)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            logger.error("Authentication failed.")
            raise ConnectorError('Authentication failed. {}'.format(str(response)))
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def get_executables(config, params):
    try:
        token = authenticate(config)
        base_url = "https://eu.application-management.eset.systems" #config.get("base_url")
        headers = {"Authorization": token, "accept": "application/json"}
        executableUuid = params.get("executableUuid")
        query_params = {}
        if executableUuid:
            endpoints_url = f"{base_url}/v1/executables/{executableUuid}"
        else:
            endpoints_url = f"{base_url}/v1/executables"
            if params.get("pageSize"):
                query_params.update({"pageSize": params.get("pageSize")})
            if params.get("pageToken"):
                query_params.update({"pageToken": params.get("pageToken")})

        response = requests.get(endpoints_url, headers=headers, params=query_params)
        if response.status_code == 200:
            return response.json()
        else:
            raise ConnectorError('Failed to get all executables {}'.format(str(response)))
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def block_unblock_executables(config, params, action):
    try:
        token = authenticate(config)
        base_url = "https://eu.application-management.eset.systems" #config.get("base_url")
        headers = {"Authorization": token, "accept": "application/json", "Content-Type": "application/json"}
        executableUuid = params.get("executableUuid")
        endpoints_url = f"{base_url}/v1/executables/{executableUuid}:{action}"
        data = params.get("json_data", {})
        response = requests.get(endpoints_url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise ConnectorError('Failed to get all executables {}'.format(str(response)))
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def block_executables(config, params):
    return block_unblock_executables(config, params, "block")


def unblock_executables(config, params):
    return block_unblock_executables(config, params, "unblock")


operations_map = {
    'get_executables': get_executables,
    'block_executables': block_executables,
    'unblock_executables': unblock_executables
}
