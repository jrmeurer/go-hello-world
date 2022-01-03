{
  'targets': [
    {
      'target_name': 'addon',
      'sources': [
        'lib/types.h',
        'lib/libgo.h',
        'addon.cc'
      ],
      'include_dirs': [ '<!(node -e \'require("nan")\')' ],
      # libraries are relative to the 'build' directory
      'libraries': [ '../lib/libgo.a' ],
      "conditions": [
        ["OS == 'android'", {
            # Add stuff.
        }],
        ["OS == 'ios'", {
            # Add stuff.
        }],
        ["target_arch == 'arm'", {
            # Add stuff.
        }]
    ],
    }
  ]
}

{
  "targets": [{
    "target_name": "test-hello-world",
    "conditions": [
      ["OS == 'linux'", {
        "cflags": [],
        "cflags!": [ "-fno-tree-vrp"]
      }],
      ["OS == 'mac'", {
        "cflags+": ["-fvisibility=hidden"],
        "xcode_settings": {
          "GCC_SYMBOLS_PRIVATE_EXTERN": "YES" # -fvisibility=hidden
        }
      }],
      ["OS == 'android'", {
        "cflags": [ "-fPIC" ],
        "ldflags": [ "-fPIC" ],
        "cflags!": [
          "-fno-tree-vrp",
          "-mfloat-abi=hard",
          "-fPIE"
        ],
        "ldflags!": [ "-fPIE" ]
      }],
      ["target_arch == 'arm'", {
        "cflags": [ "-mfloat-abi=hard" ]
      }]
    ],
    "dependencies": [
      "<(module_root_dir)/deps/leveldb/leveldb.gyp:leveldb"
    ],
    "include_dirs"  : [
      "<!(node -e \"require('napi-macros')\")"
    ],
    "sources": [
      "binding.cc"
    ]
  }]
}
