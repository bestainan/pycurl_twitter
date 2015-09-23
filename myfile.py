#-*- coding:UTF-8 -*-
def read_file_acc_paswd(fname):
    count_list =[]
    account = ''
    password = ''
    with open(fname,'r+') as f:
        a = f.readline().strip('\n').split('\t')
        account = a[0]
        password = a[1]
        
    return account,password

def save_file(fname1,fname2):
    f1_list = []
    f2_list = []
    f1 = open(fname1, 'r+')
    f2 = open(fname2, 'r+')
    for i in f1:
        f1_list.append(i)
        
    
    for i in f2:
        f2_list.append(i)
       
    for i in range(len(f2_list)):
        if f2_list[i] in f1_list:
            f1_list.remove(f2_list[i])
    f1.close()
    f2.close()
    f1 = open(fname1, 'w')
    for i in f1_list:
        f1.write(i)
    f1.close()
    
    
    

        

if __name__ == '__main__':
    #app.save_file_name()
    save_file('acc.ini', 'jihuo.ini')

