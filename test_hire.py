task=[  
    {'task1':'task1',
    'seniors':8,
    'juniors':0
    },
    {'task2':'task2',
        'seniors':8,
        'juniors':14
    },
    {   'task3':'task3',
        'seniors':6,
        'juniors':16
    },
    {   'task4':'task4',
        'seniors':5,
        'juniors':12
    },
     {   'task5':'task5',
        'seniors':6,
        'juniors':0
    },
    {   'task6':'task6',
        'seniors':8,
        'juniors':18
    },
    {   'task7':'task7',
        'seniors':9,
        'juniors':24
    },
    {   'task8':'task8',
        'seniors':2,
        'juniors':0
    },
    {   'task9':'task9',
        'seniors':4,
        'juniors':10
    },
    {   'task10':'task10',
        'seniors':6,
        'juniors':24
    },
   
]
total_hours_juniors=0
total_hours_seniors=0
task_seniors_only=[]
task_available_juniors=[]

#ratio=[10,20,30,40]


for tsk in task:
    
    total_hours_juniors=total_hours_juniors+tsk['juniors']
    total_hours_seniors=total_hours_seniors+tsk['seniors']
    if tsk['juniors']==0:
        task_seniors_only.append(tsk)
    else:
        task_available_juniors.append(tsk)
print(total_hours_juniors,total_hours_seniors)
print(task_available_juniors,task_seniors_only)
thrs=0
thjr=0
for tsk in task_seniors_only:
    
    thrs=thrs+tsk['seniors']
for tsk in task_available_juniors:
    thjr=thjr+tsk['juniors']

print(thrs,thjr)
# tjnr=0
# ratio=10
# while (len(task_seniors_only)!=len(task)):
#     total=thrs+tjnr
#     calculated_ratio=thrs/(total)
#     if calculated_ratio!=ratio:
#         pass
def check_ratio(thrs,thjr):
    
    total=thrs+thjr
    print(total)
    # calculated_ratio=(thrs/(total))*100
    calculated_ratio=(thrs/total)*100
    return calculated_ratio
check_ratio(thrs,thjr)
y=check_ratio(thrs,thjr)
print(y)
input_ratio=34
sorted_task_junior=sorted(task_available_juniors, key=lambda x: x['juniors'],reverse=True)
if input_ratio!=y:
    for i in range(len(sorted_task_junior)):
        task_seniors_only.append(sorted_task_junior.pop())
        # thjr=thjr+tsk['juniors']
        # print(thrs)
        # print(len(task_available_juniors)) 
        thrs=0
        for tsk in task_seniors_only:
    
            thrs=thrs+tsk['seniors']
        print("Senior:",thrs)

        # for tsk in task_available_juniors:
        #     thjr=thjr+tsk['juniors']
        print(len(task_seniors_only))
        print("Junior",thjr)
        y=check_ratio(thrs,thjr)
        print(round(y))
        if input_ratio==round(y):
            print(y)
            print(task_seniors_only)
            break
            
    # return calculated_ratio
# ratio=check_ratio()
# print(ratio)
# input_ratio=0
# while True:
#     # print(thrs)
#     if input_ratio!=ratio:
#         for i in range(len(task_available_juniors)):
#             print(thrs)
#             thrs=thrs+task_available_juniors[i]['seniors']
#             print(thrs)
    

  

        

                