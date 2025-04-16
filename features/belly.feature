# language: es

Característica: Comportamiento del Estómago

	@spanish
	Escenario: Comer muchos pepinos y gruñir
		Dado que he comido 42 pepinos
		Cuando espero 2 horas
		Entonces mi estómago debería gruñir

	@spanish
	Escenario: Comer pocos pepinos y no gruñir
		Dado que he comido 10 pepinos
		Cuando espero 2 horas
		Entonces mi estómago no debería gruñir

	@spanish
	Escenario: Comer muchos pepinos y esperar menos de una hora
		Dado que he comido 50 pepinos
		Cuando espero media hora
		Entonces mi estómago no debería gruñir

	@spanish
	Escenario: Comer pepinos y esperar en minutos
		Dado que he comido 30 pepinos
		Cuando espero 90 minutos
		Entonces mi estómago debería gruñir

	@spanish
	Escenario: Comer pepinos y esperar en diferentes formatos
		Dado que he comido 25 pepinos
		Cuando espero "dos horas, treinta minutos y treinta segundos"
		Entonces mi estómago debería gruñir
		
	@spanish
	Escenario: Comer pepinos fraccionarios suficientes para gruñir
		Dado que he comido 10.5 pepinos
		Cuando espero 2 horas
		Entonces mi estómago debería gruñir

	@english
	Escenario: Error al comer pepinos negativos
		Dado que intento comer -1 pepinos
		Entonces debería ver un error
	
	@english	
	Escenario: Esperar usando horas en inglés
		Dado que he comido 20 pepinos
		Cuando espero "two hours and thirty minutes"
		Entonces mi estómago debería gruñir
