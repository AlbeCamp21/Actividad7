class Belly:
	def __init__(self, clock_service=None):
		self.pepinos_comidos = 0
		self.tiempo_esperado = 0
		self.limite=10
		self.registro_tiempos = []
		self.clock_service = clock_service

	def comer(self, pepinos):
		if pepinos < 0:
			raise ValueError("No se puede comer menos de 0 pepinos")
		if pepinos > 100 and pepinos < 1000:
			raise ValueError("No se pueden comer mas de 100 pepinos")
		self.pepinos_comidos += pepinos
		if self.clock_service:
			self.registro_tiempos.append(self.clock_service())

	def esperar(self, tiempo_en_horas):
		self.tiempo_esperado += tiempo_en_horas

	def esta_gruñendo(self):
		# El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
		return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10
		
	def pepinos_restantes_grunir(self):
		falta = self.limite-self.pepinos_comidos
		return falta
