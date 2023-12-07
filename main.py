from tkinter import *
import pandas as pd
from tkinter import ttk  # for Treeview
from PIL import ImageTk, Image, ImageFile


ImageFile.LOAD_TRUNCATED_IMAGES = True
df_Button = pd.read_excel("CSDL_MON.xlsx", index_col=None)

df_Banhang = pd.read_excel("banhang.xlsx")

df_Order = pd.DataFrame([], columns = ["STT","Tên sản phẩm",
                                       "Đơn giá", "Số lượng",
                                       "Thành tiền"],index=[0])

root = Tk()
root.geometry("800x600")

leftFrame = Frame(root, bg="mistyrose", width=400, heigh=600)
leftFrame.grid(row=0, column=0)
rightFrame = Frame(root, bg="mistyrose", width=400, heigh=600)
rightFrame.grid(row=0, column=1)
tv_index = 0

def BT_callback(m):
    global tv_index
    global df_Order

    product_name = df_Button["Tên sản phẩm"][m]
    product_price = df_Button["Đơn giá"][m]

    # Check if the product already exists in the order
    if product_name in df_Order["Tên sản phẩm"].values:
        # Product exists, update quantity and total price
        df_Order.loc[df_Order["Tên sản phẩm"] == product_name, "Số lượng"] += 1
        df_Order.loc[df_Order["Tên sản phẩm"] == product_name, "Thành tiền"] = \
            df_Order.loc[df_Order["Tên sản phẩm"] == product_name, "Số lượng"] * product_price
    else:
        # New product, add to DataFrame
        print('add new')
        tv_index += 1
        new_entry = {
            "STT": tv_index,
            "Tên sản phẩm": product_name,
            "Đơn giá": product_price,
            "Số lượng": 1,
            "Thành tiền": product_price
        }
        print(df_Order)
        print(new_entry)
        # add_order = pd.DataFrame(new_entry, index=[0])
        # print(add_order)
        # df_Order = df_Order.append(new_entry, ignore_index=True)
        df_Order.loc[len(df_Order)] = new_entry

    # Update the Treeview
    tv.delete(*tv.get_children())
    for index, row in df_Order.iterrows():
        tv.insert("", index, values=row.tolist())

    # Update the total price labels
    update_total_price_labels()

def update_total_price_labels():
    total_price = df_Order["Thành tiền"].sum()
    LB_Sum_KQ.config(text=str(total_price) + "đ")
    LB_VAT_KQ.config(text=str(0.1 * total_price) + "đ")
    LB_Total_KQ.config(text=str(round(1.1 * total_price, 0)) + "đ")


def NhapMoi_Callback():
    global tv_index
    global df_Order
    tv.delete(*tv.get_children())
    tv_index = 0
    df_Order = pd.DataFrame([], columns = ["STT","Tên sản phẩm",
                                       "Đơn giá", "Số lượng",
                                       "Thành tiền"])
def ThanhToan_Callback():
    global df_Order
    global df_Banhang
    df_Banhang = df_Banhang._append(df_Order)
    df_Banhang.to_excel("banhang.xlsx",index=False) 
   
# Button creation
BT_list = []
BT_Photo = []
BT_Frame = []
BT_Label = []
BT_Price = []
for i in range(0,df_Button.shape[0]):
    BT_Frame.append(Frame(leftFrame,width=130, heigh = 200))
    BT_Frame[i].grid(row = i//3, column = i%3)
    file_name = df_Button["Mã SP"][i].strip()+".png"
    # file_name = ''
    image = Image.open(file_name)
    photo = ImageTk.PhotoImage(image)
    BT_Photo.append(photo)
    BT_list.append(Button(BT_Frame[i],
                          image = BT_Photo[i],
                          command = lambda m=i: BT_callback(m)))
    BT_list[i].grid(row=0, column=0)
    BT_Label.append(Label(BT_Frame[i],text=df_Button["Tên sản phẩm"][i]))
    BT_Label[i].grid(row=1,column=0)
    BT_Price.append(Label(BT_Frame[i],text=df_Button["Đơn giá"][i]))
    BT_Price[i].grid(row=2,column=0)

rightFrameUpper = Frame(rightFrame,width=400,heigh=400,bg='mistyrose')
rightFrameUpper.grid(row=0, column=0)

tv = ttk.Treeview(rightFrameUpper)
tv['columns']=['STT', 'Tên sản phẩm', 'Đơn giá',
               'Số lượng', 'Thành  tiền']
tv.column('#0', width=0, stretch=NO)
tv.column('STT', anchor=CENTER, width=80)
tv.column('Tên sản phẩm', anchor=CENTER, width=80)
tv.column('Đơn giá', anchor=CENTER, width=80)
tv.column('Số lượng', anchor=CENTER, width=80)
tv.column('Thành  tiền', anchor=CENTER, width=80)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('STT', text='STT', anchor=CENTER)
tv.heading('Tên sản phẩm', text='Tên sản phẩm', anchor=CENTER)
tv.heading('Đơn giá', text='Đơn giá', anchor=CENTER)
tv.heading('Số lượng', text='Số lượng', anchor=CENTER)
tv.heading('Thành  tiền', text='Thành  tiền', anchor=CENTER)
tv.grid(row=0, column=0)

rightFrameLower = Frame(rightFrame,width=400,heigh=200,bg='mistyrose')
rightFrameLower.grid(row=1, column=0)
LB_Customer = Label(rightFrameLower,text = "Khách hàng:",bg ="pink",width=10)
LB_Customer.grid(row=0, column=0)
ET_Customer = Entry(rightFrameLower,width=20)
ET_Customer.grid(row=1, column=0)

LB_Phone = Label(rightFrameLower,text = "SĐT:",bg="pink")
LB_Phone.grid(row=2, column=0)
ET_Phone = Entry(rightFrameLower)
ET_Phone.grid(row=3, column=0)

LB_Sum = Label(rightFrameLower,text = "Cộng:",bg="lavenderblush",width=10)
LB_Sum.grid(row=0, column=1)
LB_VAT = Label(rightFrameLower,text = "VAT(10%)",bg="lavenderblush",width=10)
LB_VAT.grid(row=1, column=1)
LB_Total = Label(rightFrameLower,text = "Tổng cộng:",bg="lavenderblush",width=10)
LB_Total.grid(row=2, column=1)

LB_Sum_KQ = Label(rightFrameLower,text = "0đ",bg="lavenderblush",width=10)
LB_Sum_KQ.grid(row=0, column=2)
LB_VAT_KQ = Label(rightFrameLower,text = "0đ",bg="lavenderblush",width=10)
LB_VAT_KQ.grid(row=1, column=2)
LB_Total_KQ = Label(rightFrameLower,text = "0đ",bg="lavenderblush",width=10)
LB_Total_KQ.grid(row=2, column=2)

BT_Nhapmoi = Button(rightFrameLower,text = "Nhập mới", bg="lavender",
                    command = NhapMoi_Callback)
BT_Nhapmoi.grid(row=4, column=0)
BT_ThanhToan = Button(rightFrameLower,text = "Thanh Toán", bg="oldlace",
                      command = ThanhToan_Callback)
BT_ThanhToan.grid(row=4, column=1, columnspan=2)
root.mainloop()
