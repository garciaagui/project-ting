from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mocked_values = [
        {
            "nome_do_arquivo": "test3.txt",
            "qtd_linhas": 6,
            "linhas_do_arquivo": [1, 2, 3, 4, 5, 6]
        },
        {
            "nome_do_arquivo": "test2.txt",
            "qtd_linhas": 1,
            "linhas_do_arquivo": [1]
        },
        {
            "nome_do_arquivo": "test1.txt",
            "qtd_linhas": 10,
            "linhas_do_arquivo": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
            "nome_do_arquivo": "test4.txt",
            "qtd_linhas": 4,
            "linhas_do_arquivo": [1, 2, 3, 4]
        },
    ]

    priority_queue = PriorityQueue()

    for value in mocked_values:
        priority_queue.enqueue(value)

    assert len(priority_queue) == len(mocked_values)

    dequeued_value = priority_queue.dequeue()
    assert dequeued_value == mocked_values[1]

    value_found = priority_queue.search(0)
    assert value_found == mocked_values[3]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(100)
