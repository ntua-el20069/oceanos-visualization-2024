
import random

def readline(filepath: str, fieldnames, separator = ','):
    with open(f'{filepath}', 'r', encoding='utf-8') as csvFile:
        #last_line = csvFile.read().split('\n')[random.randint(1,100)]
        last_line = csvFile.read().split('\n')[-2]
        print(last_line)
        data_dict = {label : str(x) for label, x in zip(fieldnames, last_line.split(separator))}        
        return data_dict