nasm -f elf64 rxy_ASM.asm -o rxy_ASM.o
gcc rxy_ASM.o main.c -o main -lm
./main 100