import sys
from os import path, listdir
from Processor import Processor

try:
    if path.isdir(sys.argv[1]):
        files = listdir(sys.argv[1])
        realPath = path.realpath(sys.argv[1])
        for file in files:
            if file.endswith('.vm'):
                filename = path.join(realPath, file)
                processor = Processor(filename)
                processor.start()

    elif path.isfile(sys.argv[1]):
        if sys.argv[1].endswith('.vm'):
            processor = Processor(sys.argv[1])
            processor.start()
    else:
        raise FileNotFoundError


except FileNotFoundError:
    print("File not found.")
