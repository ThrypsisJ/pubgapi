# PUBG API Wrapper for Pandas
This package is under development; thus, some features may not work correctly or exist.

## Installation
You can install this module using pip (pip3)
```bash
pip install pubgapi-ku
```

## Modules
### 1. API Connector
The module contains <b>Connector</b> class which has functions to get raw JSON data using <i>PUBG API</i> provided by <i>PUBG Developer Portal</i> (https://developer.pubg.com/).
All data which can be collected using this module can also be collected by the <b>DataWrapper</b> class, which provides data as <i>Pandas DataFrame</i> type using <b>Connector</b> class internally.
Therefore, there is no need to necessarily use <b>API Connector</b> module and <b>Connector</b> class in most cases.

#### Usage
To use <b>Connector</b> class, you must generate a <i>PUBG API key</i>. Refer instruction of <i>PUBG Developer Portal</i> (https://documentation.pubg.com/en/getting-started.html)
```Python
from pubgapiku.api_connector import Connector

conn = Connector(<your_api_key>, <platform>)
sample_matches:dict = conn.sample_matches()
```
#### Functions
<font size=4>***```__init__(self, api_key:str, platform:PLATFORM, timeout:int=1)```***</font>

Initialize API request sender

<font size=2>

|Argument|Description|
|---|---|
|***api_key:str***|An API key of the PUBG Developer Portal|
|***platform:PLATFORM***|Target platform to collect data (steam, kakao, console, psn, stadia, tournament, xbox)|
|***timeout:int***|Timeout limitation (sec), default=1|

</font>
<br/>

<font size=4>***```sample_matches(self) -> dict```***</font>

Return a dictionary(dict)-type containing a list of sample matches within 24 hours in UTC
When the API request was not successful (the response code was not 200), the function returns <i>None</i>
<br/>

<font size=4>***```players(self, **kargs) -> dict```***</code></font>

Return a dictionary-type value containing players information
When the API request was not successful (the response code was not 200), the function returns <i>None</i>

<font size=2>

|Keyword Argument|Description|
|---|---|
|***ids:list[str]***|Filters by player IDs|
|***names:list[str]***|Filters by player names|

</font>
<br/>

<font size=4>***```match(self, match_id:str) -> dict```***</font>

Return a dictionary-type value containing a match's information
When the API request was not successful (the response code was not 200), the function returns <i>None</i>

<font size=2>

|Argument|Description|
|---|---|
|***match_id:str***|The ID of the match for which you want to collect information|

</font>
<br/>

<font size=4>***```telemetry_addr(self, match_data:dict) -> str```***</font>

Return the address of telemetry data of a match from the match's data
When the address of telemetry data was not found, the function return <i>None</i>

<font size=2>

|Argument|Description|
|---|---|
|***match_data:dict***|A match data which is obtained from ***match*** function|

</font>
<br/>

<font size=4>***```get_telemetry(self, addr:str) -> list```***</font>

Return a dictionary-type value containing a match's telemetry data of the target match
When the request was not successful (the response code was not 200), the function returns <i>None</i>

<font size=2>

|Argument|Description|
|---|---|
|***addr:str***|The address of the target telemetry data obtained from <i>telemetry_addr</i> function|

</font>
<br/>

### 2. Data Wrapper
The module contains <b>DataWrapper</b> class, which has functions to get PUBG data from <i>PUBG API</i> as <i>Pandas DataFrame</i> data type
Since <b>DataWrapper</b> class works based on <b>Collector</b> class, a PUBG API key is also needed to use <b>DataWrapper</b> class

#### Usage
```Python
import pandas as pd
from pubgapiku.data_wrapper import DataWrapper

wrapper = DataWrapper(<your_api_key>)
sample_matches:list = wrapper.get_sample_matches()
players:pd.DataFrame = wrapper.get_players_in_match(sample_matches[0])
```
#### Functions