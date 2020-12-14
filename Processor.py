from CodeWriter import CodeWriter
from Parser import Parser
from Command import Command
from os.path import splitext

class Processor():
    def __init__(self, filename):
        file = splitext(filename)[0]
        self.parser = Parser(file + '.vm')
        self.code = CodeWriter(file + '.asm')

    def start(self):
        while self.parser.hasMoreCommands():
          if self.parser.commandType()[0] in [Command.C_PUSH, Command.C_POP]:
            self.code.writePushPop(self.parser.commandType()[0], self.parser.arg1(), self.parser.arg2())

          elif self.parser.commandType()[0] == Command.C_ARITHMETIC:

            self.code.writeArithmetic(self.parser.commandType()[1])

          self.parser.advance()

        self.code.close()
