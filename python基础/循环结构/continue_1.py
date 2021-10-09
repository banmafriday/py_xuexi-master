# continue跳过这个循环,执行下个循环

for year in range(1,11):
    if year==8:
        print("第8年,提前还清,以后都不用还了")
        continue
    print(year)