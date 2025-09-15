import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

# Exibe a data formatada
print(f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}")

# Exibe a hora formatada
print(f"Hora: {agora.hour:02d}:{agora.minute:02d}")
