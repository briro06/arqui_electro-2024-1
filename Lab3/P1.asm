section .data
    ; declaramos la variable M=[2,2^16-1], entonces el tipo de dato seria de 16 bits
    M dw 20000
    ; declaramos la variable B=[2,9], el tipo de dato seria de 8 bits
    B db 3
section .bss
    ; reservamos espacio de memoria(16 bits) para ptr_Q de tamaño 20
    ptr_Q resw 20
    ; reservamos espacio de memoria(16 bits) para ptr_R de tamaño 20
    ptr_R resw 20
section .text
    global _start

_start:
    ;limpiamos los registros a utilizar
    xor ax,ax
    xor r10,r10
    xor ecx,ecx
    xor r8w,r8w

    ;inicializamos el contador ecx de 32 bits
    mov ecx,0

    ;movemos el valor de la variable M(16 bits)=73 a ax(16 bits)
    mov ax,word[M]

loop1:
    ;limpiamo el valor del registro dx al incio de cada división 
    xor dx,dx

    ;movemos el valor de 3 a r8w para luego compararlo
    movzx r8w,byte[B];

    ;div divisor -> dx:ax=(dx:ax/divisor)
    ;dx:ax=M/B=73/3
    div word[B]


    ;el residuo se guarda en dx(16 bits)
    ;indexamos el puntero para que cada iteración
    mov [ptr_R+ecx*2],dx

    ;el cociente se guarda en ax (16 bits)
    ;indexamos el puntero para que cada iteración
    mov [ptr_Q+ecx*2],ax

    ;movemos el valor del cociente a ax para la siguiente división
    mov ax,[ptr_Q+ecx*2]

    ;movemos el valor del residuo a r10
    movzx r10,word[ptr_R+ecx*2]

    ;incrementamos la cuenta ecx
    inc ecx

    ;comparamos el valor del cociente con el de la base
    ;si el valor del cociente es mayor al de la base
    ;continua el loop
    cmp ax,r8w
    jg loop1

_end:
    mov rax, 0x3C
    mov rdi, 0
    syscall