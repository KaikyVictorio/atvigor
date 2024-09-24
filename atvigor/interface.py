from abc import ABC,abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento():
        pass
    @abstractmethod
    def cancelar_pagamento():
        pass
    
class PagamentoCartao(Pagamento):
    def processar_pagamento(senha,valor):
        return print(f"Sua senha é {senha}\nSeu pagamento no valor de R${valor} foi concluido")
        
    def cancelar_pagamento(senha,valor):
        return print(f"O pagamento no valor de R${valor} foi cancelado")

class PagamentoPix(Pagamento):
    def processar_pagamento(chave,valor):
        return print(f"Sua chave é {chave} e o valor R${valor}")
    def cancelar_pagamento(chave,valor):
        return print(f"A compra da chave {chave} foi cancelada ")
        
pagou = PagamentoPix.processar_pagamento("cpf",1500)
print(pagou)  
cancela = PagamentoCartao.cancelar_pagamento("cpf",2000)   
print(cancela)      
    