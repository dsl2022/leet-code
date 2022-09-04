function alienOrder(words) {
  const adjList = {};
  const inDegree = words.reduce((acc, params) => {
    // console.log({ params });
    for (char of params) {
      if (!acc[char]) acc[char] = 0;
    }
    return acc;
  }, {});
  const shiftWordsByOne = [...words];
  shiftWordsByOne.shift();
  console.log({ words, shiftWordsByOne });
  for (let i = 0; i < shiftWordsByOne.length; i++) {
    const first = words[i];
    const second = shiftWordsByOne[i];
    console.log({ first, second });
    let lengthRef = Math.min(first.length, second.length);
    console.log({ lengthRef });
    for (let i = 0; i < lengthRef; i++) {
      let c = first[i];
      let d = second[i];
      console.log({ c, d });
      if (c !== d) {
        if (!adjList[c]) {
          adjList[c] = new Set();
          if (!adjList[c].has(d)) {
            adjList[c].add(d);
            inDegree[d] += 1;
          }
        }
        break;
      } else {
        if (second.length < first.length) return "";
      }
    }
  }
  console.log(adjList);
  console.log(inDegree);
  const output = [];
  const queue = [];
  for (let degree in inDegree) {
    if (inDegree[degree] === 0) queue.push(degree);
  }
  console.log({ queue });
  while (queue.length > 0) {
    let c = queue.shift();
    console.log({ c });
    output.push(c);
    console.log({ output });
    console.log(adjList, c, "test adjustList");
    for (let d of adjList[c]) {
      console.log("test", { d });
      inDegree[d] -= 1;
      if (inDegree[d] === 0) {
        queue.push(d);
      }
    }
  }
}

alienOrder(["wrt", "wrf", "er", "ett", "rftt"]);
const words2 = ["wrt", "wrf", "er", "ett", "rftt"];
console.log(words2);
words2.shift();
console.log(words2);
