function findValidHand(cards) {
  suits = {};
  for (card of cards) {
    if (!suits[card[0]]) {
      suits[card[0]] = [];
      suits[card[0]].push(card.slice(1));
    } else {
      suits[card[0]].push(card.slice(1));
    }
  }
  console.log(suits);
}

findValidHand(["+AA", "-AA", "+AA", "-C", "-B", "+AA", "-AAA", "-A", "=AA"]);
