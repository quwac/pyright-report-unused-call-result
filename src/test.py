import os  # EXPECTED: reportUnusedImport occurred, ACTUAL: reportUnusedImport occurred


def add(v_a: int, v_b: int) -> int:
    return 0


def main():
    add(1, 2)  # EXPECTED: reportUnusedCallResult occurred, ACTUAL: nothing occurred

    if 3 is None:
        pass
