import argparse

def create_parser():
    #Initial parser / file.txt ... 
    parser = argparse.ArgumentParser(description="THE PARSER")
    parser.add_argument("file",type=str, help="The file to process")
    
    subparsers = parser.add_subparsers(help="Sub-command help", dest="command", required=True, )
    
    #ADD SUBPARSER / file.txt add details
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("details", nargs='+', default='No details', help="Details of the task to add")
    parser_add.add_argument(
    "--label",
    choices=["shopping", "sport", "homework", "administrative", "meetings"], required=True,
    help="Label of the task (shopping, sport, homework, administrative, meetings)"
   )
   
    #MODIFY SUBPARSER / file.txt modify id details
    parser_modify = subparsers.add_parser("modify", help="Modify an existing task")
    parser_modify.add_argument("id", type=int, help="The id of the task to modify")
    parser_modify.add_argument("details", nargs='+', default='No details', help="New details of the task")
    parser_modify.add_argument(
    "--label",
    choices=["shopping", "sport", "homework", "administrative", "meetings"],
    help="New label of the task"
    )
    
    #RM SUBPARSER / file.txt rm id
    parser_rm = subparsers.add_parser("rm", help="Remove an existing task")
    parser_rm.add_argument("id", type=int, help="The id of the task to remove")
    
    #SHOW SUBPARSER / file.txt show
    parser_show = subparsers.add_parser("show", help="Show all tasks")

    # FUTURE SUBPARSER / file.txt future
    parser_future = subparsers.add_parser("future", help="Add a future task")
    parser_future.add_argument("details", nargs="+", help="Details of the future task")
    parser_future.add_argument("--label", "-l", required=True, nargs="+",help="Label of the future task")
    future_subparsers = parser_future.add_subparsers(dest="future_command", required=True)

    # DATE / file.txt future ... date
    parser_date = future_subparsers.add_parser("date", help="Future task starting from a date")
    parser_date.add_argument("date",type=int,help="The date of the task")

   # TASK / file.txt future ... task
    parser_task = future_subparsers.add_parser( "task", help="Future task depending on another task")
    parser_task.add_argument("id", type=int, help="Id of the previous task")
    
    return parser
