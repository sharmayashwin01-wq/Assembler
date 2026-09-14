; Sample Assembly Program

        MOV     R1, R2

START:      ADD     R3,     R1,    R2

        SUB R4,R3,R1

LOOP:   INC     R1

        CMP     R1,      #10

        JNZ     LOOP

        MOV     R5,     #100

END:    HALT