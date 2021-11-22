import os
import sys
import time
import json

# Platform specific file name and file path.
# PATH is the location of files to be imported / exported.


# Platform specific constants
if sys.platform == 'win32':
    print("recording-test.py, running on windows")
    PIPE_TO_AUDACITY = '\\\\.\\pipe\\ToSrvPipe'
    PIPE_FROM_AUDACITY = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    print("recording-test.py, running on linux or mac")
    PIPE_TO_AUDACITY = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    PIPE_FROM_AUDACITY = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
    EOL = '\n'


print("Write to  \"" + PIPE_TO_AUDACITY +"\"")
if not os.path.exists(PIPE_TO_AUDACITY):
    print(""" ..does not exist.
    Ensure Audacity is running with mod-script-pipe.""")
    sys.exit()

print("Read from \"" + PIPE_FROM_AUDACITY +"\"")
if not os.path.exists(PIPE_FROM_AUDACITY):
    print(""" ..does not exist.
    Ensure Audacity is running with mod-script-pipe.""")
    sys.exit()

print("-- Both pipes exist.  Good.")

TOPIPE = open(PIPE_TO_AUDACITY, 'w')
print("-- File to write to has been opened")
FROMPIPE = open(PIPE_FROM_AUDACITY, 'r')
print("-- File to read from has now been opened too\r\n")


def send_command(command):
    """Send a command to Audacity."""
    TOPIPE.write(command + EOL)
    TOPIPE.flush()


def get_response():
    """Get response from Audacity."""
    line = FROMPIPE.readline()
    result = ""
    while True:
        result += line
        line = FROMPIPE.readline()
        # print(f"Line read: [{line}]")
        if line == '\n':
            return result

def do_command(command):
    """Do the command. Return the response."""
    send_command(command)
    # time.sleep(0.1) # may be required on slow machines
    response = get_response()
    return response


