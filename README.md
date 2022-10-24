# Select JCMA Projects

How to use this tool

1. Open the file config.json and set the configuration variables.
```json
  "cloud_destination_url": "https://instancename.atlassian.net",
  "projects_filename": "project_keys.txt",
  "seconds_to_start": 5
```
2. Create (or edit the project_keys.txt) a txt file and include the project keys, one per line.
```
ABC
AAC
ADA
```
3. Go to the migration page (on JCMA), execute the code and **click on the migration page (to set focus)** This should happen during the time configured in "seconds_to_start".
4. Wait for the execution.