#!/usr/bin/python3
"""comment"""
import cmd

class HBNBCommand(cmd.Cmd):
    """comment"""
    prompt = '(hbnb)'

    def do_quit(self):
        """This command is to quit"""
        self.close()
        return True

    def emptyline():
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
