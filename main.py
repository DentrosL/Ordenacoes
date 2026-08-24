# variaveis globais
run = True
array = [64, 34, 25, 12, 22, 11, 90]

print("dados a serem ordenados:", array)

def menu():
    print("Escolha o algoritmo de ordenação:")
    print("1. Bubble Sort")
    print("2. Quick Sort")
    print("3. Insertion Sort")
    print("4. Selection Sort")
    print("5. Merge Sort")
    print("6. Sair")

# o bubble sort é um ordenador simples que percorre a lista várias vezes, comparando elementos adjacentes e trocando-os se estiverem na ordem errada. O processo é repetido até que a lista esteja ordenada.
# FUNCIONAMENTO: pega o array, percorre ele no for externo, e no for interno ele compara os elementos adjacentes, se o elemento da esquerda for maior que o da direita, ele troca eles de posição. O processo é repetido até que a lista esteja ordenada.

# exemplo do bubble sort com [64, 34, 25]:
# compara 64 e 34 -> troca: [34, 64, 25]
# compara 64 e 25 -> troca: [34, 25, 64]
# ao final da primeira passagem, o maior valor vai para o final. e repete o processo para os elementos restantes.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# CONCEITO: o quick sort é um ordenador eficiente que utiliza a técnica de divisão e conquista. Ele seleciona um elemento como pivô e particiona a lista em duas sublistas: uma com elementos menores que o pivô e outra com elementos maiores. Em seguida, ele aplica recursivamente o mesmo processo às sublistas.
# FUNCIONAMENTO: pega o array, seleciona um elemento como pivô e particiona a lista em duas sublistas: uma com elementos menores que o pivô e outra com elementos maiores. Em seguida, ele aplica recursivamente o mesmo processo às sublistas.

# EXEMPLO: em [64, 34, 25], o pivô é 34.
# valores menores ficam à esquerda: [25]
# valores iguais ficam no meio: [34]
# valores maiores ficam à direita: [64]
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# CONCEITO: o insertion sort é um ordenador simples que constrói a lista ordenada um elemento de cada vez. ele percorre a lista e insere cada elemento na posição correta em relação aos elementos já ordenados.
# FUNCIONAMENTO: pega o array, percorre ele no for externo, e no for interno ele compara o elemento atual com os elementos anteriores, se o elemento atual for menor que o elemento anterior, ele troca eles de posição. o processo é repetido até que a lista esteja ordenada.

# EXEMPLO do insertion sort com [64, 34, 25]:
# começa considerando 64 como ordenado: [64, 34, 25]
# pega 34, desloca 64 para a direita e insere 34 antes dele: [34, 64, 25]
# pega 25, desloca 64 e 34 para a direita e insere 25 no início: [25, 34, 64]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# CONCEITO: o selection sort é um ordenador que divide a lista em duas partes: a parte ordenada e a parte não ordenada. ele seleciona o menor elemento da parte não ordenada e o troca com o primeiro elemento da parte não ordenada, repetindo esse processo até que toda a lista esteja ordenada.
# FUNCIONAMENTO: pega o array, percorre ele no for externo, e no for interno ele seleciona o menor elemento da parte não ordenada e o troca com o primeiro elemento da parte não ordenada. o processo é repetido até que toda a lista esteja ordenada.

# EXEMPLO do selection sort com [64, 34, 25]:
# procura o menor valor, 25, e troca com o primeiro elemento: [25, 34, 64]
# procura o menor valor restante, 34, que já está na posição correta.
# repete o processo até que todos os elementos estejam ordenados.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  

# o merge sort é um ordenador eficiente que utiliza a técnica de divisão e conquista. ele divide a lista em duas metades, ordena cada metade recursivamente e, em seguida, mescla as duas metades ordenadas em uma única lista ordenada.
# FUNCIONAMENTO: pega o array, divide a lista em duas metades, ordena cada metade recursivamente e, em seguida, mescla as duas metades ordenadas em uma única lista ordenada.

# EXEMPLO do merge sort com [64, 34, 25]:
# divide a lista em [64] e [34, 25], depois divide [34, 25] em [34] e [25].
# mescla [34] e [25] em ordem: [25, 34].
# por fim, mescla [64] com [25, 34]: [25, 34, 64].
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    # compara o primeiro elemento de cada metade e adiciona o menor resultado.
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

while run:
    menu()
    opcao = input("Escolha uma opção: ")
    match(opcao):
        case "1":
            bubble_sort(array)
            print("Array ordenado usando Bubble Sort:", array)
            break
        case "2":
            sorted_array = quick_sort(array)
            print("Array ordenado usando Quick Sort:", sorted_array)
            break
        case "3":
            insertion_sort(array)
            print("Array ordenado usando Insertion Sort:", array)
            break
        case "4":
            selection_sort(array)
            print("Array ordenado usando Selection Sort:", array)
            break
        case "5":
            sorted_array = merge_sort(array)
            print("Array ordenado usando Merge Sort:", sorted_array)
            break
        case "6":
            print("Saindo do programa.")
            run = False
            break
