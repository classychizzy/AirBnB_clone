#!/usr/bin/python3
"""comment"""
import cmd
from models.base_model import BaseModel
from models.user import User
import json

class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    classDict = {'BaseModel': BaseModel, 'User': User}

    def do_quit(self, arg):
        """Quit command to exit the programm"""
        return True

    def emptyline(self):
        """An empty line does nothing"""
        pass

    def do_EOF(self, arg):
        """Quits the console"""
        return True

    def do_create(self, model):
        """Creates a new instance of a given class, saves it and prints the id.
        Usage: create <className>
        """
        
        if not model:
            print("** class name missing **")
        elif model not in HBNBCommand.classDict.keys():
            print("** class doesn't exist **")
        else:
            my_model = HBNBCommand.classDict[model]()
            print(my_model.id)
            #my_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.
        Usage: show <className> <instanceID>
        """
        
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        
        if args[0] not in HBNBCommand.classDict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("test")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
