# PUBG API Wrapper for Pandas
This package is under development; thus, some features may not work correctly or exist.
<br/>

## Installation
You can install this module using pip (pip3)
```bash
pip install pubgapi-ku
```
<br/>

## Components
### Modules
#### 1. API Connector
The module contains **Connector** class which has functions to get raw JSON data using *PUBG API* provided by *PUBG Developer Portal* (https://developer.pubg.com/).
All data which can be collected using this module can also be collected by the **DataWrapper** class, which provides data as *Pandas DataFrame* type using **Connector** class internally.
Therefore, there is no need to necessarily use **API Connector** module and **Connector** class in most cases.

##### Usage
To use **Connector** class, you must generate a *PUBG API key*. Refer instruction of *PUBG Developer Portal* (https://documentation.pubg.com/en/getting-started.html)
```Python
from pubgapiku import api_connector

conn = Connector(<your_api_key>)
sample_matches = conn.sample_matches()
```
##### Functions
- **sample_matches(self) -> dict|None**
Return a dictionary(dict)-type containing a list of sample matches within 24 hours in UTC
When the API request was not successful (the response code was not 200), the function returns *None*
<br/>

- **players(self, \*\*kargs) -> dict|None**
Return a dictionary-type value containing players information
When the API request was not successful (the response code was not 200), the function returns *None*
    - Keyword arguments
        - **ids:list[str]** &nbsp; Filters by player IDs
        - **names:list[str]** &nbsp; Filters by player names
<br/>

- **match(self, match_id:str) -> dict|None**
Return a dictionary-type value containing a match's information
When the API request was not successful (the response code was not 200), the function returns *None*
    - Argument
        - **match_id:str** &nbsp; The ID of the match for which you want to collect information
<br/>

- **telemetry_addr(self, match_data:dict) -> str|None**
Return the address of telemetry data of a match from the match's data
When the address of telemetry data was not found, the function return *None*
    - Argument
        - **match_data:dict** &nbsp; A match data which is obtained from *match* function
<br/>

- **get_telemetry(self, addr:str) -> dict|None**
Return a dictionary-type value containing a match's telemetry data of the target match
When the request was not successful (the response code was not 200), the function returns *None*
    - Argument
        - **addr:str** &nbsp; The address of the target telemetry data obtained from *telemetry_addr* function
<br/>

#### 2. Data Wrapper
The module contains **DataWrapper** class, which has functions to get PUBG data from *PUBG API* as *Pandas DataFrame* data type
Since **DataWrapper** class works based on **Collector** class, a PUBG API key is also needed to use **DataWrapper** class

##### Usage
##### Functions