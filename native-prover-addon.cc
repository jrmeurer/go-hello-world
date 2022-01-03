#include <node.h>
#include "lib/native-prover.h"
#include "lib/types.h"

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Object;
using v8::String;
using v8::Value;
using v8::Promise;

void NativeProve (const FunctionCallbackInfo<String> &info) {
  Isolate *isolate = info.GetIsolate();

  // Parse arguments into Go object.
  NativeProverArgs args;
  args.input = info[0];

  // Call exported Go function, which returns a C string.
  char *c = Prove(args);

  // Return the value.
  args.GetReturnValue().Set(String::NewFromUtf8(isolate, c));
  delete c;
}

void Init (Local<Object> exports) {
  NODE_SET_METHOD(exports, "prove", NativeProve);
}
NODE_MODULE(myGoAddon, Init)
