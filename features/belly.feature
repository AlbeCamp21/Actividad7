# language: es

Característica: Comportamiento del Estómago

	@spanish
	Escenario: Comer muchos pepinos y gruñir
		Dado que he comido 42 pepinos
		Cuando espero 2 horas
		Entonces mi estómago debería gruñir

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
		
	@spanish
	Escenario: Comer pepinos y esperar un tiempo aleatorio
		Dado que he comido 25 pepinos
		Cuando espero un tiempo aleatorio entre 3 y 4 horas
		Entonces mi estómago debería gruñir
		
	@spanish
	Escenario: Manejar una cantidad negativa de pepinos
		Dado que intento comer -5 pepinos
		Entonces debería ocurrir un error de cantidad negativa.

	@spanish
	Escenario: Manejar una cantidad excesiva de pepinos
		Dado que intento comer 150 pepinos
		Entonces debería ocurrir un error de cantidad excesiva.
	
	@spanish	
	Escenario: Comer 1000 pepinos y esperar 10 horas
		Dado que he comido 1000 pepinos
		Cuando espero 10 horas
		Entonces mi estómago debería gruñir

	@spanish
	Escenario: Manejar otros tiempos
		Dado que he comido 50 pepinos
		Cuando espero "1 hora, 30 minutos y 45 segundos"
		Entonces mi estómago debería gruñir
		
	@spanish
	Escenario: Comer más de 10 pepinos y esperar 2 horas (test_trivia)
		Dado que he comido 15 pepinos
		Cuando espero 2 horas
		Entonces mi estómago debería gruñir
			
	@spanish
	Escenario: Saber cuántos pepinos he comido
		Dado que he comido 15 pepinos
		Entonces debería haber comido 15 pepinos
	
	
		


	@english	
	Escenario: Esperar usando horas en inglés
		Dado que he comido 20 pepinos
		Cuando espero "two hours and thirty minutes"
		Entonces mi estómago debería gruñir
		



	@issue1
	Escenario: Comportamiento del estómago luego de comer pepinos
		Dado que he comido 20 pepinos
		Cuando espero 3 horas
		Entonces mi estómago debería gruñir
		
	@issue2	
	Escenario: Predecir si estómago gruñirá luego de comer y esperar
		Dado que he comido 12 pepinos
		Cuando espero 90 minutos
		Entonces mi estómago debería gruñir
					
		



	@criterio_nuevo
	Escenario: Saber cuántos pepinos puedo comer antes de gruñir
		Dado que he comido 8 pepinos
		Cuando pregunto cuántos pepinos más puedo comer
		Entonces debería decirme que puedo comer 2 pepinos más

	@criterio_nuevo
	Escenario: Ya he alcanzado el límite de pepinos
		Dado que he comido 10 pepinos
		Cuando pregunto cuántos pepinos más puedo comer
		Entonces debería decirme que no puedo comer más pepinos

	@criterio_nuevo
	Escenario: He comido más pepinos del límite
		Dado que he comido 12 pepinos
		Cuando pregunto cuántos pepinos más puedo comer
		Entonces debería decirme que ya he comido demasiado
		
		
		
	
	@simulando_reloj
	Escenario: Registrar hora al comer pepinos
		Dado que he comido 3 pepinos
		Entonces se debe haber registrado la hora





