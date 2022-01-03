{
  'targets': [
    {
      'target_name': 'native-prover',
      'sources': [
        'lib/types.h',
        'lib/native-prover.h',
        'native-prover-addon.cc'
      ],
      'libraries': [ '../lib/native-prover.a' ],
      'include_dirs': [
        '<!(node -e \'require("nan")\')',
        '/usr/local/include/node/'
      ],
      "conditions": [
        ["OS == 'linux'", {
            'libraries': [ '../lib/native-prover.a' ],
            # 'sources+': [ '../lib/native-prover.h' ],
        }],
        ["OS == 'mac'", {
            'libraries': [ '../lib/native-prover.a' ],
            # 'sources+': [ '../lib/native-prover.h' ],
        }],
        ["OS == 'android', target_arch == 'x86'", {
            'libraries': [ '../lib/native-prover.so' ],
        }],
        ["OS == 'android', target_arch == 'arm'", {
            'libraries': [ '../lib/native-prover.so' ],
        }],
    ],
    }
  ]
}
