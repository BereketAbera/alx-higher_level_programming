#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for md in dir(hidden_4):
        if md[:2] != '__':
            print(md)
