#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    funcs = dir()
    for i in range(0, len(funcs)):
        if func[i][:2] != "__":
            print('{:s}'.format(func[i]))
