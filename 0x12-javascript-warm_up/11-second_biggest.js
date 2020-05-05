#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let fbig, sbig;
  if (parseInt(process.argv[2]) >= parseInt(process.argv[3])) {
    fbig = parseInt(process.argv[2]);
    sbig = parseInt(process.argv[3]);
  } else {
    fbig = parseInt(process.argv[3]);
    sbig = parseInt(process.argv[2]);
  }

  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > fbig) {
      sbig = fbig;
      fbig = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > sbig) {
      sbig = parseInt(process.argv[i]);
    }
  }
  console.log(sbig);
}
