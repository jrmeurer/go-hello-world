#include <node.h>
#include "lib/native-prover.h"
#include "lib/types.h"

#include <cstring>

using v8::FunctionCallbackInfo;
using v8::Isolate;
using v8::Local;
using v8::Object;
using v8::String;
using v8::Value;
using v8::Promise;

void NativeProve (const FunctionCallbackInfo<Value> &args) {
  Isolate *isolate = args.GetIsolate();

  // Create char* (for C) from C++ String.
  String::Utf8Value s(isolate, args[0]);
  std::string inputStr(*s);
  char *input = const_cast<char*>(inputStr.c_str());

  // Parse arguments into Go object.
  NativeProverArgs goArgs;
  goArgs.input = input;

  // Call exported Go "PROVE" function, which returns a C string.
  char *result = Prove(goArgs);

  // Return the value.
  args.GetReturnValue().Set(String::NewFromUtf8(isolate, result));
  delete result;
}

void Init (Local<Object> exports) {
  NODE_SET_METHOD(exports, "prove", NativeProve);
}

NODE_MODULE(nativeProverAddon, Init)
