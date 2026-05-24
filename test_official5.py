# The user said: "백금단풍잎 원리와 이해.txt 이건 운영자가 공개한 계산식인데 참고해서 다시해봐"
# If the game uses EXACTLY the official formula, then my Simul calculation should have been exact.
# BUT we saw that it was completely off!
# Why? Because in the user's mind "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# This is EXACTLY the definition of a SEQUENTIAL calculation or a RECURSIVE calculation!
# If the official formula is Simul:
# A_final = bA + bD*Cad + bH*Cah
# But the user expects: "If Defense goes up, Leaf is recalculated, and Atk/HP go up!"
# Wait. In Simul, if Defense goes up, Atk and HP DO go up!
# Because A_final = bA + bD*Cad. If bD increases, A_final increases.
# BUT, if D_final goes up, does that increase A and H?
# In Simul, Leaf is calculated from BUFFED stats (bD), not FINAL stats (D_final).
# If the user expects Leaf to be calculated from FINAL stats, then we have a recursive system!
# "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# This strongly implies that the user believes Leaf should be based on the STATS INCLUDING LEAF!
# Let's test a Fully Recursive system.
# A_final = bA + D_final * Cad + H_final * Cah
# D_final = bD + A_final * Cda + H_final * Cdh
# H_final = bH + A_final * Cha + D_final * Chd
# If this is the true equation, then we can solve for Final stats given base stats!

targetA1 = 32535511
targetD1 = 13217997
targetH1 = 293620000

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

def solve_3x3(M, Y):
    det = M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
    def get_det(M_sub):
        return M_sub[0][0]*(M_sub[1][1]*M_sub[2][2] - M_sub[1][2]*M_sub[2][1]) - M_sub[0][1]*(M_sub[1][0]*M_sub[2][2] - M_sub[1][2]*M_sub[2][0]) + M_sub[0][2]*(M_sub[1][0]*M_sub[2][1] - M_sub[1][1]*M_sub[2][0])
    M_x = [[Y[0], M[0][1], M[0][2]], [Y[1], M[1][1], M[1][2]], [Y[2], M[2][1], M[2][2]]]
    M_y = [[M[0][0], Y[0], M[0][2]], [M[1][0], Y[1], M[1][2]], [M[2][0], Y[2], M[2][2]]]
    M_z = [[M[0][0], M[0][1], Y[0]], [M[1][0], M[1][1], Y[1]], [M[2][0], M[2][1], Y[2]]]
    return get_det(M_x)/det, get_det(M_y)/det, get_det(M_z)/det

# A - D*Cad - H*Cah = bA
# -A*Cda + D - H*Cdh = bD
# -A*Cha - D*Chd + H = bH
M = [
    [1, -Cad, -Cah],
    [-Cda, 1, -Cdh],
    [-Cha, -Chd, 1]
]

A, D, H = solve_3x3(M, [bA1, bD1, bH1])
print(f"Fully Recursive 1: A={A:,.0f}, D={D:,.0f}, H={H:,.0f}")
print(f"Target 1: A={targetA1:,.0f}, D={targetD1:,.0f}, H={targetH1:,.0f}")

# Now what if "방어력(모험) 30% 적용" means bD2 = baseD * 1.71?
bD2 = baseD * 1.71
A2, D2, H2 = solve_3x3(M, [bA1, bD2, bH1])
print(f"\nFully Recursive 2 (Additive D): A={A2:,.0f}, D={D2:,.0f}, H={H2:,.0f}")

bD2_mul = baseD * 1.41 * 1.30
A2_m, D2_m, H2_m = solve_3x3(M, [bA1, bD2_mul, bH1])
print(f"Fully Recursive 2 (Multiplicative D): A={A2_m:,.0f}, D={D2_m:,.0f}, H={H2_m:,.0f}")

targetA2 = 34395421
targetD2 = 17183396
targetH2 = 306710000
print(f"Target 2: A={targetA2:,.0f}, D={targetD2:,.0f}, H={targetH2:,.0f}")

# The differences are huge!
# Fully Recursive 1: A=37,430,179, D=15,551,584, H=353,358,405
# That's way higher than Target 1 (32M, 13M, 293M).
# What if it's Sequential?
# "방어력이 올라가면 백금단풍잎 재계산되어서 공,체 올라가야하는게 맞는거야"
# This sounds like D is updated FIRST, then A and H are updated!
# This is exactly the D->H->A or D->A->H sequential logic!
