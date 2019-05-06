#!/bin/env python
# Imports
import glob
import threading

print("*** [+] Starting Encryption Detector [+] ***")
print("*** [+] [Ctrl + C] To Stop [+] ***")

running = True

print("*** [+] Defining Monitor Threads [+] ***")


class FileMonitor(threading.Thread):
    def __init__(self, file_path):
        threading.Thread.__init__(self)
        self.file_name = file_path

    def run(self):
        try:
            file = open(self.file_name)

        except:
            print("could not open file" + file)

        else:
            lines = file.read()
            try:
                lines.encode('ascii')
            except UnicodeDecodeError:
                global running
                print("*** [!] Encryption Detected In File: {} [!] ***".format(self.file_name))
                running = False

        finally:
            if file:
                file.close()
                del lines


print("*** [+] Opening Files in Current Directory [+] ***")


def init_file_list():
    files = []

    for filename in glob.glob("*.txt"):
        files.append(filename)

    return files


files = init_file_list()

if not files:
    print("*** [!] No Files Found In Folder [!] ***")
    print("*** [!] Exiting [!] ***")
    exit(1)

print("*** [+] Starting Monitoring Threads [+] ***")


def init_thread_list(files):
    threads = []

    for file_name in files:
        threads.append(FileMonitor(file_name))

    return threads


threads = init_thread_list(files)

if threads:
    while running:
        try:
            for thread in threads:
                thread.start()

            for thread in threads:
                    thread.join()

        except KeyboardInterrupt:
            running = False
            print("*** [!] Stopped By User [!] ***")
            print("*** [!] Waiting for Threads To Finish [!] ***")

        else:
            # in case files have been added or removed from folder
            files = init_file_list()
            # required
            threads = init_thread_list(files)

else:
    print("no threads")

print("*** [!] Exiting [!] ***")
