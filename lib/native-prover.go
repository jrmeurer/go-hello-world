package main

// #include "types.h"
import "C"

//export Prove
func Prove (args C.struct_native_prover_args) *C.char {
  return C.CString("Here is the PROOF result")
}

func main () {}