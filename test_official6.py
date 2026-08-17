# Look at the Fully Recursive Output!
# Fully Recursive 1: A=30,556,709, D=12,378,135, H=276,417,367
# This is STILL lower than the target.
# Wait! In the official text:
# "공격력 : (1000x1.3) + (500x1.1x0.03) = 1300 + 16.5 = 1316.5"
# Here, Leaf D to A is calculated from (500x1.1).
# 500x1.1 is exactly the BUFFED Defense. NOT the Final Defense!
# The official calculation is SIMULTANEOUS!
# "공방체% 연산을 먼저 적용한 이후 계산됩니다"
# Yes, it uses the buffed stats (after %).
# My simul calc: A_sim = bA1 + bD1 * Cad + bH1 * Cah = 29,705,701.

# The user observes 32,535,511.
# They claim: "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# This implies that the user THINKS it should be recursive or sequential.
# But the OFFICIAL documentation says it's Simul!
# And the observed Target numbers are MUCH HIGHER than Simul.

# So the bug in the game must be producing these higher numbers.
# We found that `Leaf(Buffed) + Leaf(Base)` gave A=33.4M, D=13.4M, H=297M. (Close).
# What if it's `Simul Leaf * X` ?
# To get from 29,705,701 to 32,535,511.
# Leaf A = 4,710,790.
# bA1 = 24,994,911.
# 24,994,911 + 4,710,790 * X = 32,535,511 => 4,710,790 * X = 7,540,600 => X = 1.60.
# Leaf D = 1,446,646.
# bD1 = 10,603,032.
# 10,603,032 + 1,446,646 * X = 13,217,997 => 1,446,646 * X = 2,614,965 => X = 1.80.
# Leaf H = 44,685,436.
# bH1 = 223,424,562.
# 223,424,562 + 44,685,436 * X = 293,620,000 => 44,685,436 * X = 70,195,438 => X = 1.57.

# As shown before, there is NO constant multiplier X.

# Wait... what if we look at the user's base stats again.
# Are we 100% sure that base stats are: 14616907, 7519881, 173197335?
# Yes, user said "이번엔 이 공방체 조건으로"

# What if "스텟(모험)%와 곱연산되는건 맞아" means:
# Equip_Pct * Adv_Pct ?
# In Case 1: 71%, 41%, 29%.
# IF these were BOTH Equip and Adv?
# "공방체 각각 71%,41%,29% (백단과 공방체는 최종공격력에 이미 포함되어있음)"
# What if this means Equip = 71, Adv = 71? No.
# Maybe "공방체(모험) 33%" FROM THE FIRST PROMPT is STILL APPLIED in Case 1?
# User: "방어력(모험) 30% 적용 시 수치는"
# This implies an EXTRA 30% on defense.
# Let's test with the 33% Adv included in Case 1!
targetA1 = 32535511
targetD1 = 13217997
targetH1 = 293620000

targetA2 = 34395421
targetD2 = 17183396
targetH2 = 306710000

baseA = 14616907
baseD = 7519881
baseH = 173197335

Cad = 0.36; Cah = 0.004; Cda = 0.04; Cdh = 0.002; Cha = 0.60; Chd = 2.80

bA1_adv = baseA * 1.71 * 1.33
bD1_adv = baseD * 1.41 * 1.33
bH1_adv = baseH * 1.29 * 1.33

bD2_adv = baseD * 1.41 * 1.33 * 1.30

# What is Simul with this?
A_s = bA1_adv + bD1_adv * Cad + bH1_adv * Cah
D_s = bD1_adv + bA1_adv * Cda + bH1_adv * Cdh
H_s = bH1_adv + bA1_adv * Cha + bD1_adv * Chd
print(f"Simul Adv: A={A_s:,.0f}, D={D_s:,.0f}, H={H_s:,.0f}")
# A=38.6M, D=15.6M, H=348M.
# This is WAY HIGHER than target! (Target A=32.5M, D=13.2M, H=293M).
# So the 33% is NOT applied!

# Let's test "Add Adv" instead of "Multiply Adv"
bA1_add = baseA * (1 + 0.71 + 0.33)
bD1_add = baseD * (1 + 0.41 + 0.33)
bH1_add = baseH * (1 + 0.29 + 0.33)

bD2_add = baseD * (1 + 0.41 + 0.33 + 0.30)

A_a = bA1_add + bD1_add * Cad + bH1_add * Cah
D_a = bD1_add + bA1_add * Cda + bH1_add * Cdh
H_a = bH1_add + bA1_add * Cha + bD1_add * Chd
print(f"Simul Add: A={A_a:,.0f}, D={D_a:,.0f}, H={H_a:,.0f}")
# A=35.6M, D=14.8M, H=335M.
# Still higher than target.

# Therefore, in Case 1, the user DID NOT INCLUDE the 33% "모험" stat. They only have the 71, 41, 29.
