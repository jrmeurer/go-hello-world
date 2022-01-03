const addon = require('bindings')('addon');

const testObject = {
  num: 1.243,
};

addon.doSomethingAsync(testObject).then((res) => {
  console.log(`promise result:\n  result: ${JSON.stringify(res)}`);
});
