import datetime
import time
import os

eventos = [
    {"nome": "Ano Novo", "data": datetime.datetime(datetime.datetime.now().year + 1, 1, 1, 0, 0, 0)},
    {"nome": "Meu Aniversário", "data": datetime.datetime(datetime.datetime.now().year, 1, 8, 0, 0, 0)},
    {"nome": "Natal", "data": datetime.datetime(datetime.datetime.now().year, 12, 25, 0, 0, 0)},
    {"nome": "Dia das Mães", "data": datetime.datetime(datetime.datetime.now().year, 5, 14, 0, 0, 0)},
    {"nome": "Dia dos Pais", "data": datetime.datetime(datetime.datetime.now().year, 8, 13, 0, 0, 0)},
    {"nome": "Halloween", "data": datetime.datetime(datetime.datetime.now().year, 10, 31, 0, 0, 0)},
    {"nome": "Feriado de Independência", "data": datetime.datetime(datetime.datetime.now().year, 9, 7, 0, 0, 0)},
    {"nome": "Dia dos Namorados", "data": datetime.datetime(datetime.datetime.now().year, 6, 12, 0, 0, 0)},	
]

def formatar_timedelta(td):
    dias = td.days
    segundos_totais = td.seconds
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = segundos_totais % 60
    return f"{dias}d {horas}h {minutos}m {segundos}s"

def mostrar_contagem_regressiva():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nContagem regressiva para eventos:")
        agora = datetime.datetime.now()
        for evento in eventos:
            tempo_restante = evento["data"] - agora
            if tempo_restante.total_seconds() > 0:
                print(f"{evento['nome']}: {formatar_timedelta(tempo_restante)}")
            else:
                print(f"{evento['nome']}: Evento já ocorreu!")
        time.sleep(1)

if __name__ == "__main__":
    mostrar_contagem_regressiva()