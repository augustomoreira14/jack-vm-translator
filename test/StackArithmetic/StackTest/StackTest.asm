@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // eq
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JEQStackTest.0
D;JEQ
D=1
(JEQStackTest.0)
D=D-1
@SP
A=M
M=D
@SP
M=M+1
@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16 // push constant 16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // eq
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JEQStackTest.1
D;JEQ
D=1
(JEQStackTest.1)
D=D-1
@SP
A=M
M=D
@SP
M=M+1
@16 // push constant 16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17 // push constant 17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // eq
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JEQStackTest.2
D;JEQ
D=1
(JEQStackTest.2)
D=D-1
@SP
A=M
M=D
@SP
M=M+1
@892 // push constant 892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // lt
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JLT_TRUE_StackTest.3
D;JLT
D=0
@JLT_FALSE_StackTest.3
0;JMP
(JLT_TRUE_StackTest.3)
D=-1
(JLT_FALSE_StackTest.3)
@SP
A=M
M=D
@SP
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892 // push constant 892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // lt
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JLT_TRUE_StackTest.4
D;JLT
D=0
@JLT_FALSE_StackTest.4
0;JMP
(JLT_TRUE_StackTest.4)
D=-1
(JLT_FALSE_StackTest.4)
@SP
A=M
M=D
@SP
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891 // push constant 891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // lt
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JLT_TRUE_StackTest.5
D;JLT
D=0
@JLT_FALSE_StackTest.5
0;JMP
(JLT_TRUE_StackTest.5)
D=-1
(JLT_FALSE_StackTest.5)
@SP
A=M
M=D
@SP
M=M+1
@32767 // push constant 32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // gt
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JGT_TRUE_StackTest.6
D;JGT
D=0
@JGT_FALSE_StackTest.6
0;JMP
(JGT_TRUE_StackTest.6)
D=-1
(JGT_FALSE_StackTest.6)
@SP
A=M
M=D
@SP
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767 // push constant 32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // gt
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JGT_TRUE_StackTest.7
D;JGT
D=0
@JGT_FALSE_StackTest.7
0;JMP
(JGT_TRUE_StackTest.7)
D=-1
(JGT_FALSE_StackTest.7)
@SP
A=M
M=D
@SP
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766 // push constant 32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // gt
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@JGT_TRUE_StackTest.8
D;JGT
D=0
@JGT_FALSE_StackTest.8
0;JMP
(JGT_TRUE_StackTest.8)
D=-1
(JGT_FALSE_StackTest.8)
@SP
A=M
M=D
@SP
M=M+1
@57 // push constant 57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31 // push constant 31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53 // push constant 53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // add
AM=M-1
D=M
A=A-1
M=D+M
@112 // push constant 112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // sub
AM=M-1
D=M
A=A-1
M=M-D
@SP // neg
A=M
A=A-1
M=-M
@SP // and
AM=M-1
D=M
A=A-1
M=D&M
@82 // push constant 82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP // or
AM=M-1
D=M
A=A-1
M=D|M
@SP // not
A=M
A=A-1
M=!M
