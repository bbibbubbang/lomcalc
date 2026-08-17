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

bD2 = baseD * 1.41 * 1.30

# The user is saying:
# 1. Equip% * Adv% is correct.
# 2. Def going up -> recalculate Leaf -> A and H go up is correct.
# 3. But the values are HIGHER than the official Simul logic.
# So there MUST be a multiplier or an extra term!

# Look at the Deltas:
# Target Delta D = 3,965,399. Simul Delta D = 3,180,910.
# 3,965,399 / 3,180,910 = 1.2466

# Target Delta H = 13,090,000. Simul Delta H = 8,906,547.
# 13,090,000 / 8,906,547 = 1.4697

# Target Delta A = 1,859,910. Simul Delta A = 1,145,127.
# 1,859,910 / 1,145,127 = 1.6242

# None of these match.
# But what if the user's base stats ALREADY included something?
# "역산 적용 안한 최종 공격력이 32535511... 여기서 방어력(모험) 30% 적용 시"
# What if target A1 is baseA * 1.71 * 1.33 ? The user DID say "공방체(모험) 33%" in the first prompt!
# Let's read carefully:
# "역산 적용 안한 최종 공격력이 32535511... 공방체 각각 71%,41%,29%(백단과 공방체는 최종공격력에 이미 포함되어있음). 여기서 방어력(모험) 30% 적용 시 수치는..."
# "공방체 각각 71%, 41%, 29%" ONLY. There is no 33% here!

# Let's find IF there is an extra buff.
# A1_sim = 29,705,701
# Target A1 = 32,535,511
# Ratio = 32,535,511 / 29,705,701 = 1.095

# What if "모험" was applied as an EXTRA loop?
# The user's text: "백금단풍잎 원리와 이해.txt 이건 운영자가 공개한 계산식인데 참고해서 다시해봐"
# If the game uses the formula in the TXT file, then the game SHOULD produce the Simul results.
# But it produces the Target results.
# This means there's a BUG in how the game implements the official formula!

# How can we produce the Target Deltas exactly?
# We have Delta bD = 3,180,910.
# The game produces Delta D = 3,965,399.
# The difference is 3,965,399 - 3,180,910 = 784,489.
# Where does 784,489 come from?
# Delta Leaf D = 784,489.
# But Delta Leaf D = Delta bA * Cda + Delta bH * Cdh.
# Since Delta bA = 0 and Delta bH = 0, Delta Leaf D SHOULD BE ZERO!
# Why did Leaf D change if base A and base H didn't change?
# Only one explanation: LEAF D IS CALCULATED FROM FINAL H OR FINAL A!
# If Leaf D = Final A * Cda + Final H * Cdh.
# Then Delta Leaf D = Delta Final A * Cda + Delta Final H * Cdh.
# Let's check this!
delta_final_A = 1,859,910
delta_final_H = 13,090,000

calc_delta_leaf_D = delta_final_A * Cda + delta_final_H * Cdh
print(f"Calculated Delta Leaf D = {calc_delta_leaf_D:,.0f} (Needed: 784,489)")
# 1,859,910 * 0.04 + 13,090,000 * 0.002 = 74,396 + 26,180 = 100,576.
# 100,576 != 784,489.
# So even if it used Final A and Final H, it only adds 100k, not 784k.

# What else could cause Defense to jump by 3.96M when bD only jumped by 3.18M?
# What if the 30% is multiplied to the FINAL Defense?
# TargetD1 = 13,217,997. TargetD1 * 0.30 = 3,965,399!
# This is EXACTLY the Delta D!
# I found this before! 13,217,997 * 0.30 = 3,965,399.1.
# So the 30% 방어력(모험) is DEFINITELY a 30% multiplier on the FINAL DEFENSE.
