# comunications inner threads
from functools import reduce
from operator import mul
from threading import Thread, Event
from queue import Queue

event = Event()


def primary(matrix) -> None:
    """
    0 1 3 3
    2 3 4 2
    5 3 2 4
    1 2 3 4
    :param matrix: List[list[int]]
    :return: result integer
    """
    list_primary_diagonal = []
    for lines in range(len(matrix)):
        for columns in range(len(matrix)):
            if lines == columns:
                list_primary_diagonal.append(matrix[lines][columns])
    queu.put(reduce(mul, list_primary_diagonal))  # storage the value


def secondary(matrix) -> None:
    """
    0 1 3 3
    2 3 4 2
    5 3 2 4
    1 2 3 4
    :param matrix: List[list[int]]
    :return: result integer
    """
    list_secondary_diagonal = []
    for lines in range(len(matrix)):
        for columns in range(len(matrix)):
            if columns == (len(matrix) - 1) - lines:
                list_secondary_diagonal.append(matrix[lines][columns])
    queu.put(reduce(mul, list_secondary_diagonal))  # storage the value


def solveDT() -> int:
    event.set()  # set the configurations to communicate with other threads
    value1 = queu.queue[0]
    value2 = queu.queue[1]
    return value1 - value2


if __name__ == '__main__':
    matrix = [[2, 5],
             [7, 3]]
    queu = Queue()
    th = Thread(target=primary, name="primary", args=(matrix, ))
    th2 = Thread(target=secondary, name="secondary", args=(matrix, ))
    th.start()
    th2.start()

    # check if there is any thread running.If yes, wait to execute the function
    if th.is_alive() or th2.is_alive():
        event.wait()
    else:
        print(solveDT())
