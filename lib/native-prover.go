package main

// #include "types.h"
import "C"

//export Prove
func Prove (args C.struct_go_args) *C.char {

  return C.CString("Here is the PROOF result")
}

func main () {}