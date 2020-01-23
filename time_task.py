import datetime

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

block_scheduler = BlockingScheduler()  #

jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)


# 设置监听
def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


def job_function():
    print("job_function")


scheduler.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2014-05-30')


def addMyJob():
    # 在 2019-03-29 14:00:00 时刻运行一次 job_func 方法
    scheduler.add_job(job_function, 'date', run_date=datetime(2019, 3, 29, 14, 0, 0), args=['text'])


# 特定周期性的触发
def addCirlJob():
    # 在2019-03-30 00:00:00之前，每周一到周五的5:30(am)触发
    scheduler.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2019-03-30')


# ///////////////////////////////////////////////////////////////////////////////////////
# 设置为每日凌晨00:30:30时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='1', minute='30', second='30')
def rebate():
    print("schedule execute")


if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
