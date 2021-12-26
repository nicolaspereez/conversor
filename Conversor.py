def conversor(tipo_peso, valor_dolar):
    pesos = input('¿Cuantos pesos' + tipo_peso + 'tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + '  dolares')

menu = '''
Bienvenidos al conversor de monedas 💰
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige un opcion: '''

opcion = int(input(menu))


if opcion == 1:
    conversor(' Colombianos ', 3875)
elif opcion == 2:
    conversor(' Argentinos ', 200)
elif opcion == 3:
   conversor(' Mexicano ', 20)
else:
    print('Ingrese una opcion correcta por favor')


