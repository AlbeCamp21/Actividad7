from src.clock import convertir_tiempo_a_horas
from src.belly import Belly
import pytest

def test_convertir_horas_simples():
	assert convertir_tiempo_a_horas("2 horas")==2.0

def test_convertir_minutos_simples():
	assert convertir_tiempo_a_horas("90 minutos")== 1.5

def test_convertir_media_hora():
	assert convertir_tiempo_a_horas("media hora")==0.5

def test_convertir_horas_y_minutos():
	assert convertir_tiempo_a_horas("1 hora y 30 minutos")==1.5

def test_convertir_horas_minutos_segundos():
	assert abs(convertir_tiempo_a_horas("2 horas, treinta minutos y treinta segundos")-2.5083) < 0.01 # Para probar si se hacen bien los cambios de unidades

def test_convertir_todo_en_palabras():
	assert abs(convertir_tiempo_a_horas("una hora y quince minutos")-1.25) < 0.01

def test_convertir_solo_segundos():
	assert abs(convertir_tiempo_a_horas("1800 segundos")-0.5) < 0.01

def test_convertir_numeros_con_texto_irregular():
	assert abs(convertir_tiempo_a_horas("dos horas treinta minutos")-2.5) < 0.01

def test_comer_pepinos_fraccionarios():
	b = Belly()
	b.comer(2.75)
	assert b.pepinos_comidos==2.75

def test_comer_pepinos_negativos_lanza_error():
	b = Belly()
	with pytest.raises(ValueError):
		b.comer(-1)
		
def test_grunir_si_comio_pepinos():
	b = Belly()
	b.comer(25)
	b.esperar(2)
	assert b.esta_gruñendo() == True
	
def test_pepinos_restantes():
	belly = Belly()
	belly.comer(15)
	assert belly.pepinos_comidos == 15
	
def test_esta_gruñendo_nada_de_tiempo_nada_de_pepinos():
	b = Belly()
	assert b.esta_gruñendo() is False

def test_esta_gruñendo_espera_suficiente_pero_pepinos_insuficientes():
	b = Belly()
	b.comer(10)
	b.esperar(1.5)
	assert b.esta_gruñendo() is False

def test_esta_gruñendo_gruñe_por_pepinos_y_tiempo():
	b = Belly()
	b.comer(11)
	b.esperar(1.5)
	assert b.esta_gruñendo() is True

def test_esta_gruñendo_mucho_tiempo_pocos_pepinos():
	b = Belly()
	b.comer(5)
	b.esperar(2.0)
	assert b.esta_gruñendo() is False

def test_esta_gruñendo_mucho_tiempo_muchos_pepinos():
	b = Belly()
	b.comer(15)
	b.esperar(2.0)
	assert b.esta_gruñendo() is True
	
def test_estomago_predecir_gruñido():
	belly = Belly()
	belly.comer(12)
	belly.esperar(1.5)
	assert belly.esta_gruñendo() == True

	
	
