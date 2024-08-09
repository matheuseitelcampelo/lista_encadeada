import gerenciamento_prontuarios_medicos as pm

lista = pm.ListaEncadeadaProntuarios()


## Adicionando prontuários ao sistema
lista.addProntuario("Pedro", "se maxucou", "2 dias de atestado")
lista.addProntuario("Harry", "queboru o braço", "crecimento de novos ossos")
lista.addProntuario("Hermione", "ingestão de poção ilegal", "observação")

print(lista)


# Buscando um prontuário específico pelo nome do paciente
busca_prontuario = lista.buscar_prontuario("Harry")
print(busca_prontuario)
