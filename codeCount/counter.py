from os import listdir
from os.path import isfile, join

def main(args):
    folder = args[0]
    maxdepth = int(args[1])
    extensions = args[2:]
    print(listdir(folder))
    print(count(folder, extensions, maxdepth))

def count(folder, extensions, depth):
    c = sum([len(open(join(folder, f)).readlines()) for f in listdir(folder) if isfile(join(folder, f)) and extensionMatches(f, extensions)])
    if c > 0:
        print(f'{folder}: {c}')
    if depth > 0:
        c += sum([count(join(folder, f), extensions, depth - 1) for f in listdir(folder) if not isfile(join(folder, f))])
    return c

def extensionMatches(fileName, expected):
    return fileName.split('.')[-1] in expected


if __name__ == '__main__':
    import sys
    main([a.lower() for a in sys.argv[1:]])
