#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    print("{} argument{}".format(argc, "s" if argc != 1 else ""), end="")
    print("{}".format("." if argc == 0 else ":"))

    if argc > 0:
        for x in range(1, argc + 1):
            print("{}: {}".format(x, sys.argv[x]))
