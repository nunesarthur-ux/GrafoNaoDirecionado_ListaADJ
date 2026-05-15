from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    '''
    def dfs(self):
        visitados = set()
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[i][j] == 1:
                    visitados.add(self.vertices[i])
    '''


    def ha_ciclo(self):
        '''
        Verifica se existe um ciclo no grafo direcionado. Retorna um valor booleano
        True caso exista ou False caso não exista ciclo
        :return:
        '''
        for x in self.vertices:
            for y in self.vertices:
                if self.indice_do_vertice(x) == self.indice_do_vertice(y):
                    if self.matriz[self.indice_do_vertice(x)][self.indice_do_vertice(y)] == 1:
                        return True
        return False

    def eh_arvore_dfs(self):
        '''
        determina se o grafo passado é uma árvore e se verdadeiro, definir a quantidade de nós
        folhas que ela apresenta (Dica: aqui pode ser usado tanto o BFS, como
        também o DFS, árvores são grafos conexos e sem ciclos, as folhas são vértices com grau 1).
        :return: Retorna False se não for árvore e se for, retorna uma lista contendo os nós folha.
        preciso saber: Há ciclo e não é conexo? Se sim, não é árvore;
        '''
        if self.ha_ciclo() == True:
            return False


    '''
    def eh_arvore_bfs(self):
    '''




    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        pass