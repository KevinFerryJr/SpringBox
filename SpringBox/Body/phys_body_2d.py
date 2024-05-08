from Numberful.vector import Vec2
from SpringBox.Time.clock import Clock

class PhysBody2D():
	def __init__(self):
		self._position = Vec2(0,0)
		self._velocity = Vec2(0,0)
		self._gravity = -9.81
		self._mass = 0
		self._linear_drag = 0
		self._angular_drag = 0

	@property
	def position(self) -> Vec2:
		return self._position

	@position.setter
	def position(self, value: tuple[float, float]):
		self._position.value = value

	def update(self, delta_time):
		acceleration = Vec2(0, self._gravity * delta_time)
		self._velocity += acceleration
		
		displacement = self._velocity * delta_time + acceleration * 0.5 * (delta_time**2)
		displacement *= 50
		self._position += displacement