    global rxy_ASM
    section .text

rxy_ASM:
    ;limpiamos los registros 
    xorpd xmm2,xmm2 ; xmm2 será suma_den1
    xorpd xmm3,xmm3 ; xmm3 será suma_den2
    xorpd xmm4,xmm4 ; xmm4 será suma_num
    xor rcx,rcx ; rcx llevará la cuenta
condicion:
    cmp rdx,rcx ;compara el valor de N con i
    jle done ;si N<=i salta

bucle:
    ;para el entendimiento del código se debe tener en cuanto que registro representa que variable
    ;xmm5->a, xmm6->b, xmm7->den

    ;movss xmm8,[rdi+rcx*4] ;guardamos el valor de x[i] en un registro
    ;movss xmm9,[rdi+rcx*4] ;guardamos el valor de y[i] en un registro

    subss [rdi+rcx*4],xmm0 ;realizo la resta de x[i]-mediax y lo guardo en el puntero
    movss xmm5,[rdi+rcx*4] ;guardo el valor del puntero en el registro xmm5 que será nuestra variable a

    subss [rsi+rcx*4],xmm1 ;realizo la resta de y[i]-mediay y lo guardo en el puntero
    movss xmm6,[rsi+rcx*4] ;guardo el valor del puntero en el registro xmm6 que será nuestra variable b

    mulss xmm5,xmm6 ;multiplico el valor de a con b y lo guardo en el registro xmm5
    addss xmm4,xmm5 ;sumo el valor de suma_num con la multiplicación previa que realice y lo guardo en el registro xmm4

    movss xmm5,[rdi+rcx*4]; actualizo el valor de xmm5 que se vio afectado por la multiplicación
    mulss xmm5,xmm5 ;multiplico el valor de xmm5 con su mismo valor y lo gurdo en el mismo registro
    adss xmm2,xmm5 ;sumo el valor de xmm2 con el valor de xmm5 y guardo su valor en el registro xmm5

    mulss xmm6,xmm6 ;multiplico el valor de xmm6 por si mismo y guardo su valor en el mismo registro
    adss xmm3,xmm6 ;sumo el valor de xmm3 con el valor de xmm5 y guardo su valor en el mismo registro

    sqrtss xmm2,xmm2 ;hallo la raiz cuadrada del resgistro xmm2
    sqrtss xmm3,xmm3 ; hallo la raiz cuadrada del registro xmm3 
    mulss xmm2,xmm3 ;mutiplico el valor de xmm2 con xmm3
    movss xmm7,xmm2 ;muevo el valor de la multiplicación al registro xmm7

    inc rcx ;incremento el valor de rcx
    jmp condicion ;salto sin condición a la etiqueta condicion 
done:
    divss xmm4,xmm7 
    movss [rcx],xmm4 ;pasamos el valor de la diviisión a la dirección de memoria del puntero rxy
    ret ;retorno