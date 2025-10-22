def find_hamiltonian_cycles(graph):
    n = len(graph)  # liczba wierzchołków w grafie
    cycles = []  # lista do przechowywania znalezionych cykli Hamiltona
    
    # Funkcja pomocnicza do rekursywnego przeszukiwania ścieżek (backtracking)
    def backtrack(path, visited):
        current = path[-1]  # ostatni odwiedzony wierzchołek
        
        # Sprawdzenie czy ścieżka zawiera wszystkie wierzchołki
        if len(path) == n:
            # Jeśli istnieje krawędź powrotna do wierzchołka startowego, to mamy cykl Hamiltona
            if graph[current][path[0]] == 1:
                cycles.append(path + [path[0]])  # dodajemy domknięty cykl do listy
            return
        
        # Iteracja po wszystkich możliwych sąsiadach bieżącego wierzchołka
        for neighbor in range(n):
            # Jeśli istnieje krawędź i wierzchołek nie był jeszcze odwiedzony
            if graph[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True  # oznacz wierzchołek jako odwiedzony
                backtrack(path + [neighbor], visited)  # rekurencyjne wywołanie z nową ścieżką
                visited[neighbor] = False  # cofnięcie (backtracking)
    
    # Przeszukiwanie rozpoczynamy od każdego wierzchołka jako punktu startowego
    for start in range(n):
        visited = [False] * n  # tablica odwiedzonych wierzchołków
        visited[start] = True  # oznacz wierzchołek startowy jako odwiedzony
        backtrack([start], visited)  # rozpocznij budowanie ścieżki od wierzchołka startowego
    
    return cycles  # zwróć wszystkie znalezione cykle Hamiltona


# Funkcja testująca — uruchamia algorytm na podanym grafie i wypisuje wyniki
def test_graph(graph, name):
    print(f"\n{'='*50}")
    print(f"{name}")
    print(f"{'='*50}")
    
    cycles = find_hamiltonian_cycles(graph)
    
    if cycles:
        print(f"\nPodsumowanie: Liczba cykli Hamiltona: {len(cycles)}")
        for cycle in cycles:
            print(" -> ".join(str(node) for node in cycle))
    else:
        print("\nPodsumowanie: Brak cykli Hamiltona w grafie.")


# Przykładowe grafy do testów (reprezentacja jako macierz sąsiedztwa)
graph1 = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

graph2 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

graph3 = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]

graph4 = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]


# Uruchomienie testów tylko jeśli skrypt jest uruchamiany bezpośrednio
if __name__ == "__main__":
    test_graph(graph1, "Przykład 1: Jeden cykl Hamiltona")
    test_graph(graph2, "Przykład 2: Wszystkie cykle to cykle Hamiltona")
    test_graph(graph3, "Przykład 3: Brak cykli Hamiltona")
    test_graph(graph4, "Przykład 4: Macierz 4x4")