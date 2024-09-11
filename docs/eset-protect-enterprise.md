## About the connector
ESET Protect Enterprise extended detection and response (XDR) that delivers enterprise-grade visibility, threat hunting and response options.
<p>This document provides information about the ESET Protect Enterprise Connector, which facilitates automated interactions, with a ESET Protect Enterprise server using FortiSOAR&trade; playbooks. Add the ESET Protect Enterprise Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with ESET Protect Enterprise.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-eset-protect-enterprise</pre>

## Prerequisites to configuring the connector
- You must have the credentials of ESET Protect Enterprise server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the ESET Protect Enterprise server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>ESET Protect Enterprise</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>URL for the ESET Enterprise server from where the connector gets notifications.
</td>
</tr><tr><td>Username</td><td>Username to access the ESET Enterprise server.
</td>
</tr><tr><td>Password</td><td>Password to access the ESET Enterprise server.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Executables List</td><td>Retrieves a list of all the executables from ESET.</td><td>get_executables <br/>Investigation</td></tr>
<tr><td>Get Device Tasks List</td><td>Retrieves a list of all device tasks.</td><td>get_device_tasks <br/>Investigation</td></tr>
<tr><td>Get Detections List</td><td>Retrieves a list of all the detections.</td><td>get_detections <br/>Investigation</td></tr>
<tr><td>Get Detection Groups List</td><td>Retrieves a list of all the detections groups.</td><td>get_detection_groups <br/>Investigation</td></tr>
<tr><td>Get Device by UUID</td><td>Retrieves all details of the device.</td><td>get_device <br/>Investigation</td></tr>
<tr><td>Get Device Groups List</td><td>Retrieves all details of device group.</td><td>get_device_groups <br/>Investigation</td></tr>
<tr><td>Create Device Task</td><td>Create device task. Created task requires to have at least one trigger set. Otherwise the call fails.</td><td>create_device_tasks <br/>Containment</td></tr>
<tr><td>Isolate Computer From Network</td><td>Isolate computer from network.</td><td>isolate_computer_from_network <br/>Containment</td></tr>
<tr><td>End Computer Isolation From Network</td><td>End computer isolation from network.</td><td>end_computer_isolation_from_network <br/>Containment</td></tr>
<tr><td>Block Executables</td><td>Block executables by provided UUID</td><td>block_executables <br/>Containment</td></tr>
<tr><td>Unblock Executables</td><td>Unblock executables by provided UUID</td><td>unblock_executables <br/>Remediation</td></tr>
</tbody></table>

### operation: Get Executables List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Application Management URL</td><td>Specify the server URL for Application Management.
</td></tr><tr><td>Executable UUID</td><td>(Optional) Specify the Executable UUID to get the details from ESET Server.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the page size for pagination purpose. Maximum value can be 2147483647
</td></tr><tr><td>Page Token</td><td>(Optional) Specify the page token of current page. If not given the first page is returned.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Device Tasks List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL for Automation.
</td></tr><tr><td>Task UUID</td><td>(Optional) Specify the Task UUID to get the details from ESET Server.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the page size for pagination purpose. Maximum value can be 2147483647
</td></tr><tr><td>Page Token</td><td>(Optional) Specify the page token of current page. If not given the first page is returned.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Detections List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident Management URL</td><td>Specify the server URL for Incident Management.
</td></tr><tr><td>Detection UUID</td><td>(Optional) Specify the Detection UUID to get the details from ESET Server.
</td></tr><tr><td>Device UUID</td><td>(Optional) Specify the Device UUID to get detections those are linked with the provided device.
</td></tr><tr><td>Start Time</td><td>(Optional) Specify the start time for include only incidents whose detections occurred after start time.
</td></tr><tr><td>End Time</td><td>(Optional) Specify the end time for include only incidents whose detections occurred before end time.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the page size for pagination purpose. Maximum value can be 2147483647
</td></tr><tr><td>Page Token</td><td>(Optional) Specify the page token of current page. If not given the first page is returned.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Detection Groups List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Incident Management URL</td><td>Specify the server URL for Incident Management.
</td></tr><tr><td>Detection Group UUID</td><td>(Optional) Specify the Detection Group UUID to get the details from ESET Server.
</td></tr><tr><td>Device UUID</td><td>(Optional) Specify the Device UUID to get detection groups those are linked with the provided device.
</td></tr><tr><td>Start Time</td><td>(Optional) Specify the start time for include only incidents whose detections occurred after start time.
</td></tr><tr><td>End Time</td><td>(Optional) Specify the end time for include only incidents whose detections occurred before end time.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the page size for pagination purpose. Maximum value can be 2147483647
</td></tr><tr><td>Page Token</td><td>(Optional) Specify the page token of current page. If not given the first page is returned.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Device by UUID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL for Device Management.
</td></tr><tr><td>Device UUID</td><td>Specify the Device UUID to get the details from ESET Server.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Device Groups List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL for Device Management.
</td></tr><tr><td>Group UUID</td><td>(Optional) Specify the Group UUID to get the details from ESET Server.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the page size for pagination purpose. Maximum value can be 2147483647
</td></tr><tr><td>Page Token</td><td>(Optional) Specify the page token of current page. If not given the first page is returned.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Create Device Task
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL for Automation.
</td></tr><tr><td>Task Payload</td><td>Specify the payload for new task.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Isolate Computer From Network
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL for Automation.
</td></tr><tr><td>Device UUID</td><td>Specify the device UUID to isolate from network.
</td></tr><tr><td>Device Group UUID</td><td>Specify the device group UUID to isolate from network.
</td></tr><tr><td>Task Expire Time in minutes</td><td>Specify the minutes so that this task will get expired after that.
</td></tr><tr><td>Task Display Name</td><td>(Optional) Specify the the name for new created task.
</td></tr><tr><td>Task Description</td><td>(Optional) Specify the the description for new created task.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: End Computer Isolation From Network
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL for Automation.
</td></tr><tr><td>Device UUID</td><td>Specify the device UUID to end isolation from network.
</td></tr><tr><td>Device Group UUID</td><td>Specify the device group UUID to end isolation from network.
</td></tr><tr><td>Task Expire Time in minutes</td><td>Specify the minutes so that this task will get expired after that.
</td></tr><tr><td>Task Display Name</td><td>(Optional) Specify the the name for new created task.
</td></tr><tr><td>Task Description</td><td>(Optional) Specify the the description for new created task.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Block Executables
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Application Management URL</td><td>Specify the server URL for Application Management.
</td></tr><tr><td>Executable UUID</td><td>(Optional) Specify the Executable UUID for the blocked executables.
</td></tr><tr><td>Request Body</td><td>(Optional) Specify the request body for the block executables.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Unblock Executables
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Application Management URL</td><td>Specify the server URL for Application Management.
</td></tr><tr><td>Executable UUID</td><td>(Optional) Specify the Executable UUID for the unblock executables.
</td></tr><tr><td>Request Body</td><td>(Optional) Specify the request body for the unblock executables.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - eset-protect-enterprise - 1.0.0` playbook collection comes bundled with the ESET Protect Enterprise connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the ESET Protect Enterprise connector.

- Block Executables
- Create Device Task
- End Computer Isolation From Network
- Get Detection Groups
- Get Detections
- Get Device
- Get Device Groups
- Get Device Tasks
- Get Executables
- Isolate Computer From Network
- Unblock Executables

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
