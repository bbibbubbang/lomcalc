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

# What if Leaf is calculated from Base stats + Leaf?
# Or what if we solve for the exact multipliers?
# TargetA1 = bA1 + x * lA
# TargetD1 = bD1 + x * lD
# TargetH1 = bH1 + x * lH
# lA = bD1 * Cad + bH1 * Cah = 10,603,032 * 0.36 + 223,424,562 * 0.004 = 3,817,091 + 893,698 = 4,710,790
lA = bD1 * Cad + bH1 * Cah
lD = bA1 * Cda + bH1 * Cdh
lH = bA1 * Cha + bD1 * Chd

print(f"Target A1 = {targetA1}, bA1 = {bA1}, lA = {lA}")
print(f"X_A = {(targetA1 - bA1) / lA:.4f}")
print(f"X_D = {(targetD1 - bD1) / lD:.4f}")
print(f"X_H = {(targetH1 - bH1) / lH:.4f}")

# Wait, X_A = 1.60, X_D = 1.81, X_H = 1.57.
# What if it's (1 + EquipPct)?
# EquipA = 0.71 -> 1.71 (Close to 1.60)
# EquipD = 0.41 -> 1.41 (Not close to 1.81)
# EquipH = 0.29 -> 1.29 (Not close to 1.57)

# What if Leaf uses the FULL Recursive logic, AND there's a multiplier?
# The user's exact wording: "백단과 공방체는 최종공격력에 이미 포함되어있음".
# In Korean, "공방체 각각 71%,41%,29% (백단과 공방체는 최종공격력에 이미 포함되어있음)"
# This means: The target values (32535511) are the FINAL values shown on screen, which already have the 71% and Platinum Leaf applied.
# It doesn't mean they multiply each other in a specific way, just that they are included.

# Let's revisit the user's previous statement:
# "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# Yes! The user expects a SEQUENTIAL calculation. If Defense is buffed (by 30%), it should INCREASE the Platinum Leaf for Attack and HP.
# And indeed, Target A and Target H DID go up in Case 2!
# But by HOW MUCH?
# Delta A = 1,859,910
# Delta H = 13,090,000

# The user thinks this is CORRECT behavior. "올라가야하는게 맞는거야" (It is correct that it goes up).
# "백금단풍잎 원리와 이해.txt 이건 운영자가 공개한 계산식인데 참고해서 다시해봐"
# If the user believes that the official calculation naturally leads to this...
# But in the official simultaneous calculation, if you apply 30% to Defense as a FINAL MULTIPLIER, the Leaf is calculated BEFORE the final multiplier!
# So Leaf SHOULD NOT CHANGE!
# Wait. Is the 30% a final multiplier?
# If bD2 = baseD * (1.41 + 0.30) = baseD * 1.71.
# Then TargetD2 SHOULD be:
# D2 = baseD * 1.71 + Leaf_D
# Let's check TargetD2 - baseD * 1.71 = 17,183,396 - 12,858,996 = 4,324,400.
# In Case 1: TargetD1 - baseD * 1.41 = 13,217,997 - 10,603,032 = 2,614,965.
# If it's additive (41% + 30% = 71%), Leaf D jumped from 2.6M to 4.3M.
# Why would Leaf D jump if Base A and Base H didn't change?
# Ah! Because Leaf D = Base A * Cda + Base H * Cdh.
# Since Base A and Base H didn't change, Leaf D SHOULD BE EXACTLY THE SAME!
# BUT Leaf D jumped from 2.6M to 4.3M.
# THIS PROVES that Defense is NOT 1.41 -> 1.71.
# The 30% MUST BE A MULTIPLIER ON THE FINAL STAT. 13,217,997 * 1.30 = 17,183,396.

# So, if 30% is a multiplier on the final stat, why did A and H go up?
# Because the game is buggy and recalculates Leaf A and Leaf H using the FINAL Defense!
# Let's calculate Leaf A and Leaf H using Final Defense:
# Delta H = Delta Final D * Chd = 3,965,399 * 2.80 = 11,103,117.
# Target Delta H = 13,090,000.
# There is a 1.178 multiplier on Delta H.
# Why is there a 1.178 multiplier on Delta H?
# What is 1.178? 1 + 0.178?
# What is TargetH1 / baseH ? 293,620,000 / 173,197,335 = 1.695.
# What is bH1 / baseH ? 1.29.
