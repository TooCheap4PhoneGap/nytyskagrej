from random import randint


svenskaord = ['solen skiner','det är varmt','det finns inga moln på himmelen','det är åskväder',
'det är riktigt dåligt väder','det snöar','det är kallt','det är molnigt','det är dimmigt','det är mulet',
'det är vått','det stormar']
tyskaord = ['die Sonne scheint','es ist heiss/warm','es gibt keine Wolke am Himmel','es gibt Gewitter',
'es ist ein richtiges Unwetter','es schneit','es ist kalt','es ist wolkig','es ist neblig','es ist bedeckt',
'es ist nass','es stürmt']

fel = []

def ask(word):
    

    print('Vad är "'+svenskaord[word]+'" på tyska')

    svar = input()

    if svar == tyskaord[word]:
        print('Ajamen det är rätt')
        input()

    else:
        print('Det är tyvärr fel. Rätt svar är "'+tyskaord[word]+'"')
        fel.append(word)
        input()
    

for i in range(15):
    ask(randint(0, len(svenskaord) - 1))

print('vill du prova dom du hade fel på')
print('y or n')

resp = input()

if resp == 'y':
    while len(fel) > 0:
        ask(fel[0])
        fel.pop(0)

else:
    print('king')
