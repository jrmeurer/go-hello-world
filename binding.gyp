{
  'targets': [
    {
      'target_name': 'native-prover',
      'sources': [
        'libs/native-prover.h',
        'native-prover-addon.cc'
      ],
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
        ["OS == 'android', target_arch == 'x86'", {
            'libraries': [ '../lib/native-prover.so' ],
        }],
    ],
    }
  ]
}
