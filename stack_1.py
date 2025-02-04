# スタック実装用テンプレート

def stack_push(x):
    stack_list.append(x)
    
    # デバッグ用
    # print(" ".join(stack_list))

def stack_pop():
    print(stack_list[-1])
    stack_list.pop()
    
    # デバッグ用
    # print(" ".join(stack_list))

stack_list = []
