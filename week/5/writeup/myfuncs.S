section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
<<<<<<< HEAD:week/5/myfuncs.S
        mov rcx, rdx  ;set counter for loop
        mov rax, 0    ;set index to 0
        set:
           mov byte [rdi+rax], sil ;set the array element to val
           inc rax		   ;increase the index
        loop set
=======
	mov rcx, rdx  ;set counter for loop
        mov rax, 0    ;set index to 0
        set:
           mov byte [rdi+rax], sil ;set the array element to val 
           inc rax		   ;increase the index
        loop set

>>>>>>> 12cbbca83a89e0e43ec86c70364be21b65746086:week/5/writeup/myfuncs.S

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;
	mov rcx, rdx   ;set counter for loop
       mov rax, 0      ;set index to 0
       push rbx	       ;save rbx for changing
       copy:
	  mov bl, byte [rsi+rax]	;moves a byte of rsi into bl register
          mov byte [rdi+rax], bl	;moves content of bl register into rdi
          inc rax			;increment rax register counter
       loop copy
       pop rbx	       ;restore rbx register
       

	

       mov rcx, rdx   ;set counter for loop
       mov rax, 0     ;set index to 0
       copy:
          mov byte [rdi+rax], [rsi+rax]
          inc rax
       loop copy


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
