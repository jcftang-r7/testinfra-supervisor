# -*- coding: utf8 -*-

import pytest

@pytest.fixture()
def SupervisorRunning(Command):
    def is_running(arg):
        if Command.run_expect(
                [0], "supervisorctl status %s | grep RUNNING" % arg).rc == 0:
            return True
        else:
            return False
    return is_running
