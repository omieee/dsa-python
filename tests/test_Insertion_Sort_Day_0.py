from Topics_Learning.Insertion_Sort.insertion_sort_day_0 import Insertion_Sort_Day_0


def test_Insertion_sort_Day_0() -> None:
    isd = Insertion_Sort_Day_0()
    pairs = []
    pairs.append(isd.Pair(5, "apple"))
    pairs.append(isd.Pair(2, "banana"))
    pairs.append(isd.Pair(9, "cherry"))

    want = [
        [(5, "apple"), (2, "banana"), (9, "cherry")],
        [(2, "banana"), (5, "apple"), (9, "cherry")],
        [(2, "banana"), (5, "apple"), (9, "cherry")],
    ]
    result = isd.insertionSort(pairs=pairs)
    got = []
    for state in result:  # each saved snapshot of the list
        row = []
        for p in state:  # each Pair object in that snapshot
            row.append((p.key, p.value))
        got.append(row)

    assert got == want
