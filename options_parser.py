import argparse

def create_parser():
  #Initial parser / file.txt ... 
  parser = argparse.ArgumentParser(description="THE PARSER")
  parser.add_argument("file",type=str, help="The file to process")
  
  subparsers = parser.add_subparsers(dest="command", required=True, help="Sub-command help")
  
  #ADD SUBPARSER / file.txt add details
  parser_add = subparsers.add_parser("add", help="Add a new task")
  parser_add.add_argument("details", nargs='+', default='No details', help="Details of the task to add")
  
  #MODIFY SUBPARSER / file.txt modify id details
  parser_modify = subparsers.add_parser("modify", help="Modify an existing task")
  parser_modify.add_argument("id", type=int, help="The id of the task to modify")
  parser_modify.add_argument("details", nargs='+', default='No details', help="New details of the task")
  
  #RM SUBPARSER / file.txt rm id
  parser_rm = subparsers.add_parser("rm", help="Remove an existing task")
  parser_rm.add_argument("id", type=int, help="The id of the task to remove")
  
  #SHOW SUBPARSER / file.txt show
  parser_show = subparsers.add_parser("show", help="Show all tasks")

  return parser
