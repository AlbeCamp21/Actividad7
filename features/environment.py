from src.belly import Belly
from unittest.mock import MagicMock

def before_scenario(context, scenario):
	context.belly = Belly()
	context.exception = None
	fake_clock = MagicMock()
	fake_clock.return_value=99999
	context.belly = Belly(clock_service=fake_clock)
