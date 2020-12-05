def match(command):
    return command.script.startswith('car')

def get_new_command(command):
    return 'cat' + command.script[3:]