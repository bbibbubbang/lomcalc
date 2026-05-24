# The user's prompt:
# "역산 적용 안한 최종 공격력이 32535511, 최종방어력 13217997, 최종체력 2억 9362만, 공방체 각각 71%,41%,29%(백단과 공방체는 최종공격력에 이미 포함되어있음). 여기서 방어력(모험) 30% 적용 시 수치는 최종공격력 34395421, 최종방어력 17183396, 최종체력 3억 671만."
# "너 백금 단풍잎에 대해 잘못 이해하고 있는 것 같은데, 일단 스텟%는 스텟(모험)%와 곱연산되는건 맞아. 그런데 방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야. 백금단풍잎 원리와 이해.txt 이건 운영자가 공개한 계산식인데 참고해서 다시해봐."

# Oh! "스텟%는 스텟(모험)%와 곱연산되는건 맞아."
# AND there was no "모험" stat for Atk and HP in this specific prompt?
# Wait, what if the user MEANS that "공방체 각각 71%,41%,29%" IS the Equip % + Adv % COMBINED? No.
# If "스텟%는 스텟(모험)%와 곱연산되는건 맞아", then IF they had 30% Adv Def,
# bD2 = BaseD * (1 + 0.41) * (1 + 0.30) = BaseD * 1.41 * 1.30 = BaseD * 1.833!
# Let's check this!!
baseD = 7519881
bD1 = baseD * 1.41
bD2 = baseD * 1.41 * 1.30
print(f"bD1 = {bD1:,.0f}")
print(f"bD2 = {bD2:,.0f}")
# bD1 = 10,603,032
# bD2 = 13,783,942

# If this is true, then how did Final Defense go from 13,217,997 to 17,183,396?
# TargetD1 = bD1 + LeafD1 => LeafD1 = 13,217,997 - 10,603,032 = 2,614,965
# TargetD2 = bD2 + LeafD2 => LeafD2 = 17,183,396 - 13,783,942 = 3,399,454

# Is LeafD2 / LeafD1 exactly 1.30?
print(f"LeafD2 / LeafD1 = {3399454 / 2614965:.4f}")
# YES! It's EXACTLY 1.3000!
# WOW!!!!

# This means the LEAF ITSELF was multiplied by 1.30!
# Why would Leaf D be multiplied by 1.30?
# Leaf D = Base A * Cda + Base H * Cdh.
# Base A and Base H DID NOT CHANGE!
# So Leaf D should be constant!
# Why did Leaf D get multiplied by 1.30?
# BECAUSE THE ENTIRE FINAL STAT WAS MULTIPLIED BY 1.30!
# TargetD2 = TargetD1 * 1.30 = 13,217,997 * 1.30 = 17,183,396.1
# The game calculated Final D, and THEN multiplied it by 1.30 (because Equip * Adv = 1.41 * 1.30, but the game mistakenly multiplied the ENTIRE Final Stat by 1.30 instead of just the Base Stat!).
# Let's tell the user this!

# Now, why did A and H go up?
# Because the game then RECALCULATED Leaf A and Leaf H using the NEW Final D!
# New Final D = 17,183,396.
# Old Final D = 13,217,997.
# Delta D = 3,965,399.
# Delta H = Delta D * Chd = 3,965,399 * 2.80 = 11,103,117.
# But Delta H = 13,090,000.
# Why the extra 1.178 multiplier?
# What is the Equip % for H? 29%. (1.29 multiplier).
# What is the Equip % for A? 71%. (1.71 multiplier).

# If Delta H = (Delta D * Chd) * 1.18 ...
# Wait. What if Delta H = Delta D * Chd * (1 + something)?
# We'll explain that the base cause is the multiplication of the ENTIRE defense by 1.3, which then recursively updates A and H.
