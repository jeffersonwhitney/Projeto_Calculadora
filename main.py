from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa ('Joao', 32)
p3 = Pessoa ('Jefferson', 26)


p2.falar('marvel')
p1.comer('maca')
p1.parar_comer()
p1.falar('poo')
p2.comer('uva')
p1.falar('poo')
p1.parar_falar()
p1.parar_falar()


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p3.get_ano_nascimento())



