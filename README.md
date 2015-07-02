Plugins for nagios
============



```bash
git clone https://bitbucket.org/shinespb/nagios_plugins.git
```

## What does it do?

check_patterns_count counts files in directories with a structure like: 
/<base_path>/<year>/<month>/<day>/<hour>/<minute>
and returns warning/critical/ok

```
check_patterns_count gets an arguments:
	-t <minutes>  - Gets all directories for now to <minutes> ago. DEFAULT: 5 mins.
	-c <int>	- File count for CRITICAL message. DEFAULT: 50
	-w <int>	- File count for WARNING message DEFAULT: 100
	-d <path>	- Base path where program will find structure like “<year>/<month>/<day>/<hour>/<minute>”. DEFAULT: /events_storage/phishing_detected/
```
