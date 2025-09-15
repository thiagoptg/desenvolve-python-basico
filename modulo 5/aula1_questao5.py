import emoji

# Exibir lista de emojis disponíveis
print("Emojis disponíveis:\n")
print("❤️  - :red_heart:")
print("👍  - :thumbs_up:")
print("🤔  - :thinking_face:")
print("🥳  - :partying_face:")
print()

# Solicitar frase ao usuário
frase = input("Digite uma frase e ela será emojizada:\n")

# Converter os códigos de emoji em emojis reais
frase_emojizada = emoji.emojize(frase, language="alias")

# Exibir resultado
print("\nFrase emojizada:\n")
print(frase_emojizada)
