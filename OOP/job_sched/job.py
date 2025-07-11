from enum import Enum

class Status(Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"

class Job:
    def __init__(self, id: int, description: str, status: Status = Status.pending):
        self.id = id
        self.description = description
        self.status = status

    def run(self):
        print(f"[Job-{self.id}] Status changed from: pending -> running")
        self.status = Status.running
        print(f"[Job-{self.id}] Status changed from: running -> completed")
        self.status = Status.completed


