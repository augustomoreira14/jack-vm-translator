import re
from Command import Command


class Parser():

    TYPES = {
        'push': 'C_PUSH',
        'pop': 'C_POP'
    }

    def __init__(self, file):
        f = open(file, 'r')
        text = f.read()
        f.close()

        text = re.sub(r'\/\/.*', '', text)
        self.commands = re.findall(r'[a-z]+\s[a-zA-Z\.]+\s[0-9]+|^[a-z]+', text, re.MULTILINE)
        self.commands = tuple(map(lambda x: x.split(" "), self.commands))
        self.lenTokens = len(self.commands)
        self.index = 0

    def advance(self):
        self.index += 1

    def hasMoreCommands(self):
        return self.index < self.lenTokens

    def commandType(self):
        if self.commands[self.index][0] in ["add", "sub", "eq", "lt", "gt", "neg", "and", "or", "not"]:
            return (Command.C_ARITHMETIC, self.commands[self.index][0])
        elif self.commands[self.index][0] in ["push", "pop"]:
            return (self.TYPES[self.commands[self.index][0]], self.commands[self.index][0])

    def arg1(self):
        return self.commands[self.index][1]

    def arg2(self):
        return int(self.commands[self.index][2])
