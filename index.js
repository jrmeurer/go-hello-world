const np = require('bindings')('native-prover');

const testProve = async () => {
  const testObject = {
    num: 1.243,
  };
  const res = await np.prove(testObject);
  console.log(`promise result:\n  result: ${JSON.stringify(res)}`);
};
testProve();
