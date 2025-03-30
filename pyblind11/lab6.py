import pyivp


# 創建軌跡
n_path = pyivp.XYSegList()
n_path.add_vertex(0, 0)  # 起點
n_path.add_vertex(0, 10) # 往上
n_path.add_vertex(5, 0)  # 斜向右下
n_path.add_vertex(5, 10) # 直向上
y_path = pyivp.XYSegList()
y_path.add_vertex(10, 10)  # 頂端
y_path.add_vertex(15, 5)   # 左斜下
y_path.add_vertex(20, 10)  # 右斜上
y_path.add_vertex(15, 0)   # 垂直向下
c_path = pyivp.XYSegList()
c_path.add_vertex(25, 10) # 頂端
c_path.add_vertex(20, 10) # 左
c_path.add_vertex(20, 0)  # 下
c_path.add_vertex(25, 0)  # 右
u_path = pyivp.XYSegList()
u_path.add_vertex(30, 10) # 左上
u_path.add_vertex(30, 0)  # 左下
u_path.add_vertex(35, 0)  # 右下
u_path.add_vertex(35, 10) # 右上
print("N:", n_path.get_spec())
print("Y:", y_path.get_spec())
print("C:", c_path.get_spec())
print("U:", u_path.get_spec())

