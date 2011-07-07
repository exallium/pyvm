    ldi     ax #3
    ldi bx #2       ; This is a comment and should be ignored.
    add ax bx
label:
    ldm si $56DE
    mov ax si
    bra label
END
