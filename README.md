# Select JCMA Projects

This tool will iterate a list of project and "Manually" input them on JCMA. (kinda funny to watch)

Requirements
```commandline
Python 3.7+
```

Getting Started
#### First - Configure your config.json file
```
cd <path/to/repo>
pip install -r requirements.txt
python main.py
```

**Libraries**
```commandline
MouseInfo==0.1.3
PyAutoGUI==0.9.53
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyperclip==1.8.2
PyRect==0.2.0
PyScreeze==0.1.28
pytweening==1.0.4
```

**How to use this tool**

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

**demo**
![demo gif](https://github.com/ngeorgj-cprime/select-jcma-projects/blob/main/demo/demo.gif)

*OBS.: If you are using MacOS, you will probably need to allow Python or your IDE to control your keyboard.*

Have a good migration!

Rgds,<br>
**Nivaldo Georg Junior** <br>
Technical Atlassian Engineer on Migrations (CPrime)