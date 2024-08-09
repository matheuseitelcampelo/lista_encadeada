#Class que representa um prontuário médico
# """
#     Aqui farei a class Prontuario, uma class que representa o prontuário médico, ela tera os seguintes atributos: 
#     nome_paciente
#     diagnostico
#     tratamento
#     proximo    --referencia para o proximo prontuario da lista
#     obs: proximo deve ter um valor None para receber como padrão
# """
class Prontuario:
    def __init__(self, nome_paciente, diagnostico, tratamento, proximo = None):
        self.nome_paciente = nome_paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo

    def __repr__(self) -> str:
         return f"Paciente: {self.nome_paciente} => {self.proximo}"

#Class que represenra a lista encadeada de prontuários médicos

class ListaEncadeadaProntuarios:
    def __init__(self):
        #inicializa ListaEncadeadaProntuarios como vazia
        self.head = None

    def __repr__(self) -> str:
        return "%s" % (self.head)

    def addProntuario(self, nome_paciente, diagnostico, tratamento):
        # """
        #     Adiciona um novo Prontuario a ListaEncadeadaProntuarios
        #     O novo prontuario é adicionado ao inicio da lista
        # """

        new_prontuario = Prontuario(nome_paciente, diagnostico, tratamento, self.head)
        self.head = new_prontuario

    def buscar_prontuario(self, nome_paciente):
        #  """
        # Busca um prontuário na lista pelo nome do nome_paciente.
        # Retorna o prontuário se encontrado, ou None se não for encontrado.
        # """

        current = self.head # Começa a busca pelo início da lista
        while current: #verifica se current não é nulo
            if current.nome_paciente == nome_paciente: #verifica se o nome do paciente fornecido é o mesmo do nome do paciente na busca
                return current #Retorna prontuario encontrado
            current = current.proximo #Passa para o proximo prontuario da lista
        return None #Caso o elemento não seja encontrado
        
        