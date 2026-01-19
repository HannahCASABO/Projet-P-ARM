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
	.pad	#132
	sub	sp, #132
	@APP
	sub	sp, #508
	@NO_APP
	@APP
	sub	sp, #452
	@NO_APP
	movs	r0, #3
	str	r0, [sp, #44]
	movs	r1, #4
	str	r1, [sp, #40]
	movs	r1, #0
	str	r1, [sp, #36]
	str	r1, [sp, #32]
	movs	r2, #10
	str	r2, [sp, #28]
	movs	r2, #18
	str	r2, [sp, #24]
	movs	r2, #52
	str	r2, [sp, #20]
	str	r1, [sp, #16]
	ldr	r1, [sp, #44]
	ldr	r2, [sp, #40]
	adds	r1, r1, r2
	str	r1, [sp, #36]
	ldr	r1, [sp, #40]
	ldr	r2, [sp, #44]
	subs	r1, r1, r2
	str	r1, [sp, #32]
	ldr	r1, [sp, #28]
	ldr	r2, [sp, #36]
	adds	r1, r1, r2
	str	r1, [sp, #28]
	ldr	r1, [sp, #28]
	ldr	r2, [sp, #32]
	subs	r1, r1, r2
	str	r1, [sp, #28]
	ldr	r1, [sp, #24]
	lsls	r1, r1, #2
	str	r1, [sp, #16]
	ldr	r1, [sp, #16]
	asrs	r1, r1, #1
	str	r1, [sp, #16]
	ldr	r1, [sp, #16]
	asrs	r1, r1, #1
	str	r1, [sp, #16]
	ldr	r1, [sp, #24]
	movs	r2, #15
	ands	r1, r2
	str	r1, [sp, #24]
	ldr	r1, [sp, #20]
	movs	r2, #128
	orrs	r1, r2
	str	r1, [sp, #20]
	ldr	r1, [sp, #24]
	ldr	r2, [sp, #20]
	eors	r1, r2
	str	r1, [sp, #16]
	ldr	r1, [sp, #16]
	bics	r1, r0
	str	r1, [sp, #16]
	ldr	r0, [sp, #44]
	cmp	r0, #3
	bne	.LBB0_2
	b	.LBB0_1
.LBB0_1:
	ldr	r0, [sp, #16]
	adds	r0, r0, #1
	str	r0, [sp, #16]
	b	.LBB0_3
.LBB0_2:
	ldr	r0, [sp, #16]
	adds	r0, r0, #2
	str	r0, [sp, #16]
	b	.LBB0_3
.LBB0_3:
	ldr	r0, [sp, #40]
	cmp	r0, #0
	beq	.LBB0_5
	b	.LBB0_4
.LBB0_4:
	ldr	r0, [sp, #16]
	adds	r0, r0, #3
	str	r0, [sp, #16]
	b	.LBB0_5
.LBB0_5:
	ldr	r0, [sp, #36]
	ldr	r1, [sp, #32]
	cmp	r0, r1
	blt	.LBB0_7
	b	.LBB0_6
.LBB0_6:
	ldr	r0, [sp, #16]
	adds	r0, r0, #4
	str	r0, [sp, #16]
	b	.LBB0_8
.LBB0_7:
	ldr	r0, [sp, #16]
	adds	r0, r0, #5
	str	r0, [sp, #16]
	b	.LBB0_8
.LBB0_8:
	movs	r0, #0
	str	r0, [sp, #12]
	b	.LBB0_9
.LBB0_9:
	ldr	r0, [sp, #12]
	cmp	r0, #7
	bgt	.LBB0_11
	b	.LBB0_10
.LBB0_10:
	ldr	r0, [sp, #16]
	ldr	r1, [sp, #12]
	adds	r0, r0, r1
	str	r0, [sp, #16]
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
	ldr	r0, [sp, #16]
	ldr	r1, [sp, #8]
	eors	r0, r1
	str	r0, [sp, #16]
	ldr	r0, [sp, #8]
	subs	r0, r0, #1
	str	r0, [sp, #8]
	b	.LBB0_12
.LBB0_14:
	ldr	r0, [sp, #16]
	str	r0, [sp, #4]
	ldr	r0, [sp, #4]
	adds	r0, r0, #7
	str	r0, [sp]
	ldr	r0, [sp]
	str	r0, [sp, #16]
	ldr	r0, [sp, #16]
	lsls	r0, r0, #31
	cmp	r0, #0
	bne	.LBB0_16
	b	.LBB0_15
.LBB0_15:
	ldr	r0, [sp, #16]
	adds	r0, #9
	str	r0, [sp, #16]
	b	.LBB0_17
.LBB0_16:
	ldr	r0, [sp, #16]
	subs	r0, #9
	str	r0, [sp, #16]
	b	.LBB0_17
.LBB0_17:
	b	.LBB0_18
.LBB0_18:
	b	.LBB0_19
.LBB0_19:
	b	.LBB0_19
.Lfunc_end0:
	.size	run, .Lfunc_end0-run
	.cantunwind
	.fnend

	.ident	"clang version 12.0.0"
	.section	".note.GNU-stack","",%progbits
	.addrsig
	.eabi_attribute	30, 6
