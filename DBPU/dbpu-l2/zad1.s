	.file	"zad1.c"
	.text
	.section	.rodata
.LC0:
	.string	"hello world"
.LC1:
	.string	"%s"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp    ;    Umieszczenie bazowego wskaźnika na stos
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp    ;    Kopiuje rsp do rbp (q oznacz 64bity)
	.cfi_def_cfa_register 6
	subq	$16, %rsp    ;    odejmuje 16 od rsp i wynik trafia do rsp
	leaq	.LC0(%rip), %rax    ;    wczytuje efektywny adres B do rax.
	movq	%rax, -8(%rbp)    ;    kopiuje na stos 8 elemntow z ax do bp
	movq	-8(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax    ; l - rejestr 32 bit
	call	printf@PLT    ;   Wywołanie funkcji printf
	movl	$0, %eax    ; Kopiuje 0 do eax
	leave    ;    kopiuje wskaźnik ramki do punktu stosu i zwalnia przestrzeń stosu
	.cfi_def_cfa 7, 8
	ret    ;    Powrót do programu nadrzędnego
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
