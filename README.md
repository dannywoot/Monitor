# Monitor
This script monitors a specified text document for any changes

## Features

This script monitors a specified text document for any changes. When a change is detected, the script records the new text added to the document along with the time of the modification, and appends this information to a report file. The script also displays a notification on Windows with the same information.

The script uses real-time monitoring, meaning that it detects changes as soon as they are saved to the document, rather than checking for changes at fixed intervals.

The document to monitor, the report file location, and the checking interval can all be specified by the user when running the script.

This tool can be useful for keeping track of updates to a document, especially in situations where multiple people are editing the document or where changes are being made over a long period of time.

## Requirements

This script requires Python and several libraries, including os, time, difflib, win10toast, datetime, watchdog, and argparse. Most of these libraries are built into Python, but you might need to install win10toast and watchdog using pip:

```
pip install win10toast watchdog
```

## Install

Save the script to a file on your computer. For example, you might save it as document_monitor.py in your Documents directory.

Step 3: Identify the Document to Monitor

Decide which document you want the script to monitor. You'll need to know the full path to this document.

Step 4: Decide Where to Save the Report

Choose a location to save the report that the script will generate. You'll need to know the full path to this location. Note that the script will append to this report each time it detects a change, so if you want to start fresh, you'll need to delete or rename the old report.

## Run the script

Open a command prompt and navigate to the directory where you saved the script. Then, run the script with your desired options. For example:

bash
Copy code
```
python document_monitor.py --document_path "C:\path\to\your\document.txt" --interval 10 --report_path "C:\path\to\your\report.txt"
```

Replace "C:\path\to\your\document.txt" with the path to the document you want to monitor, and "C:\path\to\your\report.txt" with the path to your report file.

The --interval option controls how often (in seconds) the script checks for changes. You can adjust this to suit your needs.

## Monitor for changes

Once the script is running, it will monitor the specified document for changes. Each time it detects a change, it will append a record to the report file and display a Windows notification.

To stop the script, press Ctrl+C in the command prompt.

Remember that this script will only detect changes that are saved to the document while the script is running. If you want to monitor changes over a longer period of time, you'll need to keep the script running.
