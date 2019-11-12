from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Window:
    
    def __init__(self, root):

        self.root = root
        self.root.title('Management System')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        try:
            self.con = mysql.connector.connect(host='localhost',
                                               user='root',
                                               password='root',
                                               database='softwarica')

            self.cur = self.con.cursor()

        except mysql.connector.Error:
            messagebox.showwarning('Database Connection Error!')

        # frame

        self.frame1 = Frame(self.root, bd=4, relief=RIDGE)
        self.frame1.place(x=0, width=500, height=500)

        self.frame2 = Frame(self.root, bd=2, relief=RIDGE)
        self.frame2.place(x=500, width=300, height=250)

        self.frame3 = Frame(self.root, bd=4, relief=RIDGE)
        self.frame3.place(x=0, y=500, width=800, height=100)

        self.btn_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.btn_frame.place(x=500, y=250, width=300, height=250)

        # Scrollbar

        self.scroll_x = Scrollbar(self.frame1, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)

        self.scroll_y = Scrollbar(self.frame1, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        # treeview

        self.student_table = ttk.Treeview(self.frame1, column=(
                                                        'student_id',
                                                        'first_name',
                                                        'last_name',
                                                        'degree',
                                                        'address',
                                                        'contact_no'), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.student_table.heading('student_id', text="Id")
        self.student_table.heading('first_name', text="First Name")
        self.student_table.heading('last_name', text="Last Name")
        self.student_table.heading('degree', text="Degree")
        self.student_table.heading('address', text="Address")
        self.student_table.heading('contact_no', text="Contact Number")
        self.student_table['show'] = 'headings'

        self.student_table.column('student_id', width=120)
        self.student_table.column('first_name', width=120)
        self.student_table.column('last_name', width=120)
        self.student_table.column('degree', width=120)
        self.student_table.column('address', width=120)
        self.student_table.column('contact_no', width=120)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.show()

        self.student_table.bind('<ButtonRelease-1>', self.pointer)
        self.student_table.pack(fill=BOTH, expand=True)

        # Inside frame2

        self.s_id = Label(self.frame2, text='Student ID')
        self.s_id.grid(row=0, column=0, padx=10, pady=10)
        self.es_id = Entry(self.frame2)
        self.es_id.grid(row=0, column=1, padx=10, pady=10)

        self.f_name = Label(self.frame2, text='First Name')
        self.f_name.grid(row=1, column=0, padx=10, pady=10)
        self.ef_name = Entry(self.frame2)
        self.ef_name.grid(row=1, column=1, padx=10, pady=10)

        self.l_name = Label(self.frame2, text='Last name')
        self.l_name.grid(row=2, column=0, padx=10, pady=10)
        self.el_name = Entry(self.frame2)
        self.el_name.grid(row=2, column=1, padx=10, pady=10)

        self.combo_lbl = Label(self.frame2, text='Degree')
        self.combo_lbl.grid(row=5, column=0, padx=10, pady=10)

        self.combo1 = ttk.Combobox(self.frame2, values=['Computing', 'Ethical Hacking'])
        self.combo1.set('Computing')
        self.combo1.grid(row=5, column=1, padx=10, pady=10)

        self.address = Label(self.frame2, text='Address')
        self.address.grid(row=3, column=0, padx=10, pady=10)
        self.e_address = Entry(self.frame2)
        self.e_address.grid(row=3, column=1, padx=10, pady=10)

        self.contact = Label(self.frame2, text='Contact')
        self.contact.grid(row=4, column=0, padx=10, pady=10)
        self.e_contact = Entry(self.frame2)
        self.e_contact.grid(row=4, column=1, padx=10, pady=10)

        # frame2buttons
        self.add_button = Button(self.btn_frame, text='Add', width=8, height=2, relief=RAISED, fg='green',
                                 command=self.add)
        self.add_button.place(x=10, y=10, width=100, height=50)

        self.btn_update = Button(self.btn_frame, text='Update', width=8, height=2, relief=RAISED, fg='blue',
                                 command=self.update)
        self.btn_update.place(x=180, y=10, width=100, height=50)

        self.delete = Button(self.btn_frame, text='Delete', width=8, height=2, relief=RAISED, fg='red',
                             command=self.delete)
        self.delete.place(x=10, y=90, width=100, height=50)

        self.btn_clear = Button(self.btn_frame, text='Clear', width=8, height=2, relief=RAISED, fg='red',
                                command=self.clear)
        self.btn_clear.place(x=180, y=90, width=100, height=50)

        self.btn_showall = Button(self.btn_frame, text='Show all', width=8, height=2, relief=RAISED, fg='blue',
                                  command=self.show)
        self.btn_showall.place(x=95, y=170, width=100, height=50)

        # search

        self.lbl_search = Label(self.frame3, text='Search By')
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        self.combo_search = ttk.Combobox(self.frame3)
        self.combo_search['values'] = ('Student ID', 'First name', 'Last name', 'Degree', 'Address', 'Contact')
        self.combo_search.set('Student ID')
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_search_text = Label(self.frame3, text='Search text')
        self.lbl_search_text.grid(row=1, column=0, padx=10, pady=10)

        self.esearch = Entry(self.frame3)
        self.esearch.grid(row=1, column=1, padx=10, pady=10)

        self.btn_Search = Button(self.frame3, text='Search', relief=RAISED, command=self.search)
        self.btn_Search.grid(row=0, column=3, rowspan=2, ipadx=30, ipady=10)

        # sort
        self.sort_lbl = Label(self.frame3, text='Sort by')
        self.sort_lbl.place(x=400, y=30)

        self.sort_combo = ttk.Combobox(self.frame3)
        self.sort_combo['values'] = ('Student ID', 'First name', 'Last name', 'Degree', 'Address', 'Contact')
        self.sort_combo.set('Student ID')
        self.sort_combo.place(x=480, y=8)

        self.sort_combo1 = ttk.Combobox(self.frame3)
        self.sort_combo1['values'] = ('Ascending', 'Descending')
        self.sort_combo1.set('Ascending')
        self.sort_combo1.place(x=480, y=50)
        self.btn_sort = Button(self.frame3, text='Sort', command=self.sort)
        self.btn_sort.place(x=660, y=15, width=80, height=50)


    # functions

    def add(self):
        student_id = int(self.es_id.get())
        first_name = self.ef_name.get()
        last_name = self.el_name.get()
        degree = self.combo1.get()
        address = self.e_address.get()
        contact_no = self.e_contact.get()

        query = 'insert into student_info values(%s,%s,%s,%s,%s,%s)'
        values = (student_id, first_name, last_name, degree, address, contact_no)
        self.cur.execute(query, values)
        print('Data saved successfully')
        self.con.commit()
        self.show()
        self.clear()

    def show(self):
        query = 'select * from student_info'
        self.cur.execute(query)
        self.result5 = self.cur.fetchall()

        if len(self.result5) != None:
            self.student_table.delete(*self.student_table.get_children())
        for row in self.result5:
            self.student_table.insert('', END, values=row)
            self.con.commit()

    def delete(self):
        student_id = int(self.es_id.get())
        query = 'delete from student_info where student_id=%s'
        values = (student_id,)
        self.cur.execute(query, values)
        # print('data deleted successfully')
        self.clear()
        self.con.commit()
        self.show()

    def clear(self):
        self.es_id.delete(0, END)
        self.ef_name.delete(0, END)
        self.el_name.delete(0, END)
        self.e_address.delete(0, END)
        self.e_contact.delete(0, END)
        self.combo1.delete(0, END)
        self.combo_search.delete(0, END)

    def pointer(self, event):
        point = self.student_table.focus()
        content = self.student_table.item(point)
        row = content['values']
        self.clear()
        self.es_id.insert(0, row[0])
        self.ef_name.insert(0, row[1])
        self.el_name.insert(0, row[2])
        self.e_address.insert(0, row[4])
        self.e_contact.insert(0, row[5])
        self.combo1.insert(0, row[3])

    def update(self):
        query = 'update student_info set first_name=%s,last_name=%s,degree=%s,address=%s,contact_no=%s where ' \
                'student_id=%s'
        self.student_id = int(self.es_id.get())
        self.first_name = self.ef_name.get()
        self.last_name = self.el_name.get()
        self.address = self.e_address.get()
        self.contact_no = int(self.e_contact.get())
        self.degree = self.combo1.get()
        values = (self.first_name, self.last_name, self.degree, self.address, self.contact_no, self.student_id)
        self.cur.execute(query, values)
        self.con.commit()
        self.show()
        self.clear()

    def search(self,list=None):
        if not list:
            self.thelist = 'select * from student_info'
            self.cur.execute(self.thelist)
            result = self.cur.fetchall()
        else:
            result = list

        if self.combo_search.get() == 'Student ID':
            self.column = 0
        elif self.combo_search.get() == 'First name':
            self.column = 1
        elif self.combo_search.get() == 'Last name':
            self.column = 2
        elif self.combo_search.get() == 'Address':
            self.column = 3
        elif self.combo_search.get() == 'Contact':
            self.column = 4
        else:
            self.column = 5

        self.list_of_found_item = []

        for row in result:
            print(row)
            if self.esearch.get() == row[self.column]:
                self.list_of_found_item.append(row)

        if len(self.list_of_found_item) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for row in self.list_of_found_item:
            self.student_table.insert('', 'end', values=row)


    def partition(self, sort_array, low, high):
        sort_by = self.sort_combo.get()
        if sort_by == "Student id":
            column_index = 0
        elif sort_by == "First name":
            column_index = 1
        elif sort_by == "Last name":
            column_index = 2
        elif sort_by == "Degree":
            column_index = 3
        elif sort_by == "Address":
            column_index = 4
        else:
            column_index = 5

        order_by = self.sort_combo1.get()
        if order_by == "Ascending":
            i = (low - 1)
            pivot = sort_array[high][column_index]
            for j in range(low, high):
                if sort_array[j][column_index] <= pivot:
                    i += 1
                    sort_array[i], sort_array[j] = sort_array[j], sort_array[i]
            sort_array[i + 1], sort_array[high] = sort_array[high], sort_array[i + 1]
            return i + 1
        else:
            i = (low - 1)
            pivot = sort_array[high][column_index]
            for j in range(low, high):
                if sort_array[j][column_index] >= pivot:
                    i += 1
                    sort_array[i], sort_array[j] = sort_array[j], sort_array[i]
            sort_array[i + 1], sort_array[high] = sort_array[high], sort_array[i + 1]
            return i + 1

    def quick_sort(self, sort_array, low, high):
        if low < high:
            pi = self.partition(sort_array, low, high)
            self.quick_sort(sort_array, pi + 1, high)
            self.quick_sort(sort_array, low, pi - 1)

    def sort(self):
        query = 'select * from student_info'
        self.cur.execute(query)
        results = self.cur.fetchall()

        self.quick_sort(results, 0, len(results) - 1)

        records = self.student_table.get_children()
        self.student_table.delete(*records)
        for row in results:
            self.student_table.insert("", "end", values=row)

window1 = Tk()
w = Window(window1)
window1.mainloop()
