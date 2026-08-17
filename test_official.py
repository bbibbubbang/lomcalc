targetA1 = 32535511
targetD1 = 13217997
targetH1 = 293620000

targetA2 = 34395421
targetD2 = 17183396
targetH2 = 306710000

baseA = 14616907
baseD = 7519881
baseH = 173197335

Cad = 9 * 4 / 100      # 0.36
Cah = 2 * 2 / 1000     # 0.004
Cda = 4 * 1 / 100      # 0.04
Cdh = 2 * 1 / 1000     # 0.002
Cha = 3 * 20 / 100     # 0.60
Chd = 7 * 40 / 100     # 2.80

# The user explicitly told me:
# "스텟%는 스텟(모험)%와 곱연산되는건 맞아."
# So Base * (1 + EquipPct) * (1 + AdvPct)

# Case 1: 71%, 41%, 29%
# Since there is NO adventure stats mentioned initially, maybe it's just Base * (1+EquipPct)
bA1 = baseA * 1.71
bD1 = baseD * 1.41
bH1 = baseH * 1.29

# The official doc says:
# "백금 단풍잎 능력치는 공방체% 연산을 먼저 적용한 이후 계산됩니다. 아래의 예제 계산식을 확인해주세요."
# "공격력 : (1000x1.3) + (500x1.1x0.03)"
# This is EXACTLY SIMULTANEOUS CALCULATION!
# A_final = bA + bD * Cad + bH * Cah
# This means my initial assumption was exactly how the game is SUPPOSED to work.

# But the user says: "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야."
# In simultaneous calculation, yes: if bD goes up, then bD * Cad increases A, and bD * Chd increases H.
# So D increasing SHOULD naturally increase A and H.

print("--- Let's recalculate based on the official logic ---")

# Let's check Case 1 again. The user says target is A=32,535,511, D=13,217,997, H=293,620,000.
# If I just use standard simultaneous:
A_sim = bA1 + bD1 * Cad + bH1 * Cah
D_sim = bD1 + bA1 * Cda + bH1 * Cdh
H_sim = bH1 + bA1 * Cha + bD1 * Chd
print(f"Simul 1: A={A_sim:,.0f}, D={D_sim:,.0f}, H={H_sim:,.0f}")
print(f"Target 1: A={targetA1:,.0f}, D={targetD1:,.0f}, H={targetH1:,.0f}")
# Simul 1: A=29,705,701, D=12,049,678, H=268,109,999.
# It is OFF. By 2.8M, 1.2M, 25M.
# Why?
# "백단과 공방체는 최종공격력에 이미 포함되어있음"
# Does this mean the user GAVE me the final stats (32,535,511) and IS ASKING WHY it's 32.5M when it should be 29.7M?
# No, "최종 공격력이 32535511... 여기서 방어력(모험) 30% 적용 시 수치는 어떻게 계산되면 저렇게 나오는지"
# "최종공격력이 32535511 ... 이렇게 나오는지."

# The user is asking how the CALCULATION yields the target numbers.
# "여기서 방어력(모험) 30% 적용 시 수치는 최종공격력 34395421 ... 이렇게 나오는지"
# Ah, Case 2: bD2 = bD1 * 1.30 ? Because "스텟%는 스텟(모험)%와 곱연산되는건 맞아".
bD2 = baseD * 1.41 * 1.30

A_sim2 = bA1 + bD2 * Cad + bH1 * Cah
D_sim2 = bD2 + bA1 * Cda + bH1 * Cdh
H_sim2 = bH1 + bA1 * Cha + bD2 * Chd
print(f"Simul 2: A={A_sim2:,.0f}, D={D_sim2:,.0f}, H={H_sim2:,.0f}")
print(f"Target 2: A={targetA2:,.0f}, D={targetD2:,.0f}, H={targetH2:,.0f}")

# Simul 2: A=30,851,844, D=15,230,587, H=277,015,930
# Target 2: A=34,395,421, D=17,183,396, H=306,710,000

# Let's look at the Deltas:
print("\n--- DELTAS ---")
print(f"Simul Delta A: {A_sim2 - A_sim:,.0f}")
print(f"Simul Delta D: {D_sim2 - D_sim:,.0f}")
print(f"Simul Delta H: {H_sim2 - H_sim:,.0f}")
print(f"Target Delta A: {targetA2 - targetA1:,.0f}")
print(f"Target Delta D: {targetD2 - targetD1:,.0f}")
print(f"Target Delta H: {targetH2 - targetH1:,.0f}")
