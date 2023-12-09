'''---------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement : Implement a problem of minimum work to be done per day to finish given tasks within D days problem.
                    -Given an array task[] of size N denoting amount of work to be done for each task, the problem
                     is to find the minimum amount of work to be done on each day so that all the tasks can be completed in at
                     most D days. Note: On one day work can be done for only one task..
---------------------------------------------------------------------------------------------------------------------------------------------'''


def can_complete_tasks(tasks, D, min_work):
    days = 0
    current_work = 0

    for task in tasks:
        current_work += task
        if current_work > min_work:
            days += 1
            current_work = task

    days += 1
    return days <= D

def min_work_per_day(tasks, D):
    left = max(tasks)
    right = sum(tasks)

    while left < right:
        mid = left + (right - left) // 2
        if can_complete_tasks(tasks, D, mid):
            right = mid
        else:
            left = mid + 1

    return left


tasks = [10, 7, 3, 5, 6]
D = 8

min_work = min_work_per_day(tasks, D)
print("Minimum work per day:", min_work)