import time


class Clock:
	def __init__(self):
		self._prev_time = time.time()

	def tick(self) -> float:
		"""
  		Called every time the application is updated to maintain an accurate 'delta_time' value between frames.
     	Returns:  
		float: The accumulated time since the function was last called (Delta Time). 
     	"""
		current_time = time.time()
		delta_time = current_time - self._prev_time
		self._prev_time = current_time
		return delta_time