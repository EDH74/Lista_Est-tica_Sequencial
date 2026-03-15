import Les

l = Les.Les(5)

l.inserir_fim(1)
l.inserir_fim(2)
l.inserir_fim(3)
l.inserir_fim(4)
l.inserir_inicio(7)
l.show()

print(l.esta_cheia())

print(l.esta_vazia())

l.remover_inicio()
l.show()

print(l.get_prim())

print(l.get_ult())

print(l.get_quant())

print(l.get_capacidade())

l.remover(3)
l.show()

print(l.index(7))

print(l.existe(4))


l.limpar()
print('Lista reiniciada para usar os metodos restantes')
l.inserir_fim(1)#1
l.inserir_fim(2)#2
l.inserir_fim(3)#3
l.inserir_fim(4)#4
l.inserir_inicio(7)#0
print()
l.show()


l.remover_anterior(2)
l.show()

l.remover_posterior(4)
l.show()





l.inserir_apos(9, 3)
l.show()

l.inserir_antes(10, 3)
l.show()
print("Adicionando algo")
l.inverter()    