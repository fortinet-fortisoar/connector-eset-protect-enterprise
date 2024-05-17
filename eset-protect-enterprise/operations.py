from connectors.core.connector import ConnectorError, get_logger
import requests

logger = get_logger('eset-protect-enterprise')


def authenticate(config):
    username = config.get("server_username")
    password = config.get("server_password")
    base_url = config.get("base_url")
    auth_url = f"{base_url}/api/authentication"
    auth_data = {"username": username, "password": password}
    response = requests.post(auth_url, json=auth_data)
    if response.status_code == 200:
        return response.json()["token"]
    else:
        print("Authentication failed.")
        return None


def list_endpoints(config, params):
    try:
        base_url = config.get("base_url")
        token = authenticate()
        endpoints_url = f"{base_url}/api/endpoints"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(endpoints_url, headers=headers)
        if response.status_code == 200:
            return response.json()["endpoints"]
        else:
            logger.error("Failed to list endpoints.")
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def isolate_endpoint(config, params):
    try:
        base_url = config.get("base_url")
        endpoint_id = params.get("endpoint_id")
        token = authenticate()
        isolate_url = f"{base_url}/api/endpoints/{endpoint_id}/isolate"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(isolate_url, headers=headers)
        if response.status_code == 200:
            logger.info(f"Endpoint {endpoint_id} has been isolated successfully.")
            return True
        else:
            raise ConnectorError(f"Failed to isolate endpoint {endpoint_id}.")
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def rejoin_endpoint(config, params):
    try:
        base_url = config.get("base_url")
        endpoint_id = params.get("endpoint_id")
        token = authenticate()
        rejoin_url = f"{base_url}/api/endpoints/{endpoint_id}/rejoin"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(rejoin_url, headers=headers)
        if response.status_code == 200:
            logger.info(f"Endpoint {endpoint_id} has rejoined the network successfully.")
            return True
        else:
            raise ConnectorError(f"Failed to rejoin endpoint {endpoint_id}.")
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def list_events(config, params):
    try:
        base_url = config.get("base_url")
        token = authenticate()
        events_url = f"{base_url}/api/events"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(events_url, headers=headers)
        if response.status_code == 200:
            return response.json()["events"]
        else:
            raise ConnectorError("Failed to list events.")
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def list_incidents(config, params):
    try:
        base_url = config.get("base_url")
        token = authenticate()
        incidents_url = f"{base_url}/api/incidents"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(incidents_url, headers=headers)
        if response.status_code == 200:
            return response.json()["incidents"]
        else:
            raise ConnectorError("Failed to list incidents.")
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def list_files(config, params):
    try:
        base_url = config.get("base_url")
        token = authenticate()
        files_url = f"{base_url}/api/files"
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(files_url, headers=headers)
        if response.status_code == 200:
            return response.json()["files"]
        else:
            raise ConnectorError("Failed to list files.")
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


operations_map = {
    'list_endpoints': list_endpoints,
    'isolate_endpoint': isolate_endpoint,
    'rejoin_endpoint': rejoin_endpoint,
    'list_files': list_files,
    'list_incidents': list_incidents,
    'list_events': list_events
}
