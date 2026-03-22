sed -i "s/baseHitMulti: 0/baseHitMulti: 1/g" index.html
sed -i "s/eqStats.baseHitMulti += effectiveValue/eqStats.baseHitMulti *= effectiveValue/g" index.html
sed -i "s/intervalEqStats.baseHitMulti += effectiveValue/intervalEqStats.baseHitMulti *= effectiveValue/g" index.html
sed -i "s/let iHitMulti = intervalEqStats.baseHitMulti > 0 ? intervalEqStats.baseHitMulti : 1;/let iHitMulti = intervalEqStats.baseHitMulti;/g" index.html
