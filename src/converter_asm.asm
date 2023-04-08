segment .data

segment .bss

segment .text
    global converter_asm
    
;params: cripto, divisa
converter_asm:
    enter 0,0           

    fld dword [ebp + 8]     
    fmul dword [ebp + 12]   

    leave              
    ret                    