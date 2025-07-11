from job import *
from worker import *
from scheduler import *

if __name__ == "__main__":
    
    job1 = Job(1, "Generate report")
    job2 = Job(2, "Send email")
    job3 = Job(3, "Backup DB")

    # creează workeri
    w1 = Worker(1, "Alice")
    w2 = Worker(2, "Bob")

    # scheduler
    scheduler = Scheduler()
    scheduler.add_worker(w1)
    scheduler.add_worker(w2)

    scheduler.add_job(job1)
    scheduler.add_job(job2)
    scheduler.add_job(job3)

    scheduler.assign_job()
