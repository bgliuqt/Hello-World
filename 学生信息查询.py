# 学生管理系统

import os
import os.path

# 创建student.txt文件
filename = "student.txt"


def main():
    while True:
        menu()

        # 判断输入是否为数字
        try:
            choice = int(input("请选择操作选项："))
        except:
            print("★\t输入不合法，请重新输入")
            continue
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("确定退出系统吗？(y/n)：")
                if answer == "y" or answer == "Y":
                    print("已退出，感谢您的使用！")
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入函数
            elif choice == 2:
                search()  # 查找函数
            elif choice == 3:
                delete()  # 删除函数
            elif choice == 4:
                modify()  # 修改函数
            elif choice == 5:
                sort()  # 排序函数
            elif choice == 6:
                total()  # 统计函数
            elif choice == 7:
                show()  # 显示函数
        else:
            print("★\t输入不合法，请重新输入")
            continue


# 主菜单
def menu():
    print("=" * 20, "学生信息管理系统", "=" * 20)
    print("★" * 24, "欢迎使用", "★" * 24)
    print("\t>> 1.录入学生信息")
    print("\t>> 2.查找学生信息")
    print("\t>> 3.删除学生信息")
    print("\t>> 4.修改学生信息")
    print("\t>> 5.根据条件排序")
    print("\t>> 6.统计学生人数")
    print("\t>> 7.显示学生信息")
    print("\t>> 0.退出管理系统")
    print("=" * 24, "欢迎使用", "=" * 24)


def insert():
    student_list = []
    while True:
        flag1 = 0
        id = input("请输入ID(例如10001)：")

        # 判定ID是否存在
        with open(filename, "r", encoding="utf-8") as rfile:
            student = rfile.readlines()
            for item in student:
                d = dict(eval(item))
                if str(id) == str(d["id"]):
                    flag1 = 1
                    break
                else:
                    continue
                print(d)
        if flag1:
            print("此id已经存在，请勿重复输入......")
            return
        if not id:
            print("输入不合法......")
            break
        name = input("请输入姓名：")
        if not name:
            print("输入不合法......")
            break
        try:
            chinese_score = int(input("请输入语文成绩："))
            math_score = int(input("请输入数学成绩："))
            python_score = int(input("请输入Python成绩："))
        except:
            print("★\t输入无效，请重新输入：")
            continue
        # 将学生信息保存到字典
        student = {
            "id": id,
            "name": name,
            "语文": chinese_score,
            "数学": math_score,
            "Python": python_score,
        }

        # 将学生信息添加到列表
        student_list.append(student)

        answer = input("是否继续添加？y/n:")
        if answer == "y" or answer == "Y":
            save(student_list)
            continue
        else:
            print()
            print("学生信息录入完毕......")
            break
    #  调用save()函数保存信息
    save(student_list)


def save(lst):
    try:
        stu_txt = open(filename, "a", encoding="utf-8")
    except:
        stu_txt = open(filename, "w", encoding="utf-8")
    for item in lst:
        stu_txt.write(str(item) + "\n")
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("按ID查找请输入1，按姓名查找请输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入学生姓名：")
            else:
                print("★\t输入有误，请重新输入：")
                search()
            with open(filename, "r", encoding="utf-8") as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != "":
                        if d["id"] == id:
                            student_query.append(d)
                    elif name != "":
                        if d["name"] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input("是否需要继续查询？y/n：")
            if answer == "y" or answer == "Y":
                continue
            else:
                break
        else:
            print("暂未保存学生信息")
            return


def show_student(lst):
    if len(lst) == 0:
        print("没有查询到学生信息，无数据显示！！")
        return
    # 定义标题显示格式
    format_title = "{:^1}\t{:^1}\t{:^1}\t{:^1}\t{:^1}\t{:^8}"
    print(format_title.format("ID", "姓名", "语文", "数学", "Python", "总成绩"))
    print("-" * 48)
    # 定义内容显示格式
    format_date = "{:^1}\t{:^1}\t{:^1}\t{:^1}\t{:^1}\t{:^8}"
    for item in lst:
        print(
            format_date.format(
                item.get("id"),
                item.get("name"),
                item.get("语文"),
                item.get("数学"),
                item.get("Python"),
                int(item.get("语文") + item.get("数学") + item.get("Python")),
            )
        )
    print()


def delete():
    while True:
        student_id = input("请输入要删除的学生的ID：")
        if student_id != "":
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, "w", encoding="utf-8") as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 把字典转成字符串
                        if d["id"] != student_id:
                            wfile.write(str(d) + "\n")
                        else:
                            flag = True
                    if flag:
                        print(f"ID为{student_id}的学生信息已删除")
                    else:
                        print(f"没找到ID为{student_id}的学生")
            else:
                print("无学生信息")
                break
            show()
            answer = input("是否继续删除？y/n：")
            if answer == "y" or answer == "Y":
                continue
            else:
                break
        else:
            print("输入为空")
            break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            student_old = rfile.readlines()
            if student_old == []:
                print("学生信息文件为空，请先录入信息")
                return
            else:
                print("已读取文件信息......")
    else:
        print("找不到学生信息文件")
        return
    student_id = input("请输入要修改的学生ID：")

    with open(filename, "w", encoding="utf-8") as wfile:
        count_num = False
        for item in student_old:
            d = dict(eval(item))
            if student_id == d["id"]:
                print("找到学生信息，可以修改")
                while True:
                    try:
                        d["name"] = input("请输入修改名字：")
                        d["语文"] = int(input("请输入语文成绩："))
                        d["数学"] = int(input("请输入数学成绩："))
                        d["Python"] = int(input("请输入Python成绩："))
                    except:
                        print("输入有误，请重新输入")
                    else:
                        break
                print("修改成功！")
            else:
                count_num = True

            wfile.write(str(d) + "\n")
        if count_num :
            print("没有此学生的信息，请重新输入！")
    answer = input("是否继续修改学生信息？y/n：")
    if answer == "y" or answer == "Y":
        modify()
    else:
        return


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc = input("请选择（0.升序  1.降序）：")
    if asc_or_desc == "0":
        asc_or_desc_bool = False
    elif asc_or_desc == "1":
        asc_or_desc_bool = True
    else:
        print("★您的输入有误，请重新输入：")
        sort()
    mode = input("请选择排序方式（1.语文成绩排序 2.按数学成绩排序 3.按Python成绩排序 0.按总成绩排序）：")
    if mode == "1":
        student_new.sort(key=lambda X: int(X["语文"]), reverse=asc_or_desc_bool)
    elif mode == "2":
        student_new.sort(key=lambda X: int(X["数学"]), reverse=asc_or_desc_bool)
    elif mode == "3":
        student_new.sort(key=lambda X: int(X["Python"]), reverse=asc_or_desc_bool)
    elif mode == "0":
        student_new.sort(
            key=lambda X: int(X["语文"]) + int(X["数学"]) + int(X["Python"]),
            reverse=asc_or_desc_bool,
        )
    else:
        print("★\t您的输入有误，请重新输入！！！")
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            students = rfile.readlines()
            if students:
                print(f"一共有{len(students)}名学生")
            else:
                print("还没有录入学生信息......")
    else:
        print("暂未保存数据信息...")


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            else:
                print("学生信息为空......")


if __name__ == "__main__":
    main()

