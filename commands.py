def find_line_by_id(file, id):
    """Return the index of the line with the given id in the file, or -1 if not found."""
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i] != '' and lines[i].strip().split(' | ')[0] == str(id):
                    return i
        return -1
    except FileNotFoundError:
        print(f"The file {file} was not found")
        return -1


def add(file, details): 
    """Add a new task with the given details to the file."""
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            #On garde les lignes non vides pour déterminer le prochain id
            valid_lines = [l.strip() for l in lines if l.strip() != '']
            if len(valid_lines) == 0:
                id = 1
            else:
                derniere_ligne = lines[-1].strip()
                str_id = derniere_ligne.split(' | ')[0]
                id = int(str_id) + 1
        with open(file, 'a') as f:
            f.write(f'{id}' + ' | ' + ' '.join(details) + '\n')
    except FileNotFoundError:
        print(f"The file {file} was not found")

def modify(file, id, details):
    "TODO"
    None

def rm(file, id):
    "TODO"
    None 

def show(file):
    """Show all tasks in the file."""
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() != '':
                    print(line.strip())
    except FileNotFoundError:
        print(f"The file {file} was not found")
