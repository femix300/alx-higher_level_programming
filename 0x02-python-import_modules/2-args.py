#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    i = 1
    args_passed = sys.argv[1:]
    arguments = len(sys.argv)
    arguments -= 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    elif arguments == 1:
        print(f"{arguments} argument:")
        print(f"{arguments}: {sys.argv[arguments]}")
    else:
        print(f"{arguments} arguments:")
        for args in args_passed:
            print(f"{i}: {args}")
            i += 1
