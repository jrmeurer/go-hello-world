package main

// #include "types.h"
import "C"
import "fmt"
import "time"

//export doSomething
func doSomething (args C.struct_go_args) C.struct_go_args {
  fmt.Println("GOLANG HELLO WORLD.")
  fmt.Println("here is the object", args)

  resultNum := 0
  channel := make(chan int)
  totalValues := 25

  // kick off a bunch of goroutines
  for i := 0; i < totalValues; i++ {
    index := i
    go func () {
      time.Sleep(time.Duration(index % 2) * time.Second)
      channel <- index
    }()
  }

  // aggregate all of the values
  // published to the channel
  count := 0
  for val := range channel {
    resultNum += val
    // close the channel after enough has been received
    if count++; count == totalValues {
      close(channel)
    }
  }

  // put the resulting data into a c struct and return it
  var result C.struct_go_args
  result.num = C.float(resultNum) + args.num
  return result
}

func main () {}