def create_file(file):
    """Create a new file if it does not exist."""
    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        with open(file, 'w') as f:
            pass

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
                return (1,0)
            for i in range(len(valid_lines)-1):
                current_line = valid_lines[i]
                next_line = valid_lines[i+1]
                current_id = int(current_line.split(' | ')[0])
                next_id = int(next_line.split(' | ')[0])
                if next_id != current_id + 1:
                    return (current_id + 1,i)
            return (int(valid_lines[-1].split(' | ')[0]) + 1,len(lines)-1)
    except FileNotFoundError:
        print(f"The file {file} was not found")

def add(file, details): 
    """Add a new task with the given details to the file."""
    try:
        with open(file, 'r') as f:
            id = find_first_missing_id(file)[0]
            lines = f.readlines()
            missing_id = find_first_missing_id(file)[1]
            lines.insert(missing_id+1, f'{id}' + ' | ' + ' '.join(details) + '\n')
        with open(file, 'w') as f:
            f.writelines(lines)
            return id
    except FileNotFoundError:
        print(f"The file {file} was not found")

def modify(file, id, details):
    """Modify the task with the given id in the file with the new details."""
    modify_id = find_line_by_id(file, id)
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        if modify_id != -1:
            #if the id was found
            # we modify the line with the new details
            lines[modify_id] = f'{id}' + ' | ' + ' '.join(details) + '\n'
            with open(file, 'w') as f:
                f.writelines(lines)
        else:
            print(f"The task with id {id} does not exist")
    except FileNotFoundError:
        print(f"The file {file} was not found")

def rm(file, id):
    """Remove the task with the given id from the file."""
    rm_id = find_line_by_id(file, id)
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        if rm_id != -1:
            #if the id was found 
            # we remove the line by setting it to an empty string 
            # then writing back only the non-empty lines
            lines[rm_id] = ''
            valid_lines = [l for l in lines if l.strip() != '']
            with open(file, 'w') as f:
                f.writelines(valid_lines)
        else:
            print(f"The task with id {id} does not exist")
    except FileNotFoundError:
        print(f"The file {file} was not found")

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
