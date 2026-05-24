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

# If TargetD2 = TargetD1 * 1.30:
print(f"Target D2 / Target D1 = {targetD2 / targetD1:.4f}")
# This is EXACTLY 1.30.
# So we know for a fact that "방어력(모험) 30%" acts as a multiplier of 1.30 on the ENTIRE Final Defense.
# FinalD2 = FinalD1 * 1.30

# The user is telling me that in the game: "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# This means: The game first calculated Final D1.
# Then, the 30% buff is applied, making Final D2 = 17,183,396.
# Because Final Defense changed, the game RECALCULATES the Leaf for Atk and HP using the NEW Final Defense!
# Wait!
# Let's check this EXACTLY!
# If Leaf for A and H uses the FINAL D instead of bD?
# TargetA1 = bA1 + FinalD1 * Cad + FinalH1 * Cah ???
# Let's see:
A1_calc = bA1 + targetD1 * Cad + targetH1 * Cah
D1_calc = bD1 + targetA1 * Cda + targetH1 * Cdh
H1_calc = bH1 + targetA1 * Cha + targetD1 * Chd

print(f"Recursive check 1:")
print(f"A={A1_calc:,.0f} (Target={targetA1:,.0f})")
print(f"D={D1_calc:,.0f} (Target={targetD1:,.0f})")
print(f"H={H1_calc:,.0f} (Target={targetH1:,.0f})")

# Wait!
# Recursive check 1:
# A=30,927,859 (Target=32,535,511)
# D=12,491,694 (Target=13,217,997)
# H=280,056,262 (Target=293,620,000)
# It doesn't match perfectly.

# What if Leaf uses (bD + FinalD_from_other_stats) ?
# What if it's Sequential on the *Buffed* stats, but we add an extra step?
# Let's check the Delta again.
DeltaA = targetA2 - targetA1 # 1,859,910
DeltaD = targetD2 - targetD1 # 3,965,399
DeltaH = targetH2 - targetH1 # 13,090,000

# If Delta H is recalculated from Delta D:
# deltaH = DeltaD * Chd = 3,965,399 * 2.80 = 11,103,117
# But Target Delta H = 13,090,000.
# Why is there a difference of 1,986,883 ?
# Wait! In Case 1, H = 293,620,000.
# What if the difference is DeltaA * Cha?
# DeltaA = 1,859,910. 1,859,910 * 0.60 = 1,115,946.
# 11,103,117 + 1,115,946 = 12,219,063. Still not 13,090,000.
