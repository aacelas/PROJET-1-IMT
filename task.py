#!/usr/bin/env python3
from options_parser import create_parser
import commands
parser = create_parser()
options = parser.parse_args()
print(options)

# Exécution de la commande
try:
    commands.create_file(options.file)
    if options.command == 'add':
        id = commands.add(options.file, options.details)
        print(f"Task added with id: {id}")
    elif options.command == 'modify':
        commands.modify(options.file, options.id, options.details)
    elif options.command == 'rm':
        commands.rm(options.file, options.id)
    elif options.command == 'show':
        commands.show(options.file)
except Exception as e:
    print(f"An error occurred: {e}")
    print(f"command {options.command} failed")
