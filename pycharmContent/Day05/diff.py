def diff_out(fname_1, fname_2, rsname):
    with open(fname_1) as f1:
        aset = set(f1)
    with open(fname_2) as f2:
        bset = set(f2)
    with open(rsname, 'w') as rs:
        rs.writelines(bset - aset)

if __name__ == '__main__':
    fname_1 = ''
    fname_2 = ''
    rsname = ''
    diff_out(fname_1, fname_2, rsname)