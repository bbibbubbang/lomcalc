targetA1 = 32535511
targetD1 = 13217997
targetH1 = 293620000

targetA2 = 34395421
targetD2 = 17183396
targetH2 = 306710000

baseA = 14616907
baseD = 7519881
baseH = 173197335

Cad = 0.36
Cah = 0.004
Cda = 0.04
Cdh = 0.002
Cha = 0.60
Chd = 2.80

bA1 = baseA * 1.71
bD1 = baseD * 1.41
bH1 = baseH * 1.29

print("The user said: '스텟%는 스텟(모험)%와 곱연산되는건 맞아. 그런데 방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야. 백금단풍잎 원리와 이해.txt 이건 운영자가 공개한 계산식인데 참고해서 다시해봐.'")

# The user is telling me that the TARGET values are what THEY observe, and they WANT me to figure out HOW it's calculated.
# Wait. Look at the Official calculation:
# 공격력 : (1000x1.3) + (500x1.1x0.03)
# Here, BaseA=1000, BaseD=500.
# Atk%=30%, Def%=10%.
# Leaf: Def to Atk = +3 per 100 -> 0.03.
# The calculation is exactly: bA + bD * 0.03.
# This means the Leaf uses the BUFFED stats (bD = 500 * 1.1) to calculate the bonus.
# And it's simultaneous.

# But the user's TARGET stats don't match this!
# A1_sim = bA1 + bD1 * Cad + bH1 * Cah = 29,705,701 (Target 32,535,511).
# If the game uses the official logic, it should be 29.7M.
# Why is it 32.5M?
# Are we sure baseA is 14,616,907?
# "최종 공격력이 32535511 ... 공방체 각각 71%,41%,29%"
# IF base stats were higher?
# What if the user had OTHER buffs?

# Let's reverse engineer BaseA, BaseD, BaseH from TargetA1, TargetD1, TargetH1 assuming the OFFICIAL logic!
# System of equations:
# A = bA + bD * Cad + bH * Cah
# D = bD + bA * Cda + bH * Cdh
# H = bH + bA * Cha + bD * Chd
# We know A = 32,535,511, D = 13,217,997, H = 293,620,000.
# Let's solve for bA, bD, bH.

import numpy as np

M = np.array([
    [1, Cad, Cah],
    [Cda, 1, Cdh],
    [Cha, Chd, 1]
])

target = np.array([targetA1, targetD1, targetH1])

b_vals = np.linalg.solve(M, target)
bA, bD, bH = b_vals
print(f"Inferred Buffed Stats: A={bA:,.0f}, D={bD:,.0f}, H={bH:,.0f}")

# From these inferred buffed stats, what are the Base stats?
# baseA = bA / 1.71
# baseD = bD / 1.41
# baseH = bH / 1.29
baseA_inf = bA / 1.71
baseD_inf = bD / 1.41
baseH_inf = bH / 1.29

print(f"Inferred Base Stats: A={baseA_inf:,.0f}, D={baseD_inf:,.0f}, H={baseH_inf:,.0f}")
print(f"Original Base Stats: A={14616907:,.0f}, D={7519881:,.0f}, H={173197335:,.0f}")

# Look at this!
# Inferred Base Stats are NOT 14.6M, 7.5M, 173M.
# They are completely different? No, wait.
