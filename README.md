# Rainmeter Aquasuite
This application is a hacky but efficient way to connect [Aquasuite](https://aquacomputer.de/software.html) to the [Rainmeter](https://www.rainmeter.net/).\
It should be a Rainmeter custom plugin but I don't have the will and time to explore C# and Plugin SDK.

## Usage
1. In Aquasuite enable `Shared Memory Export` (Data log -> Automatic data exports), set `File name` to `Rainmeter`, add `Data sources` and activate the export.
2. Run `RainmeterAquasuite.exe`. The application runs fully in the background and should be added to Windows autostart.
3. Exported data sources should appear in `HKEY_CURRENT_USER\Software\RainmeterAquasuite` registry key. By default, they are updated every second.
4. Data now can be accessed with a standard Rainmeter [registry measure](https://docs.rainmeter.net/manual/measures/registry/).