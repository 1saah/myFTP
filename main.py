# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# File Transfer Protocol

# **define the using methods(in some specific classes) first, then according to the methods to write the classes
# this means that we should write codes according to requirements but not the classes we have

# server structure
    # bin: to operate each class in core directory
        # use abs_file_path = os.path.abspath(__file__) to get file abs path
        # use root = os.path.dirname(abs_file_path) to get the parent name of this file(abs path)
        # use sys.path.append(root) to add this path to PYTHONPATH list

        # __name__ and __main__ is the variable which Python define in advance
        # use if __name__ == "__main__":   // only excute the following codes when you do not import this module but use it as main
            # ........
        # normally use this to modules which is often imperted some codes

        # teminal: can type 'python', then you can use python codes in terminal, you can type exit() to quit Python mode

        # def __init__:  // constructor method
            #....

        # sys.argv: is a parameter to save you type on the Terminal, from 1 to n, atgv[0] is the running name
            # vertify and execute sys.argv cmd
                # 1. a class which contain __init__, vertify_argv(), help_msg(), execute()
                # 2. vertify_argv(): len() > 1, because the basic length(only have [0]) is 1, cannot < 2
                #                    use reflection hasattr(self, cmd) to determine whether has this parameter or method
                # 3. help_msg(): print all  function commands, use msg =  '''
                #                                                         start
                #                                                         stop
                #                                                         restart
                #                                                         createuser
                #                                                              '''
                # exit(msg)
                # 4. execute(): use getattr(self, cmd) to excute argv_cmd, setattr(self, alias, func), delattr

    # config
        # settings.py to store some constants
            # path = os.path.join(path1, path2), this operation will combine two paths to one
            # using %s to insert one string in a string after %
            # file.ini: a configuration file for computer software. It contains key_value pairs that represent properties and their values. Can be used by configparser
            # .center(length, 'signal') : put string in the middle of this 50 length string using signal fulfill them
    # core
        # main.py
            # using self make parameter global can simplify the value passing
        # management.py
    # home
    # log

# client structure
    # use optparser to get input
