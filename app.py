"""
Program Simulator Putar Dadu
"""
import random

def putar():
    angka = random.randint(1,6)

    return angka

xKali = int(input('Mau putar berapa kali? '))
dadu = list()
main = 1

print('Putar dadu sebanyak {} kali'.format(xKali))
while main <= xKali:
    angkaDadu = putar()
    print('Permainan ke {}'.format(main))
    print('Angka Dadu yang keluar {}'.format(angkaDadu))

    main+=1
    dadu.append(angkaDadu)

print('\n')
print('Angka Dadu yang keluar secara berurutan : ')
for angka in dadu:
    print(angka, end=' ')