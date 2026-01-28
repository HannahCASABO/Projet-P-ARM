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
	.p2align	2
	.type	run,%function
	.code	16
	.thumb_func
run:
	.fnstart
	.pad	#132
	sub	sp, #132
	@APP
	sub	sp, #508
	@NO_APP
	@APP
	sub	sp, #452
	@NO_APP
	movs	r0, #0
	str	r0, [sp, #44]
	movs	r1, #3
	str	r1, [sp, #40]
	movs	r2, #4
	str	r2, [sp, #36]
	str	r0, [sp, #32]
	str	r0, [sp, #28]
	movs	r0, #10
	str	r0, [sp, #24]
	movs	r0, #18
	str	r0, [sp, #20]
	movs	r0, #52
	str	r0, [sp, #16]
	ldr	r0, [sp, #40]
	ldr	r2, [sp, #36]
	adds	r0, r0, r2
	str	r0, [sp, #32]
	ldr	r0, [sp, #36]
	ldr	r2, [sp, #40]
	subs	r0, r0, r2
	str	r0, [sp, #28]
	ldr	r0, [sp, #24]
	ldr	r2, [sp, #32]
	adds	r0, r0, r2
	str	r0, [sp, #24]
	ldr	r0, [sp, #24]
	ldr	r2, [sp, #28]
	subs	r0, r0, r2
	str	r0, [sp, #24]
	ldr	r0, [sp, #20]
	lsls	r0, r0, #2
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	asrs	r0, r0, #1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	asrs	r0, r0, #1
	str	r0, [sp, #44]
	ldr	r0, [sp, #20]
	movs	r2, #15
	ands	r0, r2
	str	r0, [sp, #20]
	ldr	r0, [sp, #16]
	movs	r2, #128
	orrs	r0, r2
	str	r0, [sp, #16]
	ldr	r0, [sp, #20]
	ldr	r2, [sp, #16]
	eors	r0, r2
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	bics	r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #40]
	cmp	r0, #3
	bne	.LBB0_2
	b	.LBB0_1
.LBB0_1:
	ldr	r0, [sp, #44]
	adds	r0, r0, #1
	str	r0, [sp, #44]
	b	.LBB0_3
.LBB0_2:
	ldr	r0, [sp, #44]
	adds	r0, r0, #2
	str	r0, [sp, #44]
	b	.LBB0_3
.LBB0_3:
	ldr	r0, [sp, #36]
	cmp	r0, #0
	beq	.LBB0_5
	b	.LBB0_4
.LBB0_4:
	ldr	r0, [sp, #44]
	adds	r0, r0, #3
	str	r0, [sp, #44]
	b	.LBB0_5
.LBB0_5:
	ldr	r0, [sp, #32]
	ldr	r1, [sp, #28]
	cmp	r0, r1
	blt	.LBB0_7
	b	.LBB0_6
.LBB0_6:
	ldr	r0, [sp, #44]
	adds	r0, r0, #4
	str	r0, [sp, #44]
	b	.LBB0_8
.LBB0_7:
	ldr	r0, [sp, #44]
	adds	r0, r0, #5
	str	r0, [sp, #44]
	b	.LBB0_8
.LBB0_8:
	ldr	r0, [sp, #44]
	adds	r0, r0, #1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #3
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #4
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #2
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #2
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #3
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #4
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #5
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #6
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, r0, #7
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	movs	r1, #5
	eors	r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	movs	r1, #4
	eors	r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	movs	r1, #3
	eors	r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	movs	r1, #2
	eors	r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	movs	r1, #1
	eors	r0, r1
	str	r0, [sp, #44]
	movs	r0, #0
	str	r0, [sp, #12]
	b	.LBB0_9
.LBB0_9:
	ldr	r0, [sp, #12]
	cmp	r0, #7
	bgt	.LBB0_11
	b	.LBB0_10
.LBB0_10:
	ldr	r0, [sp, #44]
	ldr	r1, [sp, #12]
	adds	r0, r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #12]
	adds	r0, r0, #1
	str	r0, [sp, #12]
	b	.LBB0_9
.LBB0_11:
	movs	r0, #5
	str	r0, [sp, #8]
	b	.LBB0_12
.LBB0_12:
	ldr	r0, [sp, #8]
	cmp	r0, #0
	beq	.LBB0_14
	b	.LBB0_13
.LBB0_13:
	ldr	r0, [sp, #44]
	ldr	r1, [sp, #8]
	eors	r0, r1
	str	r0, [sp, #44]
	ldr	r0, [sp, #8]
	subs	r0, r0, #1
	str	r0, [sp, #8]
	b	.LBB0_12
.LBB0_14:
	ldr	r0, [sp, #44]
	str	r0, [sp, #4]
	ldr	r0, [sp, #4]
	adds	r0, r0, #7
	str	r0, [sp]
	ldr	r0, [sp]
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	lsls	r0, r0, #1
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	adds	r0, #9
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	subs	r0, #9
	str	r0, [sp, #44]
	ldr	r0, [sp, #44]
	ldr	r1, .LCPI0_0
	str	r0, [r1]
	b	.LBB0_15
.LBB0_15:
	b	.LBB0_16
.LBB0_16:
	b	.LBB0_16
	.p2align	2
.LCPI0_0:
	.long	RESULT
.Lfunc_end0:
	.size	run, .Lfunc_end0-run
	.cantunwind
	.fnend

	.type	RESULT,%object
	.bss
	.globl	RESULT
	.p2align	2
RESULT:
	.long	0
	.size	RESULT, 4

	.ident	"clang version 12.0.0"
	.section	".note.GNU-stack","",%progbits
	.addrsig
	.addrsig_sym RESULT
	.eabi_attribute	30, 6
