# キュー実装用テンプレート

# enqueue：キューにデータを入れる
def enqueue(x):
    queue_list.append(x)
    
    # デバッグ用
    # print(" ".join(queue_list))

# dequeue：キューからデータを取り出す
def dequeue():
    print(queue_list[0])
    queue_list.pop(0)
    
    # デバッグ用
    # print(" ".join(queue_list))

queue_list = []
