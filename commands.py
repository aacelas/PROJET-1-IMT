def create_file(file):
    """Create a new file if it does not exist."""
    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        with open(file, 'w') as f:
            pass

def create_history_file():
    """Create a new history file if it does not exist."""
    try:
        with open("history.txt", 'r') as f:
            pass
    except FileNotFoundError:
        with open("history.txt", 'w') as f:
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
            if len(valid_lines) == 0 or int(valid_lines[0].split(' | ')[0]) != 1:
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
            lines.insert(missing_id+1, f'{id}' + ' | ' + ' '.join(details) + ' | ' + ','.join(label) + '\n')
        with open(file, 'w') as f:
            f.writelines(lines)
            print(f"Task added with id: {id}")
    except FileNotFoundError:
        print(f"The file {file} was not found")

def modify(file, id, details, label=None):
    create_history_file()
    """Modify the task with the given id in the file with the new details."""
    modify_id = find_line_by_id(file, id)
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            with open("history.txt", 'a') as history_file:
                history_file.write(lines[modify_id].strip() + "  ---> modified" + '\n')
        if modify_id != -1:
            #if the id was found
            # we modify the line with the new details
            if label is not None:
                if not is_valid_label(label):
                    raise ValueError(f"Invalid label: {label}. Valid labels are: shopping, sport, homework, administrative, meetings")
                lines[modify_id] = f'{id}' + ' | ' + ' '.join(details) + ' | ' + ','.join(label) + '\n'
            else:
                lines[modify_id] = f'{id}' + ' | ' + ' '.join(details) + ' | ' + lines[modify_id].split(' | ')[2] + '\n'
            with open(file, 'w') as f:
                f.writelines(lines)
        else:
            print(f"The task with id {id} does not exist")
    except FileNotFoundError:
        print(f"The file {file} was not found")

def rm(file, id):
    create_history_file()
    """Remove the task with the given id from the file."""
    rm_id = find_line_by_id(file, id)
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            with open("history.txt", 'a') as history_file:
                            history_file.write(lines[rm_id].strip() + "  ---> removed" + '\n')
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
    with open(file, 'r') as f:
        lines = f.readlines()
        lines.insert(0, "Id | Desccription | Label")
        line1 = lines[0]
        tallest_chain = [0] * len(line1.split("|"))
        for line in lines:
            for i in range(len(line.split("|"))) :
                if tallest_chain[i] < len(line.split("|")[i].strip()) :
                    tallest_chain[i] = len(line.split("|")[i].strip())
    try:
        with open(file, 'r') as f:
            print(tallest_chain)
            lines = f.readlines()
            lines.insert(0, "Id | Description | Label")
            line1 = lines[0]
            for i in range(len(line1.split("|"))) :
                print("+" + "-" + tallest_chain[i] * "-" + "-", end="")
            print("+")
            for line in lines:
                if line.strip() != '':
                    line = line.split("|")
                    for i in range(len(line)) :
                        print("|" + " " + f"{line[i].strip():<{tallest_chain[i]}}"  + " ", end="")
                    print("|")
                    for i in range(len(line)) :
                        print("+" + "-" + tallest_chain[i] * "-" + "-", end="")
                    print("+")
    except FileNotFoundError:
        print(f"The file {file} was not found")