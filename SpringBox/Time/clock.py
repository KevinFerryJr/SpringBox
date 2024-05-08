import time

class Clock:
	def __init__(self):
		self._prev_time = time.time()
		self._delta_time = 0.0

	@property
	def delta_time(self) -> float:
		return self._delta_time

	@property
	def acc_time(self) -> float:
		return self._acc_time

	def tick(self) -> float:
		"""
		Called every time the application is updated to maintain an accurate 'delta_time' value between frames.
		Returns:  
		float: The accumulated time since this function was last called (Delta Time). 
		"""
		current_time = time.time()
		delta_time = current_time - self._prev_time
		self._prev_time = current_time
		self._delta_time = delta_time
		return delta_time