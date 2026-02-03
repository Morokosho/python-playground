tasklist = []

def main():
    print('----- Todo App -----')
    print('1.タスク追加')
    print('2.タスク削除')
    print('3.全てのタスク削除')
    print('4.一覧表示')
    print('5.タスクを保存する')
    print('6.タスクファイルを読み込む')
    print('0.終了')

    choice = input('選択してください：')
    
    print('選択：' + choice)
    return choice

def add_task():
    meeage = input('追加するものを入力してください：')
    tasklist;
    tasklist.append(meeage);
    print('----- Add Task -----')

def delete_task():
    if not tasklist:
        print('----- No Task -----')
        return
    
    print('----- タスク一覧 -----')
    for i, task in enumerate(tasklist, start=1):
        print(f'{i}. {task}')


    num = input(f'タスクが{len(tasklist)}個あります。どれを削除しますか？（0でキャンセル）:')
    while True:
        if not num.isdigit():
            print('数字を入力してくだいさ。')

        num = int(num)

        if num == 0:
            break

        if num < 1 or num > len(tasklist):
            print('該当するタスクがありません。')
            print('----------')
            break

        tasklist.pop(num - 1)
        print('----- Delete Task -----')
        break


def delete_all_task():
    if not tasklist:
        print('----- No Task -----')
        return
    
    tasklist.clear()
    print('----- Delete All Task -----')

def show_all():
    print('タスクの一覧を表示します')
    [print(i) for i in tasklist];
    print('--------------------')

def close_app():
    print('----- Finish -----')

def save_task():
    if not tasklist:
        print('----- No Task -----')
        return
    
    with open(r'D:\Study\Python\todo_app\tasks.txt', 'w', encoding='UTF-8') as f:
        for task in tasklist:
            f.write(task + '\n')

    print('----- Save Task -----')

def load_task():
    try:
        with open(r'D:\Study\Python\todo_app\tasks.txt', 'r', encoding='UTF-8') as f:
            tasklist.clear()
            for task in f:
                tasklist.append(task.strip());

        print('----- Load Task -----')        
    except FileNotFoundError:
        print('----- 保存されたタスクがありません -----')



while True:
    choice = main()
    if choice == '1':
        add_task()
    elif choice == '2':
        delete_task()
    elif choice == '3':
        delete_all_task()
    elif choice == '4':
        show_all()
    elif choice == '5':
        save_task()
    elif choice == '6':
        load_task()
    elif choice == '0':
        close_app()
        break
    elif not choice.isdigit():
        print('数字を入力してくだいさ。')

