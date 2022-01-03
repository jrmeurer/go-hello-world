const np = require('bindings')('native-prover');

const testProve = async () => {
  const input = 'some input text as a string';
  const res = np.prove(input);
  console.log(`\nResult: \n${JSON.stringify(res)}`);
};

testProve();
