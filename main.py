import os
import hashlib


s_dir = 'C://python'
d_dir =  'X://python'
md5_dic = {}

def get_md5_list(path=s_dir):#获取所有文件的md5加入字典

    for name in os.listdir(path):
        fname = path +'/'+ name
        if os.path.isdir(fname):
            get_md5_list(fname)
        else:
            with open(fname,'rb')as f:
                md5 = hashlib.md5(f.read()).hexdigest()
                if md5 not in md5_dic:
                    md5_dic[name] = md5

def sync_file(s=s_dir,d=d_dir):

    for name in os.listdir(s):
        fname_s = s+'/'+name
        fname_d = d+'/'+name
        if os.path.isdir(fname_s):
            if not os.path.exists(fname_d):
                print('建立文件夹%s'%name)
                os.mkdir(fname_d)
            sync_file(fname_s,fname_d)
        else:
            if os.path.exists(fname_d):
                with open(fname_d,'rb')as f_d:
                    md5 = hashlib.md5(f_d.read()).hexdigest()
                    if md5 == md5_dic[name]:
                        print('文件%s没有被修改'%name)
                        continue
                    else:
                        md5_dic[name] = md5
            print('复制文件%s'%name)
            write_file(fname_s,fname_d)

def write_file(fname_s,fname_d):

    with open(fname_s, 'rb') as f_s:
        with open(fname_d, 'wb') as f_d:
            f_d.write(f_s.read())

get_md5_list(path=s_dir)
sync_file()


