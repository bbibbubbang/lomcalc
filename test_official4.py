targetA1 = 32535511
targetD1 = 13217997
targetH1 = 293620000

Cad = 0.36
Cah = 0.004
Cda = 0.04
Cdh = 0.002
Cha = 0.60
Chd = 2.80

def solve_3x3(M, Y):
    # Cramer's rule
    det = M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])

    def get_det(M_sub):
        return M_sub[0][0]*(M_sub[1][1]*M_sub[2][2] - M_sub[1][2]*M_sub[2][1]) - M_sub[0][1]*(M_sub[1][0]*M_sub[2][2] - M_sub[1][2]*M_sub[2][0]) + M_sub[0][2]*(M_sub[1][0]*M_sub[2][1] - M_sub[1][1]*M_sub[2][0])

    M_x = [[Y[0], M[0][1], M[0][2]], [Y[1], M[1][1], M[1][2]], [Y[2], M[2][1], M[2][2]]]
    M_y = [[M[0][0], Y[0], M[0][2]], [M[1][0], Y[1], M[1][2]], [M[2][0], Y[2], M[2][2]]]
    M_z = [[M[0][0], M[0][1], Y[0]], [M[1][0], M[1][1], Y[1]], [M[2][0], M[2][1], Y[2]]]

    return get_det(M_x)/det, get_det(M_y)/det, get_det(M_z)/det

M = [
    [1, Cad, Cah],
    [Cda, 1, Cdh],
    [Cha, Chd, 1]
]

bA, bD, bH = solve_3x3(M, [targetA1, targetD1, targetH1])
print(f"Inferred Buffed Stats: A={bA:,.0f}, D={bD:,.0f}, H={bH:,.0f}")

baseA_inf = bA / 1.71
baseD_inf = bD / 1.41
baseH_inf = bH / 1.29

print(f"Inferred Base Stats: A={baseA_inf:,.0f}, D={baseD_inf:,.0f}, H={baseH_inf:,.0f}")
print(f"Original Base Stats: A={14616907:,.0f}, D={7519881:,.0f}, H={173197335:,.0f}")
