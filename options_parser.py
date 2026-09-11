# FUTURE SUBPARSER / file.txt future
parser_future = subparsers.add_parser(
    "future",
    help="Add a future task"
)

parser_future.add_argument(
    "details",
    nargs="+",
    help="Details of the future task"
)

parser_future.add_argument(
    "--label",
    "-l",
    required=True,
    nargs="+",
    help="Label of the future task"
)

future_condition = parser_future.add_mutually_exclusive_group(
    required=True
)

future_condition.add_argument(
    "--date",
    type=int,
    help="Date from which the task can be done"
)

future_condition.add_argument(
    "--task",
    type=int,
    help="Id of the task that must be completed first"
)
