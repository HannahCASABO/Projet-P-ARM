	.text
	.syntax unified
	.eabi_attribute	67, "2.09"
	.cpu	cortex-m0
	.eabi_attribute	6, 12
	.eabi_attribute	7, 77
	.eabi_attribute	8, 0
	.eabi_attribute	9, 1
	.eabi_attribute	34, 0
	.eabi_attribute	17, 1
	.eabi_attribute	20, 1
	.eabi_attribute	21, 0
	.eabi_attribute	23, 3
	.eabi_attribute	24, 1
	.eabi_attribute	25, 1
	.eabi_attribute	38, 1
	.eabi_attribute	18, 4
	.eabi_attribute	26, 2
	.eabi_attribute	14, 0
	.file	"main.c"
	.globl	run
	.p2align	1
	.type	run,%function
	.code	16
	.thumb_func
run:
	.fnstart
	.pad	#124
	sub	sp, #124
	@APP
	sub	sp, #508
	@NO_APP
	@APP
	sub	sp, #452
	@NO_APP
	movs	r0, #0
	str	r0, [sp, #36]
	movs	r0, #3
	str	r0, [sp, #32]
	movs	r1, #4
	str	r1, [sp, #28]
	movs	r2, #10
	str	r2, [sp, #16]
	movs	r2, #18
	str	r2, [sp, #12]
	movs	r2, #52
	str	r2, [sp, #8]
	ldr	r2, [sp, #32]
	ldr	r3, [sp, #28]
	adds	r2, r2, r3
	str	r2, [sp, #24]
	ldr	r2, [sp, #28]
	ldr	r3, [sp, #32]
	subs	r2, r2, r3
	str	r2, [sp, #20]
	ldr	r2, [sp, #16]
	ldr	r3, [sp, #24]
	adds	r2, r2, r3
	str	r2, [sp, #16]
	ldr	r2, [sp, #16]
	ldr	r3, [sp, #20]
	subs	r2, r2, r3
	str	r2, [sp, #16]
	ldr	r2, [sp, #12]
	lsls	r2, r2, #2
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	asrs	r2, r2, #1
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	asrs	r2, r2, #1
	str	r2, [sp, #36]
	ldr	r2, [sp, #12]
	movs	r3, #15
	ands	r2, r3
	str	r2, [sp, #12]
	ldr	r2, [sp, #8]
	movs	r3, #128
	orrs	r2, r3
	str	r2, [sp, #8]
	ldr	r2, [sp, #12]
	ldr	r3, [sp, #8]
	eors	r2, r3
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	bics	r2, r0
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #1
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #3
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #4
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #2
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #1
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #2
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #3
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #4
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #5
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #6
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	adds	r2, r2, #7
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	movs	r3, #5
	eors	r2, r3
	str	r2, [sp, #36]
	ldr	r2, [sp, #36]
	eors	r2, r1
	str	r2, [sp, #36]
	ldr	r1, [sp, #36]
	eors	r1, r0
	str	r1, [sp, #36]
	ldr	r0, [sp, #36]
	movs	r1, #2
	eors	r0, r1
	str	r0, [sp, #36]
	ldr	r0, [sp, #36]
	movs	r1, #1
	eors	r0, r1
	str	r0, [sp, #36]
	ldr	r0, [sp, #36]
	str	r0, [sp, #4]
	ldr	r0, [sp, #4]
	adds	r0, r0, #7
	str	r0, [sp]
	ldr	r0, [sp]
	str	r0, [sp, #36]
	ldr	r0, [sp, #36]
	lsls	r0, r0, #1
	str	r0, [sp, #36]
	ldr	r0, [sp, #36]
	adds	r0, #9
	str	r0, [sp, #36]
	ldr	r0, [sp, #36]
	subs	r0, #9
	str	r0, [sp, #36]
	b	.LBB0_1
.LBB0_1:
	b	.LBB0_2
.LBB0_2:
	b	.LBB0_2
.Lfunc_end0:
	.size	run, .Lfunc_end0-run
	.cantunwind
	.fnend

	.ident	"clang version 12.0.0"
	.section	".note.GNU-stack","",%progbits
	.addrsig
	.eabi_attribute	30, 6
