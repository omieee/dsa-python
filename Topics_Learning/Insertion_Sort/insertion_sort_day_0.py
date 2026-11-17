class Insertion_Sort_Day_0:
    class Pair:
        def __init__(self, key: int, value: str):
            self.key = key
            self.value = value

    def insertionSort(self, pairs: list[Pair]) -> list[list[Pair]]:
        temppair = []
        for i in range(len(pairs)):
            j = i - 1  # For the previous one
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            temppair.append(pairs[:])
        return temppair
