#!/usr/bin python3.6
#-*-coding: utf-8-*-

from paquet_loop2 import paquet_loop2
from paquet_loop import paquet_loop

class Trame:

    def __init__(self):
        self.m_trame = "4c4f4f1401ff7f0375d40225c20105ff57013c00580010005101ff7fff7f2000ff3dff2c002900ff000000ffff7f0c0092240c000000000000000c00020000ffff037503750375ff06050e120a02151a030101ff7fff7fff7fff7fff7fff7f0a0d5ea0"
        self.m_size_type_paquet = 5
        self.list_trame = {}
        type = self.get_type_packet()
        if type == "LOOP":
            paquet_loop()
        elif type == "LOOP2":
            paquet_loop2()

        self.add_list()
        print(self.list_trame[4])
        print(len(self.list_trame))
        print(self.get_type_packet())

    def add_list(self):
        nb_tour = 0;
        etape = 0
        for case in self.m_trame:
            if etape % 2:
                self.list_trame[nb_tour] += case
                nb_tour += 1
                etape = 0
            else:
                if nb_tour == 0:
                    self.list_trame[nb_tour] = case
                else:
                    self.list_trame[nb_tour] = case
                etape += 1

    def get_type_packet(self):
        if self.m_trame[4] == "0" and self.m_trame[5] == "0":
            return "LOOP"
        elif self.m_trame[4] == "0" and self.m_trame[5] == "1":
            return "LOOP2"
        else:
            return "Erreur"

if __name__ == "__main__":
    Trame()