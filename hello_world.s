.global _start

.data
    message:  .ascii  "Hello World!\n"
    message_len: . - message            //  '.' is the current address

_start:
    MOV R7, #4  // Write
    MOV R0, #1  // Stdout
    LDR R1, =message
    LDR R2, #message_len
    SWI 0

    MOV R7, #1
    MOV R0, #0
    SWI 0
    
    
