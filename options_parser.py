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
    parser_future = subparsers.add_parser("future",help="Manage a future task")
    future_subparser = parser.add_subparsers(help="Sub-command for future", dest="future", required=True, )

    #PARSER DATE / file.txt future date
    parser_date = future_subparser.add_parser("date", help="Add future task with date")
    parser_date.add_argument("date", type=int, help="The date of the task")

    #PARSER TASK / file.txt future task
    parser_task = future_subparser.add_parser("task", help="Add future task with task")
    parser_task.add_argument("id", type=int, help="id of the previows task")
    
    return parser
