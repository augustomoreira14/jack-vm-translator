from os import path

class CodeWriter():

    def __init__(self, file):
        basename = path.basename(file)
        self.module = path.splitext(basename)[0]

        self.file = open(file, "w")
        self.commandsStack = {
            'C_PUSH': self.writePush,
            'C_POP': self.writePop
        }

        self.commandsArithmetic = {
            'add': self.writeArithmeticAdd,
            'sub': self.writeArithmeticSub,
            'eq': self.writeArithmeticEq,
            'lt': self.writeArithmeticLt,
            'gt': self.writeArithmeticGt,
            'neg': self.writeArithmeticNeg,
            'and': self.writeArithmeticAnd,
            'or': self.writeArithmeticOr,
            'not': self.writeArithmeticNot
        }

        self.countLabel = 0

    def writeArithmetic(self, command):
        self.commandsArithmetic[command]()

    def writeArithmeticAdd(self):
        self.write("@SP // add")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=D+M")

    def writeArithmeticSub(self):
        self.write("@SP // sub")  # 256, A=0, RAM[0]
        self.write("AM=M-1")  # A=255, RAM[0] = 255
        self.write("D=M")  # D=topo pilha
        self.write("A=A-1")  # A=254
        self.write("M=M-D")  # RAM[254] = novo topo pilha - D

    def writeArithmeticEq(self):
        label = "JEQ{}.{}".format(self.module, self.countLabel)
        self.countLabel += 1
        
        self.write("@SP // eq")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M-D")
        self.write("@" + label)
        self.write("D;JEQ") #Se D = 0 pula para o label
        self.write("D=1")
        self.write("("+ label +")")
        self.write("D=D-1") #Se D = 0, logo D = 0 - 1 = -1 (verdadeiro)
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

    def writeArithmeticLt(self):
        labelTrue = "JLT_TRUE_{}.{}".format(self.module, self.countLabel)
        labelFalse = "JLT_FALSE_{}.{}".format(self.module, self.countLabel)
        self.countLabel += 1

        self.write("@SP // lt")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M-D")
        self.write("@" + labelTrue)
        self.write("D;JLT")  # Se verdadeiro pula para labelTrue
        self.write("D=0")
        self.write("@" + labelFalse)
        self.write("0;JMP")
        self.write("(" + labelTrue + ")")
        self.write("D=-1")
        self.write("("+labelFalse+")")
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

    def writeArithmeticGt(self):
        labelTrue = "JGT_TRUE_{}.{}".format(self.module, self.countLabel)
        labelFalse = "JGT_FALSE_{}.{}".format(self.module, self.countLabel)
        self.countLabel += 1

        self.write("@SP // gt")
        self.write("AM=M-1")
        self.write("D=M")
        self.write("@SP")
        self.write("AM=M-1")
        self.write("D=M-D")
        self.write("@" + labelTrue)
        self.write("D;JGT") # Se verdadeiro pula para labelTrue
        self.write("D=0")
        self.write("@" + labelFalse)
        self.write("0;JMP")
        self.write("("+ labelTrue +")")
        self.write("D=-1")
        self.write("("+labelFalse+")")
        self.write("@SP")
        self.write("A=M")
        self.write("M=D")
        self.write("@SP")
        self.write("M=M+1")

    def writeArithmeticNeg(self):
        self.write("@SP // neg")
        self.write("A=M")
        self.write("A=A-1")
        self.write("M=-M")

    def writeArithmeticAnd(self):
        self.write("@SP // and") # SP = 256, A = 0
        self.write("AM=M-1") # A = 255, RAM[0] = 255
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=D&M")

    def writeArithmeticOr(self):
        self.write("@SP // or")  # SP = 256, A = 0
        self.write("AM=M-1")  # A = 255, RAM[0] = 255
        self.write("D=M")
        self.write("A=A-1")
        self.write("M=D|M")

    def writeArithmeticNot(self):
        self.write("@SP // not")
        self.write("A=M")
        self.write("A=A-1")
        self.write("M=!M")

    def writePushPop(self, command, segment, index):
        self.commandsStack[command](segment, index)

    def writePush(self, segment, index):
        if segment == "constant":
            self.write("@{} // push {} {}".format(index, segment, index))
            self.write("D=A")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
        elif segment in ["local", "argument", "this", "that"]:
            self.write(
                "@{} // push {} {}".format(self.segmentPointer(segment, index), segment, index))
            self.write("D=M")
            self.write("@{}".format(index))
            self.write("A=D+A")
            self.write("D=M")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")
        elif segment in ["temp", "static", "pointer"]:
            self.write(
                "@{} // push {} {}".format(self.segmentPointer(segment, index), segment, index))
            self.write("D=M")
            self.write("@SP")
            self.write("A=M")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M+1")

    def writePop(self, segment, index):
        if segment in ["local", "argument", "this", "that"]:
            self.write(
                "@{} // pop {} {}".format(self.segmentPointer(segment, index), segment, index))
            self.write("D=M")
            self.write("@{}".format(index))
            self.write("D=D+A")
            self.write("@R13")
            self.write("M=D")
            self.write("@SP")
            self.write("M=M-1")
            self.write("A=M")
            self.write("D=M")
            self.write("@R13")
            self.write("A=M")
            self.write("M=D")
        elif segment in ["temp", "static", "pointer"]:
            self.write("@SP // pop {} {}".format(segment, index))
            self.write("M=M-1")
            self.write("A=M")
            self.write("D=M")
            self.write("@{}".format(self.segmentPointer(segment, index)))
            self.write("M=D")

    def segmentPointer(self, segment, index):
        if segment == 'local':
            return 'LCL'
        elif segment == 'argument':
            return 'ARG'
        elif segment == 'this':
            return 'THIS'
        elif segment == 'that':
            return 'THAT'
        elif segment == 'temp':
            return 'R{}'.format(5+index)
        elif segment == 'pointer':
            return 'R{}'.format(3+index)
        elif segment == 'static':
            return '{}.{}'.format(self.module, index)

    def write(self, string):
        self.file.write(string + "\n")

    def close(self):
        self.file.close()
