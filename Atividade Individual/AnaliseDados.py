from abc import ABC, abstractmethod

class AnaliseDados(ABC):

    @abstractmethod
    def entradaDeDados(self):
        """Método abstrato para receber a entrada de dados."""
        pass

    @abstractmethod
    def calcularMediana(self):
        """Método abstrato para calcular a mediana dos dados."""
        pass
    
    @abstractmethod
    def encontrarMenor(self):
        """Método abstrato para encontrar o menor valor nos dados."""
        pass

    @abstractmethod
    def encontrarMaior(self):
        """Método abstrato para encontrar o maior valor nos dados."""
        pass

    @abstractmethod
    def calcularMedia(self):
        """Método abstrato para calcular a média dos dados."""
        pass

    @abstractmethod
    def calcularModa(self):
        """Método abstrato para calcular a moda dos dados."""
        pass

    @abstractmethod
    def listarEmOrdem(self):
        """Método abstrato para listar os dados em ordem."""
        pass
