#!/usr/bin/node
/* Task 7 - Write a function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let noccur = 0;
  for (const item of list) {
    if (item === searchElement) {
      noccur++;
    }
  }
  return noccur;
};
