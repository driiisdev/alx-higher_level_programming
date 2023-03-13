#!/usr/bin/node
module.exports = {
  callMeMoby: function (x, theFunction) {
    let i = 0;
    while (i < x) {
      theFunction();
      i++;
    }
  }
};
