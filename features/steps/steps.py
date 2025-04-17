from behave import given, when, then
import re
from src.belly import Belly
import random
import traceback
import time

# de letars a números
def convertir_palabra_a_numero(palabra):
	try:
		return float(palabra) # Cambiado a float
	except ValueError:
		numeros = {
		# espanol
		"cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4,
		"cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
		"once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
		"dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
		"veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
		"sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90,
		"media": 0.5,
		# ingles
		"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
		"six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
		"twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
		"sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
		"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
		"seventy": 70, "eighty": 80, "ninety": 90, "half": 0.5
		}
	return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes:g} pepinos') # Cambiando a float
def step_given_eaten_cukes(context, cukes):
	context.belly.comer(float(cukes))
'''
@given('que intento comer {cukes:g} pepinos')
def step_given_attempt_negative_pepinos(context, cukes):
	try:
		context.belly.comer(float(cukes))
	except Exception as e:
		context.error = str(e)
'''

@given('que intento comer {cukes:g} pepinos')
def step_given_comer_con_error(context, cukes):
	try:
		context.belly = Belly()
		context.belly.comer(float(cukes))
	except ValueError as e:
		context.exception = e

@when('espero un tiempo aleatorio entre {min_time:g} y {max_time:g} horas')
def step_when_random_wait(context, min_time, max_time):
	random_wait = random.uniform(min_time, max_time)
	print(f"Tiempo aleatorio elegido: {random_wait:.2f} horas") 
	context.belly.esperar(random_wait)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
	time_description = time_description.strip('"').lower()
	# reemplaza 'y' o ',' por espacios
	time_description = re.sub(r'[y,]', ' ', time_description)
	time_description = time_description.strip()

	pattern = re.compile(
		r'(?:(\w+)\s*(?:horas?|hours?))?\s*'
		r'(?:(\w+)\s*(?:minutos?|minutes?))?\s*'
		r'(?:(\w+)\s*(?:segundos?|seconds?))?'
	)

	match = pattern.match(time_description)

	if match:
		hours_word = match.group(1) or "0"
		minutes_word = match.group(2) or "0"
		seconds_word = match.group(3) or "0"

		hours = convertir_palabra_a_numero(hours_word)
		minutes = convertir_palabra_a_numero(minutes_word)
		seconds = convertir_palabra_a_numero(seconds_word)

		total_time_in_hours = hours + (minutes / 60) + (seconds/3600)
	else:
		raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")
	context.belly.esperar(total_time_in_hours)
	
@when('pregunto cuántos pepinos más puedo comer')
def step_when_pregunto_cuantos_faltan(context):
	context.faltan = context.belly.pepinos_restantes_grunir()

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
	assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
	assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
		
@then('debería ver un error')
def step_then_should_see_error(context):
	assert isinstance(context.exception, ValueError), "No se lanzó ValueError"


@then('debería ocurrir un error de cantidad negativa.')
def step_then_error_negativo(context):
	assert isinstance(context.exception, ValueError), "Cantidad negativa no permitida."

@then('debería ocurrir un error de cantidad excesiva.')
def step_then_error_excesivo(context):
	assert isinstance(context.exception, ValueError), "Cantidad excesiva no permitida."
	
@then('debería haber comido {esperados:g} pepinos')
def step_then_pepinos_comidos(context, esperados):
	assert context.belly.pepinos_comidos == esperados, (
		f"Se esperaban {esperados} pepinos, pero se comieron {context.belly.pepinos_comidos}."
	)
	
@then('debería decirme que puedo comer {cantidad:g} pepinos más')
def step_then_deberia_decirme_faltan(context, cantidad):
    assert context.faltan == cantidad, f"Esperado {cantidad}, pero fue {context.faltan}"

@then('debería decirme que no puedo comer más pepinos')
def step_then_no_puede_comer_mas(context):
    assert context.faltan == 0, "Se esperaba que no pudiera comer más pepinos"

@then('debería decirme que ya he comido demasiado')
def step_then_ya_excedido(context):
    assert context.faltan < 0, f"Se esperaba una cantidad negativa, pero fue {context.faltan}"





