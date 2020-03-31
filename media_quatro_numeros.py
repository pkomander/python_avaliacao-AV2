count = 4
media = 0
while count > 0:
    nota = float(input('Digite as quatro medias: '))
    media += nota
    count -=1
media = media / 4
print('A media de todas as notas e de: ', media)