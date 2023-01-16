# broj_u_indeksu=118
# rb_zad_1 = broj_u_indeksu % 8 + 1=7
# rb_zad_2 = (rb_zad_1 + 4) % 8 + 1=4

# 4) ¬(¬p∧q)⇔p∨¬q
# Sledeću strukturu ćemo razložiti na manje delove

# Sa leve strane ekvivalencije je ¬(¬p∧q), sto cemo dodeliti nekoj vrednosti A
# A=¬(¬p∧q),  A=not((not p) and q),

# Sa desne strane ekvivalencije je p∨¬q, sto cemo dodeliti nekoj vrednosti B
# B=p∨¬q,  B = p or not q

# tako da je iskaz = A⇔B, iskaz=(A and B) or not (A or B)

# imacemo 4 moguce kombinacije
# 1 slucaj p=True q=True
# 2 slucaj p=True q=False
# 3 slucaj p=False q=True
# 4 slucaj p=False q=False


# 1. slucaj
p = True
q = True

A = not((not p) and q)                # A=¬(¬p∧q)
B = p or not q                        # B=p∨¬q
iskaz = (A and B) or not (A or B)     # iskaz = A⇔B

(p1, q1, D1) = (p, q, iskaz)          # pamtimo 1 slucaj

# 2. slucaj
p = True
q = False

A = not((not p) and q)                # A=¬(¬p∧q)
B = p or not q                        # B=p∨¬q
iskaz = (A and B) or not (A or B)     # iskaz = A⇔B

(p2, q2, D2) = (p, q, iskaz)           # pamtimo 2. slucaj

# 3. slucaj
p = False
q = True

A = not((not p) and q)                 # A=¬(¬p∧q)
B = p or not q                         # B=p∨¬q
iskaz = (A and B) or not (A or B)      # iskaz = A⇔B

(p3, q3, D3) = (p, q, iskaz)              # pamtimo 3. slucaj

# 3. slucaj
p = False
q = False

A = not((not p) and q)                  # A=¬(¬p∧q)
B = p or not q                          # B=p∨¬q
iskaz = (A and B) or not (A or B)       # iskaz = A⇔B

(p4, q4, D4) = (p, q, iskaz)            # pamtimo 4. slucaj

print(p1, q1, D1)
print(p2, q2, D2)
print(p3, q3, D3)
print(p4, q4, D4)

if D1 is True and D2 is True and D3 is True and D4 is True:
    print("Iskaz je tautologija")
else:
    print("Iskaz nije tautologija")
