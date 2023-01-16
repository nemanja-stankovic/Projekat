#broj_u_indeksu=118
#rb_zad_1 = broj_u_indeksu % 8 + 1=7
#rb_zad_2 = (rb_zad_1 + 4) % 8 + 1=4

# 7) (p⇒(q⇒r))⇔((p∧q)⇒r)
#Sledeću strukturu ćemo razložiti na manje delove

# Sa leve strane ekvivalencije je (p⇒(q⇒r)), sto cemo dodeliti nekoj vrednosti B
# B=(p⇒(q⇒r)), daljim razlaganjem, (q⇒r) cemo dodeliti nekoj vrednosti A, tako da je A=(q⇒r), sto znaci da je
# B=(p⇒A)
# Sa desne strane ekvivalencije je ((p∧q)⇒r), sto cemo dodeliti nekoj vrednosti D
# D=((p∧q)⇒r), daljim razlaganjem (p∧q) cemo dodeliti nekoj vrednosti C, tako da je C=(p∧q), sto znaci da je
# D=(C⇒r)
# što znači da smo formulu razložili na iskaz = B⇔D
# gde je B=(p⇒A), A=(q⇒r), D=(C⇒r), C=(p∧q)


#imacemo 8 mogucih kombinacija
# 1 slucaj p=True q=True r=True
# 2 slucaj p=True q=True r=False
# 3 slucaj p=True q=False r=True
# 4 slucaj p=True q=False r=False
# 5 slucaj p=False q=True r=True
# 6 slucaj p=False q=True r=False
# 7 slucaj p=False q=False r=True
# 8 slucaj p=False q=False r=False

# 1 slucaj
p=True
q=True
r=True

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p1,q1,r1,D1)=(p,q,r,Iskaz)        # pamtimo prvi slucaj


# 2 slucaj
p=True
q=True
r=False

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p2,q2,r2,D2)=(p,q,r,Iskaz)        # pamtimo drugi slucaj


# 3 slucaj
p=True
q=False
r=True

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p3,q3,r3,D3)=(p,q,r,Iskaz)        # pamtimo treci slucaj


# 4 slucaj
p=True
q=False
r=False

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p4,q4,r4,D4)=(p,q,r,Iskaz)        # pamtimo cetvrti slucaj


# 5 slucaj
p=False
q=True
r=True

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p5,q5,r5,D5)=(p,q,r,Iskaz)        # pamtimo peti slucaj


# 6 slucaj
p=False
q=True
r=False

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p6,q6,r6,D6)=(p,q,r,Iskaz)        # pamtimo sesti slucaj


# 7 slucaj
p=False
q=False
r=True

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p7,q7,r7,D7)=(p,q,r,Iskaz)        # pamtimo sedmi slucaj


# 8 slucaj
p=False
q=False
r=False

A = (not q) or r                   # A=(q⇒r)
B = (not p) or A                   # B=(p⇒A)
C = p and q                        # C=(p∧q)
D = (not C) or r                   # D=(C⇒r)
Iskaz=(B and D)or not(B or D)      # Iskaz=(B⇔D)
(p8,q8,r8,D8)=(p,q,r,Iskaz)        # pamtimo osmi slucaj


print(p1,q1,r1,D1)                 # na kraju ispisujemo ulazne podatke za svaku mogucu kombinaciju
print(p2,q2,r2,D2)                 # i vrednost iskaza za tu kombinaciju
print(p3,q3,r3,D3)
print(p4,q4,r4,D4)
print(p5,q5,r5,D5)
print(p6,q6,r6,D6)
print(p7,q7,r7,D7)
print(p8,q8,r8,D8)

if D1 is True and D2 is True and D3 is True and D4 is True and D5 is True and D6 is True and D7 is True and D8 is True:
    print("Iskaz je tautologija")
else:
    print("Iskaz nije tautologija")