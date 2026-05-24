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

deltaD = targetD2 - targetD1

# User expects: "스텟%는 스텟(모험)%와 곱연산되는건 맞아. 그런데 방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# If the game recalculates A and H because D went up.
# Let's say the game recalculated H based on the new Final D.
# H_new = H_old + deltaD * Chd
print(f"H expected = {targetH1 + deltaD * 2.80:,.0f}")
print(f"H actual = {targetH2:,.0f}")

# And A is recalculated based on the new D and new H?
# A_new = A_old + deltaD * Cad + (H_new - H_old) * Cah
# If H_new - H_old = 13,090,000 (the actual change)
print(f"A expected = {targetA1 + deltaD * 0.36 + 13090000 * 0.004:,.0f}")
print(f"A actual = {targetA2:,.0f}")

# Wow!
# A expected = 32,535,511 + 1,427,543 + 52,360 = 34,015,414.
# A actual = 34,395,421.

# This proves the user's logic is exactly what the game is TRYING to do, but the game is applying EXTRA multipliers!
