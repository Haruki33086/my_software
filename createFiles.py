# tkinterのインポート
import tkinter as tk
# ファイルダイアログのインポート
from tkinter import filedialog

# 初期値の設定
dir_name =None
head_name = None
extension_name = None
lower_num = 0
upper_num = 1

##### 関数 #####
# ディレクトリパスを取得する関数
def set_func(): 
    # ファイルダイアログメニューの設定
    idir = 'C:\\Users'
    dir_path = filedialog.askdirectory(initialdir = idir)
    # 既存のパスを削除
    input_box.delete(0, tk.END)
    # パスをラベル中に表示
    input_box.insert(tk.END, dir_path)
    
    # ステータスバーの更新 
    statusbar["text"] = "ヘッド名を入力してください"

# 連番のファイルを作成する関数
def run_func():
    tmp = dir_name.replace('/', '\\')
    for i in range (int(lower_num), int(upper_num)+1):
        file_path = tmp + '\\' + head_name + str(i) + extension_name
        with open(file_path, 'w') as f:
            f.write('')
                
    # ステータスバーの更新            
    statusbar["text"] = " Done!!"

# ヘッド名を取得する関数
def get_head_name():
    global head_name
    global dir_name

    dir_name = input_box.get()
    head_name = input_headname.get()

    statusbar["text"] = "拡張子を入力してください"

def get_lower_num():
    global lower_num

    lower_num = input_lower.get()

    statusbar["text"] = "上限を入力してください"

def get_upper_num():
    global upper_num

    upper_num = input_upper.get()

    statusbar["text"] = "RUNを押してください"

# 拡張子名を取得する関数
def get_extension_name():
    global extension_name

    extension_name = input_extension.get()

    statusbar["text"] = "範囲の下限を入力してください"

# Runボタンの例外処理
def exc_run_func():
    try:
        run_func()
    except:
        # ステータスバーの更新
        statusbar["text"] = " Error!!"
    
#####  GUI  #####
# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("450x350")

# Runボタン設置
run_button = tk.Button(root, text = "Run", command = exc_run_func)
run_button.place(x = 190, y = 300)
# 参照ボタン設置
set_button = tk.Button(root, text = "参照", command = set_func)
set_button.place(x = 350, y = 7)
# ヘッド名の入力ボタン設置
head_button = tk.Button(root, text = "入力", command = get_head_name)
head_button.place(x = 350, y = 75)
# 拡張子名の入力ボタン設置
extension_button = tk.Button(root, text = "入力", command = get_extension_name)
extension_button.place(x = 350, y = 140)
# 範囲の下限の入力ボタン設置
lower_button = tk.Button(root, text = "入力", command = get_lower_num)
lower_button.place(x = 350, y = 205)
# 範囲の上限の入力ボタン設置
upper_button = tk.Button(root, text = "入力", command = get_upper_num)
upper_button.place(x = 350, y = 270)
# フォルダパス取得のテキストボックス配置
input_box = tk.Entry(width = 40)
input_box.place(x = 100, y = 10)
# ステータスバー設置
statusbar = tk.Label(root, text = "フォルダを選択してください", bd = 1, relief = tk.SUNKEN, anchor = tk.W)
statusbar.pack(side = tk.BOTTOM, fill = tk.X)
# ヘッド名取得のテキストボックス配置
input_headname = tk.Entry(width = 40)
input_headname.place(x = 100, y = 75)
# フォルダパスラベルの配置
label_ref = tk.Label(root, text="PATH:")
label_ref.place(x=50, y=10, width=35)
# ヘッド名ラベルの配置
label_head = tk.Label(root, text="ヘッド名:")
label_head.place(x=40, y=75, width=45)
# 拡張子名取得のテキストボックス配置
input_extension = tk.Entry(width = 40)
input_extension.place(x = 100, y = 140)
# 拡張子名ラベルの配置
label_extension = tk.Label(root, text="拡張子名：")
label_extension.place(x = 30, y = 140)
# 範囲の下限取得のテキストボックス配置
input_lower = tk.Entry(width = 40)
input_lower.place(x = 100, y = 205)
# 範囲の下限ラベルの配置
label_lower = tk.Label(root, text="下限：")
label_lower.place(x = 50, y = 205)
# 範囲の上限取得のテキストボックス配置
input_upper = tk.Entry(width = 40)
input_upper.place(x = 100, y = 270)
# 範囲の上限ラベルの配置
label_upper = tk.Label(root, text="上限：")
label_upper.place(x = 50, y = 270)

# ウインドウ状態の維持
root.mainloop()