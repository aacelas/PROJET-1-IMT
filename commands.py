def add(file, details): 
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            if len(lines) == 1:
                id = 1
            else:
                derniere_ligne = lines[-1].strip()
                premier_caractere = derniere_ligne[0]
                id = int(premier_caractere) + 1
        with open(file, 'a') as f:
            f.write(f'{id}' + ' | ' + ' '.join(details) + '\n')
    except FileNotFoundError:
        print(f"The file {file} was not found")

def modify(file, id, details):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        if lines[id] != '' and id < len(lines):
            lines[id] = f'{id}' + ' | ' + ' '.join(details) + '\n'
            with open(file, 'w') as f:
                f.writelines(lines)
        else:
            print(f"The task with id {id} does not exist")
    except FileNotFoundError:
        print(f"The file {file} was not found")

def rm(file, id):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        if lines[id] != '' and id < len(lines):
            lines[id] = ''
            with open(file, 'w') as f:
                f.writelines(lines)
        else:
            print(f"The task with id {id} does not exist")
    except FileNotFoundError:
        print(f"The file {file} was not found")

def show(file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != '':
                    print(line.strip())
    except FileNotFoundError:
        print(f"The file {file} was not found")
