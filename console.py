#!/usr/bin/python3
"""Console Module
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the AirBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    classDict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                 'City': City, 'Amenity': Amenity, 'State': State,
                 'Review': Review}

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
            my_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instane.
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
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance. Save the change into the JSON file.
        Usage: destroy <className> <instanceID>
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
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        Usage: all   or   all <className>
        """

        if arg == "":
            print([x.__str__() for x in storage.all().values()])
        else:
            if arg not in HBNBCommand.classDict.keys():
                print("** class doesn't exist **")
                return
            objl = []
            for obj in storage.all().values():
                if arg == obj.__class__.__name__:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, args):
        """Updates an instance and save the change into the JSON file.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        if not args:
            print("** class name missing **")
            return

        all_objs = storage.all()
        inst_p = False

        try:
            arg = args.split(' ')
            for key, objc in all_objs.items():
                cls_name = objc.__class__.__name__
                if arg[0] == cls_name and arg[1].strip('"') == objc.id:
                    inst_p = True
            model_name, model_id, attr, value = args.split(' ')
        except Exception as e:
            if arg[0] not in HBNBCommand.classDict.keys():
                print("** class doesn't exist **")
                return
            if args.count(' ') == 0:
                print("** instance id missing **")
                return
            if inst_p is False:
                print("** no instance found **")
                return
            if args.count(' ') == 1:
                print("** attribute name missing **")
            elif args.count(' ') == 2:
                print("** value missing **")
            elif args.count(' ') > 3:
                # TODO: Allow this case, and ignore the extra arguments
                print("** too many arguments**")
            else:
                print(e)
        else:
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == model_name and ob_id == model_id.strip('"'):
                    setattr(objc, attr, value)
                    storage.save()
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
