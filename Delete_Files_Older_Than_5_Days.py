import os
import datetime
import shutil
path=r"C:\Users\Iliyas\OneDrive\Documents"
all_dir=os.listdir(path)
age=5
today=datetime.datetime.now()
print('-----------------------------------------------------------------')
print(f' Log Date {today}')
Target_dir=('_CodeBackup','_AWS-Keys')
for each_dir in all_dir:
    if each_dir.startswith(Target_dir):
      each_dir_path=os.path.join(path,each_dir)
      if os.path.isdir(each_dir_path):
       die_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_dir_path))
       dif_days=(today-die_cre_date).days
       if dif_days > age:
           print('-----------------------------------------------------------------------')
           print(f' The {each_dir_path} folder in older the {dif_days} days : Deleting it')
           shutil.rmtree(each_dir_path)
           print("Path Deleted")
           print('-----------------------------------------------------------------------')
       else:
           print(f'{each_dir_path} is {dif_days} days older :Keeping it')
print('-----------------------------------------------------------------')