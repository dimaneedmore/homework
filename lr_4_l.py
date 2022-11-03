def is_reflexive(matrix):
    for r in range(0, len(matrix)):
        if matrix[r][r] != 1:
            return False
    return True


def is_transitive(rel):
    seconds_elements = {b for (a, b) in rel}
    for (a, b) in rel:
        for c in seconds_elements:
            if (b, c) in rel and (a, c) not in rel:
                return False
    return True


def is_simetrical(rel):
    for (a, b) in rel:
        if (a, b) and (b, a) not in rel:
            return False
    return True


def is_anti_simetrical(rel):
    pass


def equ_rel(matrix, ra):
    ref = is_reflexive(matrix)
    tra = is_transitive(ra)
    sim = is_simetrical(ra)
    if ref and tra and sim:
        return True
    return False


def par_ord(matrix, ra):
    ref = is_reflexive(matrix)
    tra = is_transitive(ra)
    an_sim = is_anti_simetrical(ra)
    if ref and tra and an_sim:
        return True
    return False



matrix = [[0, 1, 0, 0, 1],
          [1, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1],
          [1, 0, 0, 1, 1]]
ra = []
for r in range(0, len(matrix)):
    for s in range(0, len(matrix[0])):
        if matrix[r][s] == 1:
            ra.append((r+1, s+1))

print(ra)
print(f"-"*80,
      "\n--refl-", is_reflexive(matrix),
      "\n--tran-", is_transitive(ra),
      "\n--sime-", is_simetrical(ra),
      "\nequ rel", equ_rel(matrix, ra))

print(f"-"*80,
      "\n--refl---", is_reflexive(matrix),
      "\n--tran---", is_transitive(ra),
      "\nan sim---", is_anti_simetrical(ra),
      "\npar order", equ_rel(matrix, ra))

print(f"-"*80,
      "\n--refl-", is_reflexive(matrix),
      "\n--tran-", is_transitive(ra),
      "\nan sim", is_anti_simetrical(ra),
      "\nequ rel", equ_rel(matrix, ra))

print(f"-"*80,
      "\n--refl-", is_reflexive(matrix),
      "\n--tran-", is_transitive(ra),
      "\nan sim", is_anti_simetrical(ra),
      "\nequ rel", equ_rel(matrix, ra))
