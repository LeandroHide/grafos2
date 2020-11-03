class Grafos:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.pesos = []
        self.listasArestasComValor = []


    def ler(self, arquivo):
        f = open(arquivo, "r")
        contador = 0
        block = 0
        edgesArcs = 0
        listaVertices = []
        listaArestas = []
        matrizPesos = []
        listasArestasComValor = []

        for x in f:
            if x[0] == "*":
                contador += 1
                if x[1] == "e":
                    edgesArcs = 1
                else:
                    edgesArcs = 2
                if block == 0:
                    v = int(x[10:])+1
                    for _ in range(v):
                        
                        listaArestas.append([])
                    matrizPesos = [[float('inf') for x in range(v)] for y in range(v)]
                    block = 1
            if contador == 1 and x[0] != "*":
                temp = x.split()
                temp1 = temp[1]
                for i in range(2, len(temp)):
                    temp1 = temp1 + " " + temp[i]
                lista = []
                lista.append(int(temp[0]))
                lista.append(temp1)
                temp = lista

                listaVertices.append(temp)
            if contador == 2 and x[0] != "*" and edgesArcs == 1:
                temp = x.split()
                listaArestas[int(temp[0])].append(int(temp[1]))
                listaArestas[int(temp[1])].append(int(temp[0]))
                matrizPesos[int(temp[0])][int(temp[1])] = temp[2]
                matrizPesos[int(temp[1])][int(temp[0])] = temp[2]

                listasArestasComValor.append([int(temp[0]), int(temp[1]), float(temp[2])])
            if contador == 2 and x[0] != "*" and edgesArcs == 2:
                temp = x.split()
                listaArestas[int(temp[0])].append(int(temp[1]))
                matrizPesos[int(temp[0])][int(temp[1])] = temp[2]

        self.vertices = listaVertices
        self.arestas = listaArestas
        self.pesos = matrizPesos
        self.listasArestasComValor = listasArestasComValor


    def fortemente_conexas(self):
        [c, t, a, f] = self.dfs(self.vertices, self.arestas)
        graf = Grafos()
        graf.vertices = self.vertices
        
        for u in range(len(self.vertices)+1):
            graf.arestas.append([])

        for u in range(1, len(self.vertices)+1):
            for v in self.arestas[u]:
                graf.arestas[v].append(u)

        for i in range(1, len(self.vertices)+1):
            for j in range(i, len(self.vertices)+1):
                if f[j] > f[i]:
                    temp = f[i]
                    f[i] = f[j]
                    f[j] = temp
                    temp2 = graf.vertices[i-1]
                    graf.vertices[i-1] = graf.vertices[j-1]
                    graf.vertices[j-1] = temp2

        [ct, tt, at, ft] = self.dfs(graf.vertices, graf.arestas)

        lista = []
        lista_raizes = []
        conexo = False
        for i in range(1, len(self.vertices)+1):
            if at[i] == None:
                lista_raizes.append(i)
            caminho = [i]
            j = i
            while True:
                if at[j] == None:
                    break
                caminho = caminho + [at[j]]
                j = at[j]
                conexo = True
            lista.append(caminho)

        if conexo == True:
            for x in lista_raizes:
                maior = []
                for y in lista:
                    if x == y[len(y)-1]:
                        if len(y) > len(maior):
                            maior = y
                print(*maior, sep = ", ")
        else:
            print("Nao ha componentes conexos")
                    


    def dfs(self, lista_vertices, lista_arestas):
        c = []
        t = []
        f = []
        a = []
    
        for x in range(len(lista_vertices)+1):
            c.append(False)
            t.append(float('inf'))
            f.append(float('inf'))
            a.append(None)

        tempo = 0


        for u in lista_vertices:
            if c[u[0]] == False:
                [c, t, a, f, tempo] = self.dfs_visit(lista_arestas, u[0], c, t, a, f, tempo)

        return [c, t, a, f]

    def dfs_visit(self, lista_arestas, v, c, t, a, f, tempo):
        c[v] = True
        tempo += 1
        t[v] = tempo
        for u in lista_arestas[v]:
            if c[u] == False:
                a[u] = v 
                [c, t, a, f, tempo] = self.dfs_visit(lista_arestas, u, c, t, a, f, tempo)
        tempo += 1
        f[v] = tempo
        return [c, t, a, f, tempo]


    def ordenacao_topologica(self):
        c = []
        t = []
        f = []
    
        for x in range(len(self.vertices)+1):
            c.append(False)
            t.append(float('inf'))
            f.append(float('inf'))

        tempo = 0
        o = []
 
        for u in self.vertices:
            if c[u[0]] == False:
                [c, t, f, tempo, o] = self.dfs_visit_ot(u[0], c, t, f, tempo, o)

        print(*o, sep = " -> ")
        return o
    
    def dfs_visit_ot(self, v, c, t, f, tempo, o):
        c[v] = True
        tempo += 1
        t[v] = tempo
        for u in self.arestas[v]:
            if c[u] == False:
                [c, t, f, tempo, o] = self.dfs_visit_ot(u, c, t, f, tempo, o)
        tempo = tempo + 1
        f[v] = tempo
        o = [self.vertices[v-1][1]] + o

        return [c, t, f, tempo, o]

    def kruskal(self):
        a = []
        s = []
        for v in self.vertices:
            s.append([v[0]])
        e = self.listasArestasComValor
        e.sort(key = lambda x: x[2])
        somatorio = 0
        for [u, v, w] in e:
            if s[u-1] != s[v-1]:
                string = str(u) + "-" + str(v)
                a = a + [string]
                somatorio += w
                x = s[u-1] + s[v-1]
                for y in x:
                    s[y-1] = x

        print(somatorio)
        print(*a, sep = ", ")

grafo2 = Grafos()
grafo2.ler("exemplos/manha.net")
grafo2.fortemente_conexas()
grafo2.ordenacao_topologica()


