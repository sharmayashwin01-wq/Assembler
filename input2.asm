// Source file hack asembly
        @10
        D=A
        @20
        D=D+A

(START)
        @RESULT
        M=D
        @i
        M=0

(LOOP)
        @i
        M=M+1
        @10
        D=M
        @i
        D=D-M
        @LOOP
        D;JGT
        @RESULT
        D=M
        @END
        0;JMP

(END)
        @END
        0;JMP
