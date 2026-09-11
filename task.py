#!/usr/bin/env python3
from options_parser import create_parser
import commands
parser = create_parser()
options = parser.parse_args()

# Exécution de la commande
try:
    commands.create_file(options.file)
    if options.command == 'add':
        commands.add(options.file, options.details, options.label)
    elif options.command == 'modify':
        commands.modify(options.file, options.id, options.details, options.label)
    elif options.command == 'rm':
        commands.rm(options.file, options.id)
    elif options.command == 'show':
        commands.show(options.file)
    elif options.command == 'future':
        commands.future(options.file, options.details, options.label, options.future_condition)
except Exception as e:
    print(f"An error occurred: {e}")
    print(f"command {options.command} failed")
