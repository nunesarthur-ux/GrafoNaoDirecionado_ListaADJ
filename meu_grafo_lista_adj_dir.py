from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaDirecionado):

    '''
    def visita_vizinho(self):
        for v in self.vertices:
            for a in self.arestas:
                if self.vertices[v].rotulo == self.arestas[a].v1.rotulo:
    '''
    def vertice_oposto (self,V,a):
        oposto = ''
        for a in self.arestas:
            if V in self.arestas[a].v1:
                oposto = self.arestas[a].v2
            elif V in self.arestas[a].v2:
                oposto = self.arestas[a].v1
        return oposto

    def dfs_recursivo(self, V):
        a = self.arestas_sobre_vertice(V)
        arestas_visitadas = []
        for i in a:
            self.get_vertice(V)
            self.get_aresta(a)
            arestas_visitadas.append(i)
            x = self.vertice_oposto(V,i)
            self.dfs_recursivo(x)



    def bfs(self):
        '''
        Explora as arestas do grafo para descobrir
        cada vértice que pode ser alcançado a partir do vértice fonte.
        :return:
        '''

    

    def verifica_repeticao(self):
        for v in self.vertices:
            if self.vertices[v].count(v.rotulo) > 1:
                return True
        return False



    def ha_ciclo(self):
        '''
        Se o vértice se repetir na busca, tem ciclo. Verifica a ocorrência do vértice
        Uso da função verifica_repeticao
        '''

    def eh_arvore(self):
        '''
        Se houver ciclo, não é árvore.

        :return:
        '''

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        pass # Apague essa instrução e inicie seu código aqui

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau_entrada(self, V=''):
        '''
        Provê o grau de entrada do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau de saída do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError


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
        arestas_sobre_vertices = []
        if not self.existe_rotulo_vertice(V):
            return VerticeInvalidoError
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                arestas_sobre_vertices.append(a.rotulo)
        return arestas_sobre_vertices

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''