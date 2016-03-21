import testinfra
import pytest

def test(SupervisorRunning):
	assert SupervisorRunning("activitydb") == True
