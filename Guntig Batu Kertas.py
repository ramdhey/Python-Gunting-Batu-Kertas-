from unittest import result

import random


def validasi(hand):
    if hand<0 or hand>2:
        return False
    return True

def print_tangan(hand,nama='tamu'):
    hands = [' Gunting ',' Batu ',' Kertas ']

    print(nama+' memilih '+hands[hand])

def menilai(player, computer):
    if player==computer:
        return' seri '
    elif player==0 and computer==1:
        return' kalah '
    elif player==1 and computer==2:
        return ' kalah '
    elif player==2 and computer==0:
        return ' kalah '
    else:
        return ' menang '

print('=========================================================')
print('Mari Mulai Permainan Gunting , Batu , dan Kertas!')
print('=========================================================')
print(' ')
print(' ')
nama_orang =input('Masukkan Namamu : ')

print('Pilih 0=Gunting , 1= Batu, 2= Kertas')

tangan_orang =int(input('Pilih Nomor 0-2 :'))

if validasi(tangan_orang):
    tangan_computer=random.randint(0,2)

    print_tangan(tangan_orang,nama_orang)
    print_tangan(tangan_computer,' Komputer ')

    result=menilai(tangan_orang,tangan_computer)
    print('Hasil: '+result)
else:
    print('Mohon masukkan nomor yang tersedia (0-2)')

