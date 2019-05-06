#!/bin/env python
# Imports
import os
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
            print("could not open file" + file_name)

        else:
            lines = file.read()
            try:
                lines.encode('ascii')
            except UnicodeEncodeError:
                global running
                print(" in except" + running)
                running = False
                print(running)
            else:
                global running
                print("in else" + running)

        finally:
            if file:
                file.close()


print("*** [+] Opening Files in Current Directory [+] ***")

current_dir = os.getcwd()
files = []

for file_name in os.listdir(current_dir):
    files.append(current_dir + '/' + file_name)
    print(current_dir + '/' + file_name)



print("*** [+] Starting Monitoring Threads [+] ***")

threads = []

for file_mame in files:
    threads.append(FileMonitor(file_name))

if threads:
    threads[0].start()
    threads[0].join()
else:
    print("no threads")
# while running:
#     try:
#         for thread in threads:
#             thread.start();
#
#     except KeyboardInterrupt:
#         running = False
#         print("*** [!] Stopped By User [!] ***")
#         print("*** [!] Waiting for Threads To Finish [!] ***")
#
#
#     finally:
#         for thread in threads:
#             thread.join();

print("*** [+]  [+] ***")
print("*** [+]  [+] ***")