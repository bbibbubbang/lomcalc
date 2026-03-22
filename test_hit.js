// If another item adds "기본 타수(배) +3", effectiveValue = 3
let effectiveValue2 = 3;
let eqStats2 = { baseHitMulti: 1 };
eqStats2.baseHitMulti *= 2;
eqStats2.baseHitMulti *= 3;
console.log("baseHitMulti multiple =", eqStats2.baseHitMulti);
