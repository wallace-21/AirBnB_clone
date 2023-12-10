#!/usr/bin/python3
""" HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ create a console using cmd """

    prompt = "(hbnb) "
    __cnames = {"BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"}

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        arguments = line.split()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__cnames:
            print("** class doesn't exist **")
        else:
            print(eval(arguments[0])().id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance based
         on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        arguments = line.split()
        dobjects = storage.all()

        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__cnames:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in dobjects:
            print("** no instance found **")
        else:
            print(dobjects["{}.{}".format(arguments[0], arguments[1])])

    def do_destroy(self, line):
        """Deletes an instance len(arguments) ==
        2 based on the class name and id (save the
          change into the JSON file). Ex:
        $ destroy BaseModel 1234-1234-1234."""
        arguments = line.split()
        dobjects = storage.all()
        if len(arguments) == 0:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.__cnames:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arguments[0], arguments[1]) not in dobjects:
            print("** no instance found **")
        else:
            del dobjects["{}.{}".format(arguments[0], arguments[1])]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not S
        on the class name. Ex: $ all BaseModel or $ all"""
        arguments = line.split()
        newlist = []
        dobjects = storage.all()
        if len(arguments) == 0:
            print("** class doesn't exist **")
        elif arguments[0] not in HBNBCommand.__cnames:
            print("** class doesn't exist **")
        else:
            for i in dobjects.values():
                if len(arguments) == 0 or arguments[0] == i.__class__.__name__:
                    newlist.append(i.__str__())
            print(newlist)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file). Ex: $ update
         BaseModel 1234-1234-1234 email "aibnb@mail.com"""
        arguments = line.split()
        dobjects = storage.all()
        if len(arguments) < 4:
            if len(arguments) == 0:
                print("** class name missing **")
            elif len(arguments) == 1:
                print("** instance id missing **")
            elif len(arguments) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")

        elif arguments[0] not in HBNBCommand.__cnames:
            print("** class doesn't exist **")
        else:
            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in dobjects:
                print("** no instance found **")
            else:
                setattr(dobjects[key], arguments[2], arguments[3])
                storage.save()

    def do_quit(self, line):
        """ hadles the quit command"""
        return True

    def do_EOF(self, line):
        """ handles the quit command """
        return True

    def help_quit(self):
        """ hepls with help """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ helps with help """
        print("EOF command to exit the program")

    def emptyline(self):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
