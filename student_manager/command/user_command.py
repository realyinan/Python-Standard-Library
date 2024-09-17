COMMAND_LIST = {
    "add",
    "list",
    "delete",
    "edit",
    "exit",
    "average"
}

def get_user_command() -> str:
    while True:
        command = input("please input command: ")
        cmd = command.lower()
        if cmd not in COMMAND_LIST:
            print(f"{cmd} is not a valid command")
        else:
            return cmd
        