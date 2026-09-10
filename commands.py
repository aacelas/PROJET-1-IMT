def create_file(file):
    """Create a new file if it does not exist."""
    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        with open(file, 'w') as f:
            pass

def is_valid_label(label):
    """Check if the label is valid."""
    if isinstance(label, list):
        for l in label:
            if l not in ["shopping", "sport", "homework", "administrative", "meetings"]:
                return False
    else:
        if label not in ["shopping", "sport", "homework", "administrative", "meetings"]:
            return False
    return True

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

def add(file, details, label): 
    """Add a new task with the given details to the file."""
    try:
        if not is_valid_label(label):
            raise ValueError(f"Invalid label: {label}. Valid labels are: shopping, sport, homework, administrative, meetings")
        with open(file, 'r') as f:  
            id = find_first_missing_id(file)[0]
            lines = f.readlines()
            missing_id = find_first_missing_id(file)[1]
            lines.insert(missing_id+1, f'{id}' + ' | ' + ' '.join(details) + ' | ' + ' '.join(label) + '\n')
        with open(file, 'w') as f:
            f.writelines(lines)
            print(f"Task added with id: {id}")
    except FileNotFoundError:
        print(f"The file {file} was not found")

def modify(file, id, details, label=None):
    """Modify the task with the given id in the file with the new details."""
    modify_id = find_line_by_id(file, id)
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        if modify_id != -1:
            #if the id was found
            # we modify the line with the new details
            if label is not None:
                if not is_valid_label(label):
                    raise ValueError(f"Invalid label: {label}. Valid labels are: shopping, sport, homework, administrative, meetings")
                lines[modify_id] = f'{id}' + ' | ' + ' '.join(details) + ' | ' + ' '.join(label) + '\n'
            else:
                lines[modify_id] = f'{id}' + ' | ' + ' '.join(details) + ' | ' + lines[modify_id].split(' | ')[2] + '\n'
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
            print("+----+----------------+----------+")
            print("| id | description    | label    |")
            print("+----+----------------+----------+")
            for line in lines:
                if line.strip() != '':
                    print(f"| {line.strip().split(' | ')[0]:<2} | {line.strip().split(' | ')[1][:14]:<14} | {line.strip().split(' | ')[2][:8]:<8} |")
                    if len(line.strip().split(' | ')[1]) > 14:
                        for i in range(14, len(line.strip().split(' | ')[1]), 14):
                            print(f"|    | {line.strip().split(' | ')[1][i:i+14]:<14} |      |")
                    print("+----+----------------+----------+")
    except FileNotFoundError:
        print(f"The file {file} was not found")
