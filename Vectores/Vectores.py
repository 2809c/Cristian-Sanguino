lista_vacia = []

lista = ['computador', 'mesa', 'moto', 'carro', 'silla']
longitud = len(lista)
print(f'la longitud es de la lista es: {longitud}')

primer_elemento = lista[0]
elemnto_central = lista[len(lista) // 2]
ultimo_elemnto = lista[-1]
print(f'primer elemento: {primer_elemento}, elemnto central: {elemnto_central}, utimo elemnto: {ultimo_elemnto}')

tipos_datos_mezclados = ['Cristian', '20', '1.84', 'soltero', 'san pacho']

it_companies = ['facebook', 'google', 'microsoft', 'apple', 'ibm', 'oracle', 'amazon']
it_companies.append('twitter')

empresa = 'google'
if empresa in it_companies:
    print(f'{empresa} esta en la lista')
else:
    print(f'{empresa} no esta en la lista')
    
it_companies.sort()
print(f'lista ordenada: {it_companies}')

it_companies.reverse()
print(f'lista en orden decente: {it_companies}')

it_companies.pop(0)
print(f'lista despues de eliminar la empresa: {it_companies}')

it_companies.clear()
print(f'lista despues de eliminar todas las empresas: {it_companies}')