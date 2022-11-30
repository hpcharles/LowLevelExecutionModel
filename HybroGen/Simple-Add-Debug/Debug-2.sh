riscv32-unknown-elf-gdb Add-With-Specialization
GNU gdb (GDB) 9.2
../..
(gdb) target remote :7777
(gdb) break main
Breakpoint 1 at 0x107c6: file Add-With-Specialization.c, line 201.
(gdb) c
Continuing.
Breakpoint 1, main (argc=3, argv=0x40800374) at Add-With-Specialization.c:201
201	  if (argc < 3)
(gdb) n
206	  in0  = atoi (argv[1]);   // Get the users values in1 & in2
211	  fPtr = (pifi) genAdd (ptr, in0); // Generate instructions
(gdb)
212	  res  = fPtr(in1);  // Call generated code
(gdb) x/4i fPtr
   0x19008:	ori	t1,zero,3
   0x1900c:	add	t0,t1,a0
   0x19010:	mv	a0,t0
   0x19014:	ret
(gdb)
