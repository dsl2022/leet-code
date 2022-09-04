var coinChange = function (coins, amount) {
  const dp = new Array(amount).fill(amount + 1);
  dp[0] = 0;
  for (let a = 1; a < dp.length + 1; a++) {
    for (coin of coins) {
      if (a - coin > 0) {
        dp[a] = Math.min(dp[a], dp[a - c] + 1);
      }
    }
  }
  return dp[amount] != amount + 1 ? dp[amount] : -1;
};
