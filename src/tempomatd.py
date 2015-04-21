#!/usr/bin/env python

import time
from daemon import runner
from tempomat import Tempomat

class TempOMatDaemon():
    
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = 'test.log'
        self.stderr_path = 'test2.log'
        self.pidfile_path =  '/var/run/tempomat.pid'
        self.pidfile_timeout = 5
        
    def run(self):
        mat = Tempomat()
        mat.runContinuous()

app = TempOMatDaemon()
daemon_runner = runner.DaemonRunner(app)
#This ensures that the logger file handle does not get closed during daemonization
# daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()
