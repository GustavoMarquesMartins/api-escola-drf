from django.core.management.utils import get_random_secret_key

# Gera uma chave secreta aleatória de forma segura 
# Como usar:
# Primeiro, dentro do diretório 'scripts', utilize o comando 'python secret_key_generator.py' e copie o resultado.
# Em seguida, adicione o resultado à sua variável de ambiente 'SECRET_KEY'.
print(get_random_secret_key())
