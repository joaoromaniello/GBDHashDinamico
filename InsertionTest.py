import os
import random
import struct

from FileManager import FileManager


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
        registro = {
            'nseq': i,
            'text': generate_random_string(16)
        }
        fm.insert_record(registro, i)


test_file_manager()