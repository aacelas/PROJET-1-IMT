#!/usr/bin/env python3

from options_parser import create_parser
from commands import *

parser = create_parser()
options = parser.parse_args()

# Exécution de la commande
if options.command == 'add':
    commands.add(options.file, options.details)
elif options.command == 'modify':
    commands.modify(options.file, options.id, options.details)
elif options.command == 'rm':
    commands.rm(options.file, options.id)
elif options.command == 'show':
    commands.show(options.file) 
