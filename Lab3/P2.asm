section .data
    ; declarar la variable M
    M db 10

section .bss
    ; reservar espacio de memoria para ptr_fibo
    ptr_fibo resb 11
section .text
    global _start

_start:

    ;limpiamos los registros a utilizar
    xor bl,bl
    xor r8b,r8b
    xor r9b,r9b
    xor r10b,r10b
    xor ecx,ecx

    ;inicializamos el contador ecx de 32 bits a partir de 0
    mov ecx,0

    ;movemos el valor de 0 al registro bl
    mov bl,0

    ;inicializamos los dos primeros valores de la serie
    ;inicializamos el primer valor
    mov [ptr_fibo+ecx*1],bl

    ;incrementamos a 1 el valor de bl
    inc bl

    inc ecx
    ;inicializamos el segundo valor
    mov [ptr_fibo+ecx*1],bl

    ;nuestro valor de ecx será 2
    inc ecx;

loop0:
    ;tenemos nuestro r8b para Fn-2
    mov r8b,[ptr_fibo+(ecx-2)*1]

    ;tenemos nuestro r8b para Fn-1
    mov r9b,[ptr_fibo+(ecx-1)*1]

    ;sumamos el contendigo de los registros de r8b con r9b
    add r8b,r9b
    ;movemos el registro de r8b a r10b
    mov r10b,r8b

    ;movemos el registro de r10b a nuestro puntero que almacenara la serie
    mov [ptr_fibo+ecx*1],r10b

    ;incrementamos la cuenta ecx
    inc ecx

    ;incremetamos el valor de M para comparar con su tamaño que separamos
    inc dword[M]
    ;asi compararemos y si es menor e igual saltara a la etiqueta loop0
    cmp ecx,M
    jle loop0

_end:
    mov rax, 0x3C
    mov rdi, 0
    syscall