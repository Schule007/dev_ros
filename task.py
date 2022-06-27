from invoke import task
from invoke import run

@task
def build(c):
    c1 = 'catkin clean'
    c2 = 'catkin config --install'
    c3 = 'catkin build'
    run(c1)
    run(c2)
    run(c3)
