package main

// #include "types.h"
import "C"
import "fmt"

//export Prove
func Prove (args C.struct_native_prover_args) *C.char {
  input := C.GoString(args.input)

  fmt.Println("GOLANG NATIVE PROVER: ", input)

  return C.CString("Here is the PROOF result")
}

func main () {}