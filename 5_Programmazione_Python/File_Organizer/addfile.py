import argparse
import sys
import os.path
import shutil
import csv
from binfiles import categorize

def get_metadata(filename, file_list, directory):
    tmp = filename.split('.') #rimosso il ciclo for perché ora c'è un solo file
    size = os.path.getsize(directory+'/'+filename) 
    sys.stdout.write('File coinvolto:\n') #rimosso il metodo os.listdir perché ora il file viene esplicitato dall'utente
    file_list.extend([tmp[0], tmp[1], size]) 
    type = categorize(tmp[1])
    sys.stdout.write(f'Name: {tmp[0]}, Type: {type}, Size: {size} Bytes\n') 

def create_recap(directory, file_list): 
    with open(directory+'/recap.csv', 'w', newline='') as recap:
        writer = csv.writer(recap)
        writer.writerow(['name', 'type', 'size']) 
        type = categorize(file_list[1]) 
        writer.writerow([file_list[0], type, file_list[2]]) #rimosso il ciclo for perché la lista file_list include un solo file

def update_recap(directory, file_list):
    with open(directory+'/recap.csv', 'a', newline='') as recap:
        writer = csv.writer(recap)
        type = categorize(file_list[1]) #rimosso il ciclo for perché la lista file_list include un solo file
        writer.writerow([file_list[0], type, file_list[2]])

def move(directory, file_list):
    type = categorize(file_list[1]) #rimosso il ciclo for perché la lista file_list include un solo file
    starting_path = f'{directory}/{file_list[0]}.{file_list[1]}' 
    destination_path = f'{directory}/File {type.capitalize()}' 
    if os.path.isdir(destination_path):
        pass
    else:
        os.mkdir(destination_path) 
    shutil.move(starting_path, destination_path) 

def main(directory): 
    file_list = []
    get_metadata(directory, file_list)
    if os.path.isfile(directory+'/recap.csv'): 
        update_recap(directory, file_list)
    else:
        create_recap(directory, file_list)
    move(directory, file_list)

def main(directory):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=str, help='Inserisci il nome del file che vuoi spostare, compreso della sua estensione')
        args = parser.parse_args()
        file_list = []
        get_metadata(args.filename, file_list, directory)
        if os.path.isfile(directory+'/recap.csv'):
            update_recap(directory, file_list)
        else:
            create_recap(directory, file_list)
        move(directory, file_list)  
        sys.stdout.write('Operazione Completata')
    except FileNotFoundError:
        sys.stdout.write(f'ERRORE: Il file digitato non esiste nella directory {directory}')

if __name__ == '__main__': 
    main('files')