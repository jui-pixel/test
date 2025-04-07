import pyivp
import matplotlib.pyplot as plt

# 创建轨迹
n_path = pyivp.XYSegList()
n_path.add_vertex(0, 0, 0, "")  # 起点
n_path.add_vertex(0, 2, 0, "") # 往上
n_path.add_vertex(1, 0, 0, "")  # 斜向右下
n_path.add_vertex(1, 2, 0, "") # 直向上

y_path = pyivp.XYSegList()
y_path.add_vertex(2, 2, 0, "")  # 顶端
y_path.add_vertex(3, 1, 0, "")   # 左斜下
y_path.add_vertex(4, 2, 0, "")  # 右斜上
y_path.add_vertex(3, 1, 0, "")   # 左斜下
y_path.add_vertex(3, 0, 0, "")   # 垂直向下

c_path = pyivp.XYSegList()
c_path.add_vertex(6, 2, 0, "") # 顶端
c_path.add_vertex(5, 2, 0, "") # 左
c_path.add_vertex(5, 0, 0, "")  # 下
c_path.add_vertex(6, 0, 0, "")  # 右

u_path = pyivp.XYSegList()
u_path.add_vertex(7, 2, 0, "") # 左上
u_path.add_vertex(7, 0, 0, "")  # 左下
u_path.add_vertex(8, 0, 0, "")  # 右下
u_path.add_vertex(8, 2, 0, "") # 右上
# 传递参数给 get_spec 方法
print("N:", n_path.get_spec("spec"))
print("Y:", y_path.get_spec("spec"))
print("C:", c_path.get_spec("spec"))
print("U:", u_path.get_spec("spec"))
# 获取顶点坐标
def get_coords(path):
    x = []
    y = []
    for i in range(path.size()):
        x.append(path.get_vx(i))
        y.append(path.get_vy(i))
    return x, y

# 获取各路径的顶点坐标
n_x, n_y = get_coords(n_path)
y_x, y_y = get_coords(y_path)
c_x, c_y = get_coords(c_path)
u_x, u_y = get_coords(u_path)

# 绘制路径
plt.figure(figsize=(10, 10))
plt.plot(n_x, n_y, marker='o', label='N')
plt.plot(y_x, y_y, marker='o', label='Y')
plt.plot(c_x, c_y, marker='o', label='C')
plt.plot(u_x, u_y, marker='o', label='U')

# 设置图形属性
plt.title('NYCU Path')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# 显示图形
plt.show()
