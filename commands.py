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

def find_first_missing_id(file):
    """Return the first missing id in the file, or 1 if the file is empty."""
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            valid_lines = [l.strip() for l in lines if l.strip() != '']
            if len(valid_lines) == 0:
                return 1
            for i in range(len(valid_lines)-1):
                current_line = valid_lines[i]
                next_line = valid_lines[i+1]
                current_id = int(current_line.split(' | ')[0])
                next_id = int(next_line.split(' | ')[0])
                if next_id != current_id + 1:
                    return current_id + 1
            return int(valid_lines[-1].split(' | ')[0]) + 1
    except FileNotFoundError:
        print(f"The file {file} was not found")


def add(file, details): 
    """Add a new task with the given details to the file."""
    try:
        with open(file, 'r') as f:
            id = find_first_missing_id(file)
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
