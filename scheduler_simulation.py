from priority_queue import PriorityQueue, Task


def simulate_scheduler():
    pq = PriorityQueue()

    tasks = [
        Task("T1", 3, 0, 15, "Routine backup"),
        Task("T2", 8, 1, 5, "Security patch"),
        Task("T3", 5, 2, 10, "Database cleanup"),
        Task("T4", 10, 3, 4, "Critical server restart"),
        Task("T5", 1, 4, 20, "Generate weekly report")
    ]

    for task in tasks:
        pq.insert(task)

    print("Task execution order based on priority:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(task)


if __name__ == "__main__":
    simulate_scheduler()