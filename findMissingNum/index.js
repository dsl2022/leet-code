var findDuplicate = function (nums) {
  for (const value of nums) {
    const absValue = Math.abs(value);
    if (nums[absValue - 1] < 0) return absValue;
    nums[absValue - 1] *= -1;
  }
  return -1;
};

console.log(findDuplicate([1, 3, 4, 2, 2]));
