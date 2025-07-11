from job import Job

class Worker:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
    
    def execute(self, job: Job):
        print(f"[Worker-{self.id}] {self.name} Executing Job {job.id}: {job.description}")
        job.run()
