#!/usr/bin/python3
""" HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ create a console using cmd """

    prompt = "(hbnb)"

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

    def complete_nothing(self, line, text, begidx, endidx):
        """ handles empty line """
        command = [""]
        return [cmd for cmd in command if cmd.startswith(text)]


if __name__ == '__main__':
    HBNBCommand().cmdloop()
