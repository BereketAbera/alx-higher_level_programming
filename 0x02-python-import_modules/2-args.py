#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    al = len(sys.argv) - 1
    print("{} {}{}".format(al, "argument" if al == 1 else "arguments",
                           "." if al == 0 else ":"))
    for index, value in enumerate(sys.argv[1:]):
        print("{}: {}".format(index + 1, value))
