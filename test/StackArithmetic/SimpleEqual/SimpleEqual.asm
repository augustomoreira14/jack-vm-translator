@8 // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1
@8 // push constant 8
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
@JEQSimpleEqual.0
D;JEQ
D=1
(JEQSimpleEqual.0)
D=D-1
@SP
A=M
M=D
@SP
M=M+1
@5 // push constant 5
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
@JEQSimpleEqual.1
D;JEQ
D=1
(JEQSimpleEqual.1)
D=D-1
@SP
A=M
M=D
@SP
M=M+1
