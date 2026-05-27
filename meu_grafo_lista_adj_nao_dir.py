from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def verifica_repeticao(self):
        for v in self.vertices:
            if self.vertices[v].count(v.rotulo) > 1:
                return True
        return False


    def ha_ciclo(self):
        if self.verifica_repeticao():
            return True
        return False


    def eh_arvore(self):
        for a in self.arestas:
            if self.grau(self.arestas[a].v1.rotulo) or self.grau(self.arestas[a].v2.rotulo) > 1:
                return False
        return True


    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''



    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == self.arestas[a].v2.rotulo:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        grau = 0
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        a_v = []
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or (not self.arestas[a].v2.rotulo == V):
                a_v.append(self.arestas[a].rotulo)
        return a_v

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass