import os
import time
import difflib
import win10toast
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_path, report_path, notification_function):
        self.file_path = file_path
        self.report_path = report_path
        self.notification_function = notification_function
        with open(self.report_path, "r") as f:
            self.old_information = f.read()

    def on_modified(self, event):
        if event.src_path == self.file_path:
            print("Change detected!")
            with open(self.file_path, "r") as f:
                new_information = f.read()

            modification_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Identify new text
            diff = difflib.ndiff(self.old_information.splitlines(), new_information.splitlines())
            new_text = '\n'.join(line[2:] for line in diff if line.startswith('+ '))
            report_content = "\nThe document was modified at " + modification_time + ". The new text added is: \n\n" + new_text

            with open(self.report_path, "a") as f:  # Note the "a" here for "append" mode
                f.write(report_content)

            print("Sending notification...")
            self.notification_function(new_text, modification_time)

            self.old_information = new_information

def send_windows_notification(changes, modification_time):
    title = "Document has been modified"
    message = "The document was modified at " + modification_time + ". The new text added is: \n\n" + str(changes)

    print("Preparing Windows notification...")
    notification = win10toast.ToastNotifier()
    print("Showing Windows notification...")
    notification.show_toast(title, message, duration=10)

def main(document_path, interval, report_path):
    event_handler = FileChangeHandler(document_path, report_path, send_windows_notification)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(document_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(interval)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monitor a document for changes.')
    parser.add_argument('--document_path', type=str, required=True, help='The path of the document to monitor.')
    parser.add_argument('--interval', type=int, default=10, help='The interval (in seconds) at which to check for changes.')
    parser.add_argument('--report_path', type=str, required=True, help='The path of the report file.')

    args = parser.parse_args()

    main(args.document_path, args.interval, args.report_path)
