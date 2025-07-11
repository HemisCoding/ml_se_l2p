from job import Job
from worker import Worker
from typing import List

class Scheduler:

    def __init__(self, jobs: List[Job] = None, workers: List[Worker] = None):
        self.jobs = jobs if jobs else []
        self.workers = workers if workers else []

    def add_job(self, job: Job):
        self.jobs.append(job)
        print(f"[Scheduler] Added Job {job.id}: {job.description}")
    
    def add_worker(self, worker: Worker):
        self.workers.append(worker)
        print(f"[Scheduler] Added Worker {worker.id}: {worker.name}")

    def assign_job(self):

        print(f"[Scheduler] Assigning jobs...")
        worker_count = len(self.workers)
        for index, job in enumerate(self.jobs):
            worker = self.workers[index % worker_count]
            worker.execute(job)

        