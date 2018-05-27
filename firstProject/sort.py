# 插入排序
def insert_sort(origin_list):
    for i in range(0, len(origin_list)):
        if origin_list[i] > origin_list[i + 1]:
            origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]


origin_list = [5, 3, 1, 7, 9, 8]
insert_sort(origin_list)
print(origin_list)


# 冒泡排序
def bubble_sort(origin_list):
    for i in range(len(origin_list), 0, -1):
        for j in range(i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]


origin_list = [5, 3, 1, 7, 9, 8]
bubble_sort(origin_list)
print(origin_list)

# 快速排序


# 归并排序
