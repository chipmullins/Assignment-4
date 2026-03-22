from dataclasses import dataclass


@dataclass
class Task:
    task_id: str
    priority: int
    arrival_time: int
    deadline: int
    description: str = ""

    def __repr__(self):
        return (
            f"Task(task_id={self.task_id}, priority={self.priority}, "
            f"arrival_time={self.arrival_time}, deadline={self.deadline})"
        )


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task: Task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def increase_key(self, task_id: str, new_priority: int):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    raise ValueError("New priority must be greater than current priority.")
                self.heap[i].priority = new_priority
                self._heapify_up(i)
                return
        raise ValueError("Task not found.")

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def __repr__(self):
        return str(self.heap)


if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert(Task("T1", 4, 0, 10, "Write report"))
    pq.insert(Task("T2", 7, 1, 8, "Fix server issue"))
    pq.insert(Task("T3", 2, 2, 15, "Reply to email"))

    print("Initial queue:", pq)
    print("Extracted max:", pq.extract_max())
    pq.increase_key("T3", 9)
    print("Queue after increasing T3 priority:", pq)