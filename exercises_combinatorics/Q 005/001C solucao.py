import math
# 5 engenheiros
# 2 economistas
# 4 administradores
# equipe: 1 eng, 1 econ, 1 adm

engenheiros = 5
economistas = 2
administradores = 4

eng = math.comb(5,1)
eco = math.comb(2,1)
adm = math.comb(4,1)

total_equipes = eng * eco * adm

print(f'A comissão formada por {engenheiros} engenheiros, {economistas} economistas, {administradores} administradores podem formar {total_equipes} equipes diferentes!')