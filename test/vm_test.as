org $123
label:
    ldm si $56DE
    mov ax si
org $0
    ldi     ax #3
    ldi bx #2       ; This is a comment and should be ignored.
    add ax bx
    bra label
END
