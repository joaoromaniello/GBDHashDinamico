import os
import random
import struct

from FileManager import FileManager
from hashAlt3Text import TabelaHash


def generate_random_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    result = ''

    for i in range(length):
        result += random.choice(characters)

    return result


def test_file_manager():
    main_file = 'main.bin'
    index_file = 'index.bin'
    open("dataFiles/"+main_file, 'w').close()
    open("dataFiles/"+index_file, 'w').close()

    fm = FileManager(main_file, index_file)

    for i in range(6000):
        registro = f"{format(i, '04d')} {generate_random_string(16)} " '\n'" "
        fm.insert_record(registro, i)


def createIndexes():
        tabela_hash = TabelaHash()
        f = open("dataFiles/main.bin", "r")
        Lines = f.readlines()

        try:
            for line in Lines:
                parts = line.split(" ")
                nseq = parts[1]
                text = parts[2]
                tabela_hash.inserir(nseq, text)

        except:
            print("FIM DE ARQUIVO")

        tabela_hash.imprimir()
        tabela_hash.criarIndices()




createIndexes()

#test_file_manager()