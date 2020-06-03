string = input('Digite algo: ')

print('Informações sobre a string {}:'.format(string))
print('Ela é composta apenas por letras minúsculas?', string.islower())
print('Ela é composta apenas por letras maiúsculas?', string.isupper())
print('Ela é composta apenas por letras?', string.isalpha())
print('Ela é composta apenas por números?', string.isnumeric())
print('Ela é composta apenas por letras ou números?', string.isalnum())
print('Ela é composta apenas caracteres ASCII?', string.isascii())
print('Ela é um decimal?', string.isdecimal())
print('Ela é um dígito?', string.isdigit())
print('Ela é um identificador?', string.isidentifier())
print('Ela é imprimível?', string.isprintable())
print('Ela é um título?', string.istitle())
print('Ela é um espaço?', string.isspace())


