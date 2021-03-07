# from flask import Flask
import datetime as dt
from data import db_session
from data.users import User
from data.job import Job
import sqlalchemy
from flask import url_for, request, Flask, render_template
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# def main():

db_session.global_init('db/blogs.db')
db_sess = db_session.create_session()

# job = Job()
# job.team_leader = 1
# job.job = "deployment of residential modules 1 and 2"
# job.work_size = 15
# job.collaborators = "2, 3"
#
# db_sess.add(job)
#
#
# for i in range(10):
#     job = Job()
#     job.team_leader = i
#     job.job = f"deployment of residential modules {10 * i} and {10 * i + 1}"
#     job.work_size = 15+i
#     job.collaborators = f"{i+1}, 5"
#     job.is_finished = i % 2 == 0
#
#     db_sess.add(job)
# db_sess.commit()


# global_init(input())
# db_sess = create_session()


@app.route('/')
def index():
    params = ['title', 'team_lead', 'duration', 'collaborators', 'is_finished']
    log = [dict(zip(params, [job.job, job.team_leader,
                             ((job.end_date or dt.datetime.now()) - job.start_date).total_seconds() // 3600,
                             job.collaborators, job.is_finished]))
           for job in db_sess.query(Job).all()]
    print(log)
    return render_template('work_log.html', log=log)


app.run()

# if __name__ == '__main__':
#     main()
