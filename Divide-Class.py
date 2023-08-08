import xlrd
import xlwt
import copy
from operator import itemgetter
import random

class Read_Ex:
    
    def read_excel(self):
        global book_key
        string_input = "/Users/liangkaixi/Desktop/3年级成绩表.xls"
        book = xlrd.open_workbook(string_input)
        string_input = "Sheet1"
        table = book.sheet_by_name(string_input)
        row_Num = table.nrows
        col_Num = table.ncols
        s = []
        key = table.row_values(0)
        book_key = key
        if row_Num <= 1:
            print('没数据')
        else:
            j = 1
            for i in range(row_Num - 1):
                d = { }
                values = table.row_values(j)
                for x in range(col_Num):
                    d[key[x]] = values[x]
                j += 1
                s.append(d)
            return s
def change_sex():
    # 对男女超过平均值的班级配平男女
    # 1. 男女都超过高平均值的两个班级互换
    for boys_id in range(need_class):
        while every_class[boys_id]['男'] > every_boys_number2:
            once_flag = 0
            for girls_id in range(need_class):
                if boys_id != girls_id and every_class[girls_id]['女'] > every_girls_number2:
                    # 在 boys_id 班和 girls_id 班中寻找 分段 相同的男女生交换
                    for boy in range(len(finall_class[boys_id])):
                        if finall_class[boys_id][boy]['性别'] == '男' \
                        and ((book_key.count('预设班级') != 0 and finall_class[boys_id][boy]['预设班级'] == '') or book_key.count('预设班级') == 0):
                            for girl in range(len(finall_class[girls_id])):
                                if finall_class[girls_id][girl]['性别'] == '女' \
                                and ((book_key.count('预设班级') != 0 and finall_class[girls_id][girl]['预设班级'] == '') or book_key.count('预设班级') == 0) \
                                and finall_class[boys_id][boy]['分段'] ==  finall_class[girls_id][girl]['分段']:
                                    finall_class[boys_id][boy], finall_class[girls_id][girl] = finall_class[girls_id][girl],finall_class[boys_id][boy]
                                    every_class[boys_id]['男'] = every_class[boys_id]['男'] - 1
                                    every_class[boys_id]['女'] = every_class[boys_id]['女'] + 1
                                    every_class[girls_id]['男'] = every_class[girls_id]['男'] + 1
                                    every_class[girls_id]['女'] = every_class[girls_id]['女'] - 1
                                    once_flag = 1;
                                    break
                        if once_flag == 1:
                            break
                if once_flag == 1:
                    break
            if once_flag == 0:
                break
    # 2. 女生超过高平均值的班级和男生超过低平均值的班级互换 （男生班级人数会变成高平均值）
    for girls_id in range(need_class):
        while every_class[girls_id]['女'] > every_girls_number2:
            once_flag = 0
            for boys_id in range(need_class):
                if boys_id != girls_id and every_class[boys_id]['男'] > every_boys_number1:
                    # 在 boys_id 班和 girls_id 班中寻找 分段 相同的男女生交换
                    for boy in range(len(finall_class[boys_id])):
                        if finall_class[boys_id][boy]['性别'] == '男'\
                        and ((book_key.count('预设班级') != 0 and finall_class[boys_id][boy]['预设班级'] == '') or book_key.count('预设班级') == 0):
                            for girl in range(len(finall_class[girls_id])):
                                if finall_class[girls_id][girl]['性别'] == '女' \
                                    and ((book_key.count('预设班级') != 0 and finall_class[girls_id][girl]['预设班级'] == '') or book_key.count('预设班级') == 0) \
                                    and finall_class[boys_id][boy]['分段'] ==  finall_class[girls_id][girl]['分段']:
                                    finall_class[boys_id][boy], finall_class[girls_id][girl] = finall_class[girls_id][girl],finall_class[boys_id][boy]
                                    every_class[boys_id]['男'] = every_class[boys_id]['男'] - 1
                                    every_class[boys_id]['女'] = every_class[boys_id]['女'] + 1
                                    every_class[girls_id]['男'] = every_class[girls_id]['男'] + 1
                                    every_class[girls_id]['女'] = every_class[girls_id]['女'] - 1
                                    once_flag = 1;
                                    break
                        if once_flag == 1:
                            break
                if once_flag == 1:
                    break
            if once_flag == 0:
                break
    # 3. 男生超过高平均值的班级和女超过低平均值的班级互换 （女班级人数会变成高平均值）
    for boys_id in range(need_class):
        while every_class[boys_id]['男'] > every_boys_number2:
            once_flag = 0
            for girls_id in range(need_class):
                if boys_id != girls_id and every_class[girls_id]['女'] > every_girls_number1:
                    # 在 boys_id 班和 girls_id 班中寻找 分段 相同的男女生交换
                    for boy in range(len(finall_class[boys_id])):
                        if finall_class[boys_id][boy]['性别'] == '男'\
                        and ((book_key.count('预设班级') != 0 and finall_class[boys_id][boy]['预设班级'] == '') or book_key.count('预设班级') == 0):
                            for girl in range(len(finall_class[girls_id])):
                                if finall_class[girls_id][girl]['性别'] == '女' \
                                    and ((book_key.count('预设班级') != 0 and finall_class[girls_id][girl]['预设班级'] == '') or book_key.count('预设班级') == 0) \
                                    and finall_class[boys_id][boy]['分段'] ==  finall_class[girls_id][girl]['分段']:
                                    finall_class[boys_id][boy], finall_class[girls_id][girl] = finall_class[girls_id][girl],finall_class[boys_id][boy]
                                    every_class[boys_id]['男'] = every_class[boys_id]['男'] - 1
                                    every_class[boys_id]['女'] = every_class[boys_id]['女'] + 1
                                    every_class[girls_id]['男'] = every_class[girls_id]['男'] + 1
                                    every_class[girls_id]['女'] = every_class[girls_id]['女'] - 1
                                    once_flag = 1;
                                    break
                        if once_flag == 1:
                            break
                if once_flag == 1:
                    break
            if once_flag == 0:
                break      
    # 4. 女生低于低平均值的班级和女生等于高平均值班级互换 （男生班级人数会变成低平均值）
    for girls_id in range(need_class):
        while every_class[girls_id]['女'] < every_girls_number1 and every_class[girls_id]['男'] > every_boys_number1:
            once_flag = 0
            for boys_id in range(need_class):
                if boys_id != girls_id and every_class[boys_id]['男'] < every_boys_number2 and every_class[boys_id]['女'] > every_girls_number1:
                    # 在 boys_id 班和 girls_id 班中寻找 分段 相同的男女生交换
                    for boy in range(len(finall_class[girls_id])):
                        if finall_class[girls_id][boy]['性别'] == '男'\
                            and ((book_key.count('预设班级') != 0 and finall_class[girls_id][boy]['预设班级'] == '') or book_key.count('预设班级') == 0):
                            for girl in range(len(finall_class[boys_id])):
                                if finall_class[boys_id][girl]['性别'] == '女' \
                                    and ((book_key.count('预设班级') != 0 and finall_class[boys_id][girl]['预设班级'] == '') or book_key.count('预设班级') == 0) \
                                    and finall_class[boys_id][girl]['分段'] ==  finall_class[girls_id][boy]['分段']:
                                    finall_class[boys_id][girl], finall_class[girls_id][boy] = finall_class[girls_id][boy],finall_class[boys_id][girl]
                                    every_class[boys_id]['男'] = every_class[boys_id]['男'] + 1
                                    every_class[boys_id]['女'] = every_class[boys_id]['女'] - 1
                                    every_class[girls_id]['男'] = every_class[girls_id]['男'] - 1
                                    every_class[girls_id]['女'] = every_class[girls_id]['女'] + 1
                                    once_flag = 1;
                                    break
                        if once_flag == 1:
                            break
                if once_flag == 1:
                    break
            if once_flag == 0:
                break
def cal_ave():
    all_range = 0
    for cal_ave_subject in score_key:
        all_cal_ave_subject = '总分' + cal_ave_subject
        max_score = -1
        min_score = 1000000
        for i in range(need_class):
            every_class[i][cal_ave_subject] = 0
            for number_id in range(len(finall_class[i])):
                every_class[i][cal_ave_subject] = every_class[i][cal_ave_subject] + finall_class[i][number_id][cal_ave_subject]
            every_class[i][all_cal_ave_subject] = every_class[i][cal_ave_subject]
            every_class[i][cal_ave_subject] = every_class[i][cal_ave_subject] / len(finall_class[i])
            if max_score < every_class[i][cal_ave_subject]:
                max_score = every_class[i][cal_ave_subject]
            if min_score > every_class[i][cal_ave_subject]:
                min_score = every_class[i][cal_ave_subject]
        all_range = all_range + max_score - min_score
    return all_range
# 按两个班级的每门课平均分差值是否变小决定是否交换
def check1(max_class_id, p1, min_class_id, p2):
    all_range1 = 0
    for subject in score_key:
        all_range1 = all_range1 + abs(every_class[max_class_id][subject] - every_class[min_class_id][subject])
    all_range2 = 0
    for subject in score_key:
        all_subject = '总分' + subject    
        temp1_ave = every_class[max_class_id][all_subject] - finall_class[max_class_id][p1][subject] + finall_class[min_class_id][p2][subject]
        temp1_ave = temp1_ave / len(finall_class[max_class_id])
        temp2_ave = every_class[min_class_id][all_subject] - finall_class[min_class_id][p2][subject] + finall_class[max_class_id][p1][subject]
        temp2_ave = temp2_ave / len(finall_class[min_class_id])
        all_range2 = all_range2 + abs(temp2_ave - temp1_ave)
    if all_range2 < all_range1:
        return True
    else:
        return False

# 按总极差变小决定是否交换
def check2(max_class_id, p1, min_class_id, p2):
    all_range = 0
    all_range1 = 0
    for subject in score_key:
        all_range1 = all_range1 + abs(every_class[max_class_id][subject] - every_class[min_class_id][subject])
    all_range2 = 0
    for subject in score_key:
        all_subject = '总分' + subject 
        temp1_ave = every_class[max_class_id][all_subject] - finall_class[max_class_id][p1][subject] + finall_class[min_class_id][p2][subject]
        temp1_ave = temp1_ave / len(finall_class[max_class_id])
        temp2_ave = every_class[min_class_id][all_subject] - finall_class[min_class_id][p2][subject] + finall_class[max_class_id][p1][subject]
        temp2_ave = temp2_ave / len(finall_class[min_class_id])
        if temp1_ave > temp2_ave:
            temp1_ave, temp2_ave = temp2_ave, temp1_ave
        max_score = temp2_ave
        min_score = temp1_ave
        for i in range(need_class):
            if i != max_class_id and i != min_class_id:
                if max_score < every_class[i][subject]:
                    max_score = every_class[i][subject]
                if min_score > every_class[i][subject]:
                    min_score = every_class[i][subject]
        all_range = all_range + max_score - min_score
    return all_range

def change_people(max_class_id, min_class_id, subject):
    global finall_all_range
    for p1 in range(len(finall_class[max_class_id])):
        # 在高分班级中选出高于该科目平均分的人 finall_class[max_class_id][p1]
        if finall_class[max_class_id][p1][subject] > every_class[max_class_id][subject]:
            for p2 in range(len(finall_class[min_class_id])):
                # 预设班级的人不允许交换
                if (book_key.count('预设班级') != 0 and finall_class[max_class_id][p1]['预设班级'] == '' and finall_class[min_class_id][p2]['预设班级'] == '') \
                   or book_key.count('预设班级') == 0:
                    # 在低分班级中选出低于该科目平均分的人 finall_class[min_class_id][p2]
                    if finall_class[max_class_id][p1]['性别'] == finall_class[min_class_id][p2]['性别'] \
                        and finall_class[max_class_id][p1]['分段'] == finall_class[min_class_id][p2]['分段'] \
                        and finall_class[min_class_id][p2][subject] < every_class[min_class_id][subject]:
                        # 计算交换后总极差
                        choice_check = int(random.random() * 2)
                        checkok = False
                        if choice_check == 1:
                            checkok = check1(max_class_id, p1, min_class_id, p2)
                        else:
                            temp_all_range = check2(max_class_id, p1, min_class_id, p2)
                            if temp_all_range < finall_all_range:
                                checkok = True
                        # print(temp_range, finall_all_range)
                        # 若交换后极差变变小则交换
                        if checkok == True:
                            finall_class[max_class_id][p1], finall_class[min_class_id][p2] = finall_class[min_class_id][p2], finall_class[max_class_id][p1]
                            finall_all_range = cal_ave()
if __name__ == '__main__':
    r = Read_Ex()
    all_students = r.read_excel()
    all_students = sorted(all_students, key=itemgetter('总分'), reverse=True)
    need_class = 12
    finall_class = []
    every_class = []
    for i in range(need_class):
        temp_map = {
            '男': 0,
            '女': 0 }
        temp_list = []
        finall_class.append(temp_list)
        every_class.append(temp_map)
    every_level = (int)(20 / need_class) * need_class
    if every_level < 20:
        every_level = every_level + need_class
    now_class_number = 0
    flag = 1
    level_numebr = 1
    now_level_number = 0
    now_every_level = every_level
    boys_number = 0
    girls_number = 0
    every_level_two = 0
    for i in range(len(all_students)):
        if now_class_number<need_class:
            if all_students[i]['性别'] == '男':
                boys_number = boys_number + 1
                every_class[now_class_number]['男'] = every_class[now_class_number]['男'] + 1
            else:
                girls_number = girls_number + 1
                every_class[now_class_number]['女'] = every_class[now_class_number]['女'] + 1
            all_students[i]['分段'] = level_numebr
            now_level_number = now_level_number + 1
            if now_level_number >= now_every_level:
                if i + 1 < len(all_students) and all_students[i + 1]['总分'] == all_students[i]['总分']:
                    now_every_level += need_class
                else:
                    now_level_number = 0
                    level_numebr = level_numebr + 1
                    every_level_two = every_level_two + 1
                    if every_level_two >= 2:
                        now_every_level = now_every_level + every_level
                        every_level_two = 0
            finall_class[now_class_number].append(all_students[i])
            now_class_number = now_class_number + flag
            if now_class_number >= need_class or now_class_number < 0:
                now_class_number = now_class_number - flag
                flag = -flag
        # 调整预设班级
        if book_key.count('预设班级') != 0:
            for i in range(need_class):
                for p1 in range(len(finall_class[i])):
                    go_class = finall_class[i][p1]['预设班级']
                    if go_class != '' and i != int(go_class) - 1:
                        go_class = int(go_class) - 1
                        for p2 in range(len(finall_class[go_class])):
                            if finall_class[i][p1]['性别'] == finall_class[go_class][p2]['性别']:
                                finall_class[i][p1], finall_class[go_class][p2] = finall_class[go_class][p2], finall_class[i][p1]
                                break
    every_boys_number1 = int(boys_number / need_class)
    every_boys_number2 = int(boys_number / need_class)
    if boys_number % need_class != 0:
        every_boys_number2 = every_boys_number2 + 1
    every_girls_number1 = int(girls_number / need_class)
    every_girls_number2 = int(girls_number / need_class)
    if girls_number % need_class != 0:
        every_girls_number2 = every_girls_number2 + 1
    change_sex()
    score_key = []
    flag = 0
    for i in book_key:
        if flag == 1:
            score_key.append(i)
        if i == '性别':
            flag = flag ^ 1
        if i == '总分':
            flag = flag ^ 1
    all_range = cal_ave()
    finall_all_range = all_range
    temp_finall_class = copy.deepcopy(finall_class)
    temp_every_class = copy.deepcopy(every_class)
    ans_range = all_range
    ans_class = []
    ans_every = []
    random_number = 10
    for j_j in range(random_number):
        finall_class = copy.deepcopy(temp_finall_class)
        every_class = copy.deepcopy(temp_every_class)
        finall_all_range = cal_ave()
        for i_i in range(1000):
            subject = score_key[int(random.random() * len(score_key))]
            class1 = int(random.random() * need_class)
            class2 = int(random.random() * need_class)
            if class1 == class2:
                if class2 < need_class - 1:
                    class2 = class2 + 1
                else:
                    class2 = class2 - 1
            change_people(class1, class2, subject)
            print('第', j_j, '次测试总极差值为: ', finall_all_range)
            if finall_all_range < ans_range:
                ans_range = finall_all_range
                ans_class = copy.deepcopy(finall_class)
                ans_every = copy.deepcopy(every_class)
                
                finall_class = copy.deepcopy(ans_class)
                every_class = copy.deepcopy(ans_every)
                finall_all_range = cal_ave()
                print('最终方案误差为: ', finall_all_range)
    workbook = xlwt.Workbook()
    for class_id in range(need_class):
        write_class = copy.deepcopy(finall_class[class_id])
        write_class = sorted(write_class, key=itemgetter('性别', '总分'), reverse=True)
        write_class_boy = []
        write_class_girl = []
        for i in range(len(write_class)):
            if write_class[i]['性别'] == '女':
                write_class_girl.append(write_class[i])
            else:
                write_class_boy.append(write_class[i])
        write_class = write_class_girl + write_class_boy
        sheet = workbook.add_sheet(str(class_id + 1) + '班')
        sheet.write(0, 0, '班内学号')
        for i in range(len(book_key)):
            sheet.write(0, i + 1, book_key[i])
        every_class[class_id]['男'] = 0
        every_class[class_id]['女'] = 0
        for stu_id in range(len(write_class)):
            sheet.write(stu_id + 1, 0, str(stu_id + 1))
            for i in range(len(book_key)):
                sheet.write(stu_id + 1, i + 1, write_class[stu_id][book_key[i]])
            if write_class[stu_id]['性别'] == '男':
                every_class[class_id]['男'] += 1
            else:
                every_class[class_id]['女'] += 1
    sheet = workbook.add_sheet('总情况')
    row_number = 0
    sheet.write(row_number, 0, '班级')
    for i in range(need_class):
        sheet.write(row_number, i + 1, str(i + 1))
    sheet.write(row_number, need_class + 1, '全校')
    sheet.write(row_number, need_class + 2, '最大最小差')
    row_number = row_number + 1
    sheet.write(row_number, 0, '男')
    for i in range(need_class):
        sheet.write(row_number, i + 1, str(every_class[i]['男']))
    sheet.write(row_number, need_class + 1, str(boys_number))
    row_number = row_number + 1
    sheet.write(row_number, 0, '女')
    for i in range(need_class):
        sheet.write(row_number, i + 1, str(every_class[i]['女']))
    sheet.write(row_number, need_class + 1, str(girls_number))
    row_number = row_number + 1
    for subject in score_key:
        sheet.write(row_number, 0, subject + '均分')
        all_score = 0
        max_score = -1
        min_score = 1000000
        for i in range(need_class):
            all_score = all_score + every_class[i]['总分' + subject]
            sheet.write(row_number, i + 1, int(every_class[i][subject] * 100) / 100)
            if max_score < every_class[i][subject]:
                max_score = every_class[i][subject]
            if min_score > every_class[i][subject]:
                min_score = every_class[i][subject]
        all_score = all_score / len(all_students)
        sheet.write(row_number, need_class + 1, str(int(all_score * 100) / 100))
        sheet.write(row_number, need_class + 2, str(int((max_score - min_score) * 100) / 100))
        row_number = row_number + 1
    lv = []
    all_lv_number = 0
    for i in range(need_class):
        lv.append(0)
    for level in range(1, level_numebr + 1):
        for i in range(need_class):
            for p in finall_class[i]:
                if p['分段'] == level:
                    lv[i] = lv[i] + 1
                    all_lv_number = all_lv_number + 1
        sheet.write(row_number, 0, '前' + str(all_lv_number) + '名人数')
        for i in range(need_class):
            sheet.write(row_number, i + 1, str(lv[i]))
        row_number = row_number + 1
    workbook.save('Finall_plan.xls')
    input('\n\n分班结束，分班结果处于代码目录下的 Finall_plan.xls 中，按回车结束程序')