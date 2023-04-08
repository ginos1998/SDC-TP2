all: calc

calc: ./src/main.c converter_asm.o
	gcc ./src/main.c converter_asm.o -m32 -o calc

converter_asm.o: src/converter_asm.asm
	nasm -f elf32 src/converter_asm.asm -o converter_asm.o

