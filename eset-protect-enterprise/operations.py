""" Copyright start
  MIT License
  Copyright (c) 2024 Fortinet Inc
  Copyright end """


from connectors.core.connector import ConnectorError, get_logger
import requests
from datetime import datetime, timedelta
from connectors.core.utils import update_connnector_config

logger = get_logger('eset-protect-enterprise')


def make_api_call(config, connector_info,  url, method="GET", params=None, data=None, json_data={}):
    try:
        token = authenticate(config, connector_info)
        headers = {"Authorization": token, "accept": "application/json", "Content-Type": "application/json"}
        response = requests.request(method=method, url=url,
                                    headers=headers, data=data, json=json_data, params=params, verify=config.get("verify_ssl"))
        if response.ok:
            if response.content:
                response = response.json()
            else:
                response = {"Success": "No Data Returned"}
            return response
        logger.error(response)
        raise ConnectorError(str(response))
    except Exception as e:
        if 'Max retries exceeded' in str(e):
            raise ConnectorError(
                'Max retries exceeded. Please check the URL provided for configuration of connector')
        raise ConnectorError(e)


def validate_token(config):
    current_time = datetime.now()
    expires_in = datetime.strptime(config.get("expires_in", ""), "%Y-%m-%d %H:%M:%S.%f")
    if config.get("expires_in") and  expires_in < current_time:
        return True
    return False


def generate_auth_token(config, connector_info, refresh_token=False):
    username = config.get("server_username")
    password = config.get("server_password")
    base_url = config.get("base_url")
    auth_url = f"{base_url}/oauth/token"
    auth_data = {"grant_type": "password", "username": username, "password": password}
    if refresh_token:
        auth_data = {"grant_type": "refresh_token", "refresh_token": config.get("refresh_token")}
    headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(auth_url, data=auth_data, headers=headers)
    if response.status_code == 200:
        config["refresh_token"] = response.json()["refresh_token"]
        config["access_token"] = response.json()["access_token"]
        current_time = datetime.now()
        new_time = current_time + timedelta(seconds=response.json()["expires_in"])
        config["expires_in"] = str(new_time)
        update_connnector_config(connector_info['connector_name'], connector_info['connector_version'],
                                 config, config.get("config_id"))
        return response.json()["access_token"]
    else:
        logger.error("Authentication failed.")
        raise ConnectorError('Authentication failed. {}'.format(str(response)))


def authenticate(config, connector_info):
    try:
        if config.get("access_token"):
            if validate_token(config):
                return config.get("access_token")
            return generate_auth_token(config, connector_info, True)
        else:
            return generate_auth_token(config, connector_info)
    except Exception as err:
        logger.exception('An exception occurred {}'.format(str(err)))
        raise ConnectorError('An exception occurred {}'.format(str(err)))


def get_executables(config, params, connector_info):
    try:
        base_url = params.get("server_url")
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
        return make_api_call(config, connector_info, endpoints_url, params=query_params)
    except Exception as err:
        logger.exception('Failed to get all executables {}'.format(str(err)))
        raise ConnectorError('Failed to get all executables {}'.format(str(err)))


def block_unblock_executables(config, params, connector_info, action):
    try:
        base_url = params.get("server_url")
        executableUuid = params.get("executableUuid")
        endpoints_url = f"{base_url}/v1/executables/{executableUuid}:{action}"
        data = params.get("json_data", {})
        return make_api_call(config, connector_info, endpoints_url, data=data)
    except Exception as err:
        logger.exception('Failed to block/unblock executables {}'.format(str(err)))
        raise ConnectorError('Failed to block/unblock executables {}'.format(str(err)))


def block_executables(config, params, connector_info):
    return block_unblock_executables(config, params, connector_info, "block")


def unblock_executables(config, params, connector_info):
    return block_unblock_executables(config, params, connector_info, "unblock")


def get_device(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        deviceUuid = params.get("deviceUuid")
        endpoints_url = f"{base_url}/v1/devices/{deviceUuid}"
        return make_api_call(config, connector_info, endpoints_url)
    except Exception as err:
        logger.exception('Failed to get device. {}'.format(str(err)))
        raise ConnectorError('Failed to get device. {}'.format(str(err)))


def get_device_groups(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        groupUuid = params.get("groupUuid")
        query_params = {}
        if groupUuid:
            endpoints_url = f"{base_url}/v1/device_groups/{groupUuid}/devices"
        else:
            endpoints_url = f"{base_url}/v1/device_groups"
        if params.get("pageSize"):
            query_params.update({"pageSize": params.get("pageSize")})
        if params.get("pageToken"):
            query_params.update({"pageToken": params.get("pageToken")})
        return make_api_call(config, connector_info, endpoints_url, params=query_params)
    except Exception as err:
        logger.exception('Failed to get device group. {}'.format(str(err)))
        raise ConnectorError('Failed to get device group. {}'.format(str(err)))


def get_detections(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        detectionUuid = params.get("detectionUuid")
        query_params = {}
        if detectionUuid:
            endpoints_url = f"{base_url}/v1/detections/{detectionUuid}"
        else:
            endpoints_url = f"{base_url}/v1/detections"
            if params.get("deviceUuid"):
                query_params.update({"deviceUuid": params.get("deviceUuid")})
            if params.get("start_time"):
                query_params.update({"startTime": params.get("start_time")})
            if params.get("end_time"):
                query_params.update({"endTime": params.get("end_time")})
            if params.get("pageSize"):
                query_params.update({"pageSize": params.get("pageSize")})
            if params.get("pageToken"):
                query_params.update({"pageToken": params.get("pageToken")})
        return make_api_call(config, connector_info, endpoints_url, params=query_params)
    except Exception as err:
        logger.exception('Failed to get device group. {}'.format(str(err)))
        raise ConnectorError('Failed to get device group. {}'.format(str(err)))


def get_detection_groups(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        detectionGroupUuid = params.get("detectionGroupUuid")
        query_params = {}
        if detectionGroupUuid:
            endpoints_url = f"{base_url}/v2/detection-groups/{detectionGroupUuid}"
        else:
            endpoints_url = f"{base_url}/v2/detection-groups"
            if params.get("deviceUuid"):
                query_params.update({"deviceUuid": params.get("deviceUuid")})
            if params.get("start_time"):
                query_params.update({"startTime": params.get("start_time")})
            if params.get("end_time"):
                query_params.update({"endTime": params.get("end_time")})
            if params.get("pageSize"):
                query_params.update({"pageSize": params.get("pageSize")})
            if params.get("pageToken"):
                query_params.update({"pageToken": params.get("pageToken")})
        return make_api_call(config, connector_info, endpoints_url, params=query_params)
    except Exception as err:
        logger.exception('Failed to get device group. {}'.format(str(err)))
        raise ConnectorError('Failed to get device group. {}'.format(str(err)))


def get_device_tasks(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        task_uuid = params.get("task_uuid")
        query_params = {}
        if task_uuid:
            endpoints_url = f"{base_url}/v1/device_tasks/{task_uuid}"
        else:
            endpoints_url = f"{base_url}/v1/device_tasks"
            if params.get("pageSize"):
                query_params.update({"pageSize": params.get("pageSize")})
            if params.get("pageToken"):
                query_params.update({"pageToken": params.get("pageToken")})
        return make_api_call(config, connector_info, endpoints_url, params=query_params)
    except Exception as err:
        logger.exception('Failed to get device group. {}'.format(str(err)))
        raise ConnectorError('Failed to get device group. {}'.format(str(err)))


def isolate_computer_from_network(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        endpoints_url = f"{base_url}/v1/device_tasks"
        task_expire_time = params.get("task_expire_time")
        current_time = datetime.now()
        new_time = current_time + timedelta(minutes=task_expire_time)
        formatted_time = new_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        isolation_device = {
            "task": {
            "description": params.get("device_uuid", "IsolateDeviceASAP"),
            "displayName": params.get("device_uuid", "IsolateDevice"),
            "targets": {
                 "devicesUuids": [params.get("device_uuid")],
                 "deviceGroupsUuids": [params.get("device_group_uuid")]
            },
            "triggers": [{
                 "manual": {
                         "expireTime": formatted_time
                }
            }],
            "action": {
                 "name": "StartNetworkIsolation"
                }
            }
        }
        params.get("device_uuid")
        return make_api_call(config, connector_info, endpoints_url, json_data=isolation_device, method="POST")
    except Exception as err:
        logger.exception('Failed to get device group. {}'.format(str(err)))
        raise ConnectorError('Failed to get device group. {}'.format(str(err)))


def end_computer_isolation_from_network(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        endpoints_url = f"{base_url}/v1/device_tasks"
        task_expire_time = params.get("task_expire_time")
        current_time = datetime.now()
        new_time = current_time + timedelta(minutes=task_expire_time)
        formatted_time = new_time.strftime('%Y-%m-%dT%H:%M:%SZ')
        isolation_device = {
            "task": {
            "description": params.get("device_uuid", "IsolateDeviceASAP"),
            "displayName": params.get("device_uuid", "IsolateDevice"),
            "targets": {
                 "devicesUuids": [params.get("device_uuid")],
                 "deviceGroupsUuids": [params.get("device_group_uuid")]
            },
            "triggers": [{
                 "manual": {
                         "expireTime": formatted_time
                }
            }],
            "action": {
                 "name": "EndNetworkIsolation"
                }
            }
        }
        params.get("device_uuid")
        return make_api_call(config, connector_info, endpoints_url, json_data=isolation_device, method="POST")
    except Exception as err:
        logger.exception('Failed to get device group. {}'.format(str(err)))
        raise ConnectorError('Failed to get device group. {}'.format(str(err)))


def create_device_tasks(config, params, connector_info):
    try:
        base_url = params.get("server_url")
        endpoints_url = f"{base_url}/v1/device_tasks"
        task_payload = params.get("task_payload")
        return make_api_call(config, connector_info, endpoints_url, json_data=task_payload, method="POST")
    except Exception as err:
        logger.exception('Failed to get device tasks. {}'.format(str(err)))
        raise ConnectorError('Failed to get device tasks. {}'.format(str(err)))


operations_map = {
    'get_executables': get_executables,
    'block_executables': block_executables,
    'unblock_executables': unblock_executables,
    'get_device': get_device,
    'get_device_groups': get_device_groups,
    'get_detections': get_detections,
    'get_detection_groups': get_detection_groups,
    'get_device_tasks': get_device_tasks,
    'isolate_computer_from_network': isolate_computer_from_network,
    'create_device_tasks': create_device_tasks,
    'end_computer_isolation_from_network': end_computer_isolation_from_network
}
