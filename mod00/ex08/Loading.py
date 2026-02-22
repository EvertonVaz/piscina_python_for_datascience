from typing import Iterator
from time import sleep, time


def ft_tqdm(lst: range) -> Iterator[int]:
    """Gerador de barra de progresso..."""
    start = time()
    size = len(lst)
    for i, elem in enumerate(lst):
        percent = (i + 1) / size * 100
        bar = "=" * int(percent // 2) + ">" + " " * (50 - int(percent // 2))
        print(f"\r{percent:.0f}%|[{bar}]| {int(elem)+1}/{size}", end="")
        yield elem
        end = time()
        elapsed = end - start

    it_per_sec = (i + 1) / elapsed if elapsed > 0 else 0

    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    elapsed_str = f"{minutes:02d}:{seconds:02d}"

    print(f"[{elapsed_str}<00:00, {it_per_sec:.2f}it/s]", end="\n")


if __name__ == "__main__":
    for i in ft_tqdm(list(range(333))):
        sleep(0.005)
