import pickle

def save_list_to_file(data_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data_list, file)

def load_list_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# 初始化列表
original_list = [1, 2, 3, 4, 5]

# 保存列表到文件
save_list_to_file(original_list, 'list_data.pkl')

# 从文件中加载数据
loaded_list = load_list_from_file('list_data.pkl')

# 比较原始列表和加载后的列表
assert original_list == loaded_list, "The lists do not match!"

print("The lists match!")
