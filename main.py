import tkinter as tk
from tkinter import ttk
from tkinter import Menu, CENTER, SUNKEN, RIGHT, RAISED, BOTTOM, W, E, NORMAL, FLAT
from tkinter import messagebox as msg
import re
import math
import random


class Weekly:
    routine_disabled_state = False
    check_disabled_state = True
    attendance_percent_clicked = False
    classes_to_attend_clicked = False
    total_subjects_is_zero = True
    select_class_executed = False
    attendance_percent_calculated = False
    ok_button_clicked = False
    refresh_button_clicked = False  # not used
    total_subjects = 0
    checkButton_enabled_count = 0
    count_for_correct_timing = 0
    count_for_default_time_value = 0
    count_for_unacceptable_value = 0
    count_routine_to_calculate_classes_to_attend = 0
    select_class_executed_count = 0
    highlighted_subject_count = 0
    count_classes_to_attend = 0
    disable_checkButton_list = []
    valid_entry_chkBox_list = []
    list_for_classes_to_attend = []
    disable_entry_list = []
    highlight_entry_list = []

    def __init__(self):
        self.win_root = tk.Tk()
        self.win_root.title("Attendance Manager")

        self.timing_1 = tk.StringVar()
        self.timing_2 = tk.StringVar()
        self.timing_3 = tk.StringVar()
        self.timing_4 = tk.StringVar()
        self.timing_5 = tk.StringVar()

        self.sub_name_11 = tk.StringVar()
        self.sub_name_12 = tk.StringVar()
        self.sub_name_13 = tk.StringVar()
        self.sub_name_14 = tk.StringVar()
        self.sub_name_15 = tk.StringVar()

        self.sub_name_21 = tk.StringVar()
        self.sub_name_22 = tk.StringVar()
        self.sub_name_23 = tk.StringVar()
        self.sub_name_24 = tk.StringVar()
        self.sub_name_25 = tk.StringVar()

        self.sub_name_31 = tk.StringVar()
        self.sub_name_32 = tk.StringVar()
        self.sub_name_33 = tk.StringVar()
        self.sub_name_34 = tk.StringVar()
        self.sub_name_35 = tk.StringVar()

        self.sub_name_41 = tk.StringVar()
        self.sub_name_42 = tk.StringVar()
        self.sub_name_43 = tk.StringVar()
        self.sub_name_44 = tk.StringVar()
        self.sub_name_45 = tk.StringVar()

        self.sub_name_51 = tk.StringVar()
        self.sub_name_52 = tk.StringVar()
        self.sub_name_53 = tk.StringVar()
        self.sub_name_54 = tk.StringVar()
        self.sub_name_55 = tk.StringVar()

        self.sub_name_61 = tk.StringVar()
        self.sub_name_62 = tk.StringVar()
        self.sub_name_63 = tk.StringVar()
        self.sub_name_64 = tk.StringVar()
        self.sub_name_65 = tk.StringVar()

        self.checkVar_11 = tk.IntVar()
        self.checkVar_12 = tk.IntVar()
        self.checkVar_13 = tk.IntVar()
        self.checkVar_14 = tk.IntVar()
        self.checkVar_15 = tk.IntVar()

        self.checkVar_21 = tk.IntVar()
        self.checkVar_22 = tk.IntVar()
        self.checkVar_23 = tk.IntVar()
        self.checkVar_24 = tk.IntVar()
        self.checkVar_25 = tk.IntVar()

        self.checkVar_31 = tk.IntVar()
        self.checkVar_32 = tk.IntVar()
        self.checkVar_33 = tk.IntVar()
        self.checkVar_34 = tk.IntVar()
        self.checkVar_35 = tk.IntVar()

        self.checkVar_41 = tk.IntVar()
        self.checkVar_42 = tk.IntVar()
        self.checkVar_43 = tk.IntVar()
        self.checkVar_44 = tk.IntVar()
        self.checkVar_45 = tk.IntVar()

        self.checkVar_51 = tk.IntVar()
        self.checkVar_52 = tk.IntVar()
        self.checkVar_53 = tk.IntVar()
        self.checkVar_54 = tk.IntVar()
        self.checkVar_55 = tk.IntVar()

        self.checkVar_61 = tk.IntVar()
        self.checkVar_62 = tk.IntVar()
        self.checkVar_63 = tk.IntVar()
        self.checkVar_64 = tk.IntVar()
        self.checkVar_65 = tk.IntVar()

        self.year = tk.IntVar()

        self.day_1 = tk.IntVar()
        self.month_1 = tk.StringVar()

        self.day_2 = tk.IntVar()
        self.month_2 = tk.StringVar()

        self.day_3 = tk.IntVar()
        self.month_3 = tk.StringVar()

        self.day_4 = tk.IntVar()
        self.month_4 = tk.StringVar()

        self.day_5 = tk.IntVar()
        self.month_5 = tk.StringVar()

        self.day_6 = tk.IntVar()
        self.month_6 = tk.StringVar()

        self.percent = tk.DoubleVar()
        self.attend_class = tk.DoubleVar()

        self.create_labels()
        self.create_time()
        self.create_date()
        self.create_routine()
        self.create_functions_button()

        self.entry_list = [self.sub_entry_11, self.sub_entry_12, self.sub_entry_13, self.sub_entry_14,
                           self.sub_entry_15, self.sub_entry_21, self.sub_entry_22, self.sub_entry_23,
                           self.sub_entry_24, self.sub_entry_25, self.sub_entry_31, self.sub_entry_32,
                           self.sub_entry_33, self.sub_entry_34, self.sub_entry_35, self.sub_entry_41,
                           self.sub_entry_42, self.sub_entry_43, self.sub_entry_44, self.sub_entry_45,
                           self.sub_entry_51, self.sub_entry_52, self.sub_entry_53, self.sub_entry_54,
                           self.sub_entry_55, self.sub_entry_61, self.sub_entry_62, self.sub_entry_63,
                           self.sub_entry_64, self.sub_entry_65]

        self.check_button_list = [self.chk_11, self.chk_12, self.chk_13, self.chk_14, self.chk_15,
                                  self.chk_21, self.chk_22, self.chk_23, self.chk_24, self.chk_25,
                                  self.chk_31, self.chk_32, self.chk_33, self.chk_34, self.chk_35,
                                  self.chk_41, self.chk_42, self.chk_43, self.chk_44, self.chk_45,
                                  self.chk_51, self.chk_52, self.chk_53, self.chk_54, self.chk_55,
                                  self.chk_61, self.chk_62, self.chk_63, self.chk_64, self.chk_65]

        self.check_variables_list = [self.checkVar_11, self.checkVar_12, self.checkVar_13,
                                     self.checkVar_14, self.checkVar_15, self.checkVar_21,
                                     self.checkVar_22, self.checkVar_23, self.checkVar_24,
                                     self.checkVar_25, self.checkVar_31, self.checkVar_32,
                                     self.checkVar_33, self.checkVar_34, self.checkVar_35,
                                     self.checkVar_41, self.checkVar_42, self.checkVar_43,
                                     self.checkVar_44, self.checkVar_45, self.checkVar_51,
                                     self.checkVar_52, self.checkVar_53, self.checkVar_54,
                                     self.checkVar_55, self.checkVar_61, self.checkVar_62,
                                     self.checkVar_63, self.checkVar_64, self.checkVar_65]

        self.subject_variables_list = [self.sub_name_11, self.sub_name_12, self.sub_name_13, self.sub_name_14,
                                       self.sub_name_15, self.sub_name_21, self.sub_name_22, self.sub_name_23,
                                       self.sub_name_24, self.sub_name_25, self.sub_name_31, self.sub_name_32,
                                       self.sub_name_33, self.sub_name_34, self.sub_name_35, self.sub_name_41,
                                       self.sub_name_42, self.sub_name_43, self.sub_name_44, self.sub_name_45,
                                       self.sub_name_51, self.sub_name_52, self.sub_name_53, self.sub_name_54,
                                       self.sub_name_55, self.sub_name_61, self.sub_name_62, self.sub_name_63,
                                       self.sub_name_64, self.sub_name_65]

    def create_labels(self):
        ttk.Label(self.win_root, text=" Timings:\n Date ", font=("Georgia", 18)).grid(column=0, row=2)
        ttk.Label(self.win_root, text="  ", font=("Georgia", 12)).grid(column=0, row=10)
        ttk.Label(self.win_root, text=" ", font=("Georgia", 18)).grid(column=3, row=11)

        routine_frame1 = tk.Frame(self.win_root, height=600, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame1.grid(column=5, row=12)

        self.display_attend_percent = tk.Entry(routine_frame1, width=8, textvariable=self.percent, justify=CENTER,
                                               font=("Georgia", 18))
        self.display_attend_percent.grid(column=5, row=12)

        routine_frame2 = tk.Frame(self.win_root, height=600, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame2.grid(column=11, row=12)

        self.classes_to_attend_display = tk.Entry(routine_frame2, width=8, textvariable=self.attend_class,
                                                  justify=CENTER, font=("Georgia", 18), state="normal")
        self.classes_to_attend_display.grid(column=11, row=12)

        # ttk.Label(routine_frame2, text="Attendance \n Percent: ", font=("Georgia", 18)).grid()

    def create_time(self):
        ttk.Label(self.win_root, text="               ", font="Georgia").grid(column=2, row=2, sticky=E)

        routine_frame3 = tk.Frame(self.win_root, height=10, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame3.grid(column=3, row=2, pady=20)

        time_entry_1 = ttk.Entry(routine_frame3, width=12, textvariable=self.timing_1, justify=CENTER,
                                 font=("Georgia", 15))
        time_entry_1.grid(column=3, row=2, sticky=E)
        self.timing_1.set("__:__ - __:__")

        # ---------------
        ttk.Label(self.win_root, text="               ", font="Georgia").grid(column=4, row=2, sticky=E)

        routine_frame4 = tk.Frame(self.win_root, height=10, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame4.grid(column=5, row=2)
        time_entry_2 = ttk.Entry(routine_frame4, width=12, textvariable=self.timing_2, justify=CENTER,
                                 font=("Georgia", 15))
        time_entry_2.grid(column=5, row=2, sticky=E)
        self.timing_2.set("__:__ - __:__")

        # --------------
        ttk.Label(self.win_root, text="               ", font="Georgia").grid(column=6, row=2, sticky=E)
        routine_frame5 = tk.Frame(self.win_root, height=10, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame5.grid(column=7, row=2)
        time_entry_3 = ttk.Entry(routine_frame5, width=12, textvariable=self.timing_3, justify=CENTER,
                                 font=("Georgia", 15))
        time_entry_3.grid(column=7, row=2, sticky=E)
        self.timing_3.set("__:__ - __:__")

        # --------------
        ttk.Label(self.win_root, text="               ", font="Georgia").grid(column=8, row=2, sticky=E)
        routine_frame6 = tk.Frame(self.win_root, height=10, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame6.grid(column=9, row=2)
        time_entry_4 = ttk.Entry(routine_frame6, width=12, textvariable=self.timing_4, justify=CENTER,
                                 font=("Georgia", 15))
        time_entry_4.grid(column=9, row=2, sticky=E)
        ttk.Label(self.win_root, text="               ", font="Georgia").grid(column=10, row=2, sticky=E)
        self.timing_4.set("__:__ - __:__")

        # --------------

        routine_frame7 = tk.Frame(self.win_root, height=10, bd=3, highlightcolor="red", relief=SUNKEN)
        routine_frame7.grid(column=11, row=2)
        time_entry_5 = ttk.Entry(routine_frame7, width=12, textvariable=self.timing_5, justify=CENTER,
                                 font=("Georgia", 15))
        time_entry_5.grid(column=11, row=2, sticky=E)
        self.timing_5.set("__:__ - __:__")

        ttk.Label(self.win_root, text="               ", font="Georgia").grid(column=12, row=2, sticky=E)

    def create_date(self):

        date_frame1 = tk.Frame(self.win_root, height=600, bd=2, highlightcolor="red", relief=SUNKEN)
        date_frame1.grid(column=0, row=3, padx=10)

        date_frame2 = tk.Frame(self.win_root, height=600, bd=2, highlightcolor="red", relief=SUNKEN)
        date_frame2.grid(column=0, row=4, padx=10)

        date_frame3 = tk.Frame(self.win_root, height=600, bd=2, highlightcolor="red", relief=SUNKEN)
        date_frame3.grid(column=0, row=5, padx=10)

        date_frame4 = tk.Frame(self.win_root, height=600, bd=2, highlightcolor="red", relief=SUNKEN)
        date_frame4.grid(column=0, row=6, padx=10)

        date_frame5 = tk.Frame(self.win_root, height=600, bd=2, highlightcolor="red", relief=SUNKEN)
        date_frame5.grid(column=0, row=7, padx=10)

        date_frame6 = tk.Frame(self.win_root, height=600, bd=2, highlightcolor="red", relief=SUNKEN)
        date_frame6.grid(column=0, row=8, padx=10)

        year_frame = tk.Frame(self.win_root, height=600, bd=1, relief=FLAT)
        year_frame.grid(column=7, row=1, pady=20)
        ttk.Label(year_frame, text=" Year:", font=("Georgia", 20)).grid(column=0, row=1, padx=5)

        self.year_selected = ttk.Combobox(year_frame, width=4, textvariable=self.year, font="Georgia")
        self.year_selected['values'] = (2020, 2021, 2022, 2023, 2024, 2025)
        self.year_selected.grid(column=7, row=1)
        self.year_selected.current(0)

        # ---------

        self.day1_selected = ttk.Combobox(date_frame1, width=2, textvariable=self.day_1, font="Georgia")
        self.day1_selected['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31)

        self.day1_selected.grid(column=0, row=3, sticky=W)
        self.day1_selected.current(0)

        self.month1_selected = ttk.Combobox(date_frame1, width=8, textvariable=self.month_1, font="Georgia")
        self.month1_selected['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December")

        self.month1_selected.grid(column=1, row=3, sticky=W)
        self.month1_selected.current(0)

        # ---------
        self.day2_selected = ttk.Combobox(date_frame2, width=2, textvariable=self.day_2, font="Georgia")
        self.day2_selected['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31)

        self.day2_selected.grid(column=0, row=4, sticky=W)
        self.day2_selected.current(0)

        self.month2_selected = ttk.Combobox(date_frame2, width=8, textvariable=self.month_2, font="Georgia")
        self.month2_selected['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December")

        self.month2_selected.grid(column=1, row=4, sticky=W)
        self.month2_selected.current(0)

        # ---------
        self.day3_selected = ttk.Combobox(date_frame3, width=2, textvariable=self.day_3, font="Georgia")
        self.day3_selected['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31)

        self.day3_selected.grid(column=0, row=5, sticky=W)
        self.day3_selected.current(0)

        self.month3_selected = ttk.Combobox(date_frame3, width=8, textvariable=self.month_3, font="Georgia")
        self.month3_selected['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December")

        self.month3_selected.grid(column=1, row=5, sticky=W)
        self.month3_selected.current(0)

        # ---------
        self.day4_selected = ttk.Combobox(date_frame4, width=2, textvariable=self.day_4, font="Georgia")
        self.day4_selected['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31)

        self.day4_selected.grid(column=0, row=6, sticky=W)
        self.day4_selected.current(0)

        self.month4_selected = ttk.Combobox(date_frame4, width=8, textvariable=self.month_4, font="Georgia")
        self.month4_selected['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December")

        self.month4_selected.grid(column=1, row=6, sticky=W)
        self.month4_selected.current(0)

        # ---------
        self.day5_selected = ttk.Combobox(date_frame5, width=2, textvariable=self.day_5, font="Georgia")
        self.day5_selected['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31)

        self.day5_selected.grid(column=0, row=7, sticky=W)
        self.day5_selected.current(0)

        self.month5_selected = ttk.Combobox(date_frame5, width=8, textvariable=self.month_5, font="Georgia")
        self.month5_selected['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December")

        self.month5_selected.grid(column=1, row=7, sticky=W)
        self.month5_selected.current(0)

        # ---------
        self.day6_selected = ttk.Combobox(date_frame6, width=2, textvariable=self.day_6, font="Georgia")
        self.day6_selected['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25, 26, 27, 28, 29, 30, 31)

        self.day6_selected.grid(column=0, row=8, sticky=W)
        self.day6_selected.current(0)

        self.month6_selected = ttk.Combobox(date_frame6, width=8, textvariable=self.month_6, font="Georgia")
        self.month6_selected['values'] = ("January", "February", "March", "April", "May", "June", "July",
                                          "August", "September", "October", "November", "December")

        self.month6_selected.grid(column=1, row=8, sticky=W)
        self.month6_selected.current(0)

    def check_date(self):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        day_list = [self.day_1.get(), self.day_2.get(), self.day_3.get(), self.day_4.get(), self.day_5.get(),
                    self.day_6.get()]
        month_list = [self.month_1.get(), self.month_2.get(), self.month_3.get(), self.month_4.get(),
                      self.month_5.get(), self.month_6.get()]

        print(day_list)
        print(month_list)

        current_year = self.year.get()
        print(current_year)
        if current_year % 4 == 0:
            for i in range(6):
                if day_list[i] == 31:
                    if month_list[i] == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                        print(day_list[i])
                        print(month_list[i])
                        print("accepted")


                else:
                    print(day_list[i])
                    print(month_list[i])
                    print("not accepted")

            # days[1] += 1
            # print(days)

    def create_routine(self):
        self.sub_entry_11 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_11, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_11.grid(column=3, row=3, pady=30, sticky=E)

        self.sub_entry_12 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_12, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_12.grid(column=5, row=3, sticky=E)

        self.sub_entry_13 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_13, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_13.grid(column=7, row=3, sticky=E)

        self.sub_entry_14 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_14, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_14.grid(column=9, row=3, sticky=E)

        self.sub_entry_15 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_15, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_15.grid(column=11, row=3, sticky=E)

        # ----------

        self.sub_entry_21 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_21, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_21.grid(column=3, row=4, pady=25)

        self.sub_entry_22 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_22, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_22.grid(column=5, row=4)

        self.sub_entry_23 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_23, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_23.grid(column=7, row=4)

        self.sub_entry_24 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_24, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_24.grid(column=9, row=4)

        self.sub_entry_25 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_25, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_25.grid(column=11, row=4)

        # ------------

        self.sub_entry_31 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_31, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_31.grid(column=3, row=5, pady=25)

        self.sub_entry_32 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_32, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_32.grid(column=5, row=5)

        self.sub_entry_33 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_33, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_33.grid(column=7, row=5)

        self.sub_entry_34 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_34, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_34.grid(column=9, row=5)

        self.sub_entry_35 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_35, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_35.grid(column=11, row=5)

        # ------------

        self.sub_entry_41 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_41, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_41.grid(column=3, row=6, pady=25)

        self.sub_entry_42 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_42, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_42.grid(column=5, row=6)

        self.sub_entry_43 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_43, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_43.grid(column=7, row=6)

        self.sub_entry_44 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_44, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_44.grid(column=9, row=6)

        self.sub_entry_45 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_45, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_45.grid(column=11, row=6)

        # ------------

        self.sub_entry_51 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_51, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_51.grid(column=3, row=7, pady=25)

        self.sub_entry_52 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_52, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_52.grid(column=5, row=7)

        self.sub_entry_53 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_53, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_53.grid(column=7, row=7)

        self.sub_entry_54 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_54, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_54.grid(column=9, row=7)

        self.sub_entry_55 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_55, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_55.grid(column=11, row=7)

        # ------------

        self.sub_entry_61 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_61, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_61.grid(column=3, row=8, pady=25)

        self.sub_entry_62 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_62, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_62.grid(column=5, row=8)

        self.sub_entry_63 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_63, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_63.grid(column=7, row=8)

        self.sub_entry_64 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_64, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_64.grid(column=9, row=8)

        self.sub_entry_65 = tk.Entry(self.win_root, width=12, textvariable=self.sub_name_65, justify=CENTER,
                                     font=("Georgia", 15), state="normal", relief="groove", bd=1, bg="beige")
        self.sub_entry_65.grid(column=11, row=8)

        # radio buttons

        self.chk_11 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_11, state="disabled")
        self.chk_11.deselect()
        self.chk_11.grid(column=4, row=3, sticky=W)

        self.chk_12 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_12, state="disabled")
        self.chk_12.deselect()
        self.chk_12.grid(column=6, row=3, sticky=W)

        self.chk_13 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_13, state="disabled")
        self.chk_13.deselect()
        self.chk_13.grid(column=8, row=3, sticky=W)

        self.chk_14 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_14, state="disabled")
        self.chk_14.deselect()
        self.chk_14.grid(column=10, row=3, sticky=W)

        self.chk_15 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_15, state="disabled")
        self.chk_15.deselect()
        self.chk_15.grid(column=12, row=3, sticky=W)

        # ----------------

        self.chk_21 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_21, state="disabled")
        self.chk_21.deselect()
        self.chk_21.grid(column=4, row=4, sticky=W)

        self.chk_22 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_22, state="disabled")
        self.chk_22.deselect()
        self.chk_22.grid(column=6, row=4, sticky=W)

        self.chk_23 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_23, state="disabled")
        self.chk_23.deselect()
        self.chk_23.grid(column=8, row=4, sticky=W)

        self.chk_24 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_24, state="disabled")
        self.chk_24.deselect()
        self.chk_24.grid(column=10, row=4, sticky=W)

        self.chk_25 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_25, state="disabled")
        self.chk_25.deselect()
        self.chk_25.grid(column=12, row=4, sticky=W)

        # ----------------

        self.chk_31 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_31, state="disabled")
        self.chk_31.deselect()
        self.chk_31.grid(column=4, row=5, sticky=W)

        self.chk_32 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_32, state="disabled")
        self.chk_32.deselect()
        self.chk_32.grid(column=6, row=5, sticky=W)

        self.chk_33 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_33, state="disabled")
        self.chk_33.deselect()
        self.chk_33.grid(column=8, row=5, sticky=W)

        self.chk_34 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_34, state="disabled")
        self.chk_34.deselect()
        self.chk_34.grid(column=10, row=5, sticky=W)

        self.chk_35 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_35, state="disabled")
        self.chk_35.deselect()
        self.chk_35.grid(column=12, row=5, sticky=W)

        # ----------------

        self.chk_41 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_41, state="disabled")
        self.chk_41.deselect()
        self.chk_41.grid(column=4, row=6, sticky=W)

        self.chk_42 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_42, state="disabled")
        self.chk_42.deselect()
        self.chk_42.grid(column=6, row=6, sticky=W)

        self.chk_43 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_43, state="disabled")
        self.chk_43.deselect()
        self.chk_43.grid(column=8, row=6, sticky=W)

        self.chk_44 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_44, state="disabled")
        self.chk_44.deselect()
        self.chk_44.grid(column=10, row=6, sticky=W)

        self.chk_45 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_45, state="disabled")
        self.chk_45.deselect()
        self.chk_45.grid(column=12, row=6, sticky=W)

        # ----------------

        self.chk_51 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_51, state="disabled")
        self.chk_51.deselect()
        self.chk_51.grid(column=4, row=7, sticky=W)

        self.chk_52 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_52, state="disabled")
        self.chk_52.deselect()
        self.chk_52.grid(column=6, row=7, sticky=W)

        self.chk_53 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_53, state="disabled")
        self.chk_53.deselect()
        self.chk_53.grid(column=8, row=7, sticky=W)

        self.chk_54 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_54, state="disabled")
        self.chk_54.deselect()
        self.chk_54.grid(column=10, row=7, sticky=W)

        self.chk_55 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_55, state="disabled")
        self.chk_55.deselect()
        self.chk_55.grid(column=12, row=7, sticky=W)

        # ----------------

        self.chk_61 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_61, state="disabled")
        self.chk_61.deselect()
        self.chk_61.grid(column=4, row=8, sticky=W)

        self.chk_62 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_62, state="disabled")
        self.chk_62.deselect()
        self.chk_62.grid(column=6, row=8, sticky=W)

        self.chk_63 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_63, state="disabled")
        self.chk_63.deselect()
        self.chk_63.grid(column=8, row=8, sticky=W)

        self.chk_64 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_64, state="disabled")
        self.chk_64.deselect()
        self.chk_64.grid(column=10, row=8, sticky=W)

        self.chk_65 = tk.Checkbutton(self.win_root, text="", variable=self.checkVar_65, state="disabled")
        self.chk_65.deselect()
        self.chk_65.grid(column=12, row=8, sticky=W)

    def create_functions_button(self):

        # new_frame = tk.Frame(self.win_root, height=500, bd=2, relief=SUNKEN)
        # new_frame.grid(column=8, row=2)
        attendance_percent = tk.Button(self.win_root, text="Attendance Percent", font="Georgia",
                                       command=self.attendance_percent_button_clicked)
        attendance_percent.grid(column=3, row=12)

        class_to_attend = tk.Button(self.win_root, text="Classes to attend", font="Georgia",
                                    command=self.classes_to_attend)
        class_to_attend.grid(column=9, row=12)

        select_button = tk.Button(self.win_root, text="Select", font="Georgia", command=self.select_classes)
        select_button.grid(column=12, row=3, padx=90)

        check_time_button = tk.Button(self.win_root, text="Check", font="Georgia", command=self.check_date)
        check_time_button.grid(column=12, row=5, padx=90)

        check_time_button = tk.Button(self.win_root, text="Refresh", font="Georgia", command=self.refresh_clicked)
        check_time_button.grid(column=12, row=6, padx=90)

        ok_button = tk.Button(self.win_root, text="ok", font="Georgia", command=self.ok_clicked)
        ok_button.grid(column=12, row=12)

        save_button = tk.Button(self.win_root, text="save", font="Georgia", command=self.save_button_clicked)
        save_button.grid(column=12, row=13, pady=20)

    def check_time(self):
        pattern = re.compile(r'[0-1][0-9]:[0-5][0-9]\s-\s[0-1][0-9]:[0-5][0-9]')

        timing_variables_list = [self.timing_1, self.timing_2, self.timing_3, self.timing_4, self.timing_5]

        for entry in timing_variables_list:
            if len(entry.get()) == 13:
                if pattern.match(entry.get()) is not None:
                    self.count_for_correct_timing += 1

                elif entry.get() == "__:__ - __:__":
                    self.count_for_default_time_value += 0

            else:
                entry.set("")
                self.count_for_unacceptable_value += 1

        if self.count_for_correct_timing < 5 and self.count_for_unacceptable_value == 0:
            msg.showinfo("Attendance Manager", "Enter the timings in the specified format!")

        if self.count_for_unacceptable_value > 0:
            msg.showinfo("Attendance Manager", "Alphabets or AlphaNumeric combinations, or random numbers or symbols"
                                               " in any random sequence are not allowed!")

    def enable_check_box(self):
        for entry in self.check_button_list:
            entry.configure(state="normal")
        msg.showinfo("Attendance Manager", " You can select the attended classes! \n Press select button to save your "
                                           "selections")
        self.check_disabled_state = False

    # disable the check buttons associated with the empty or ----- entry box
    def disable_not_required_check_boxes(self):
        for pos in self.disable_checkButton_list:
            self.check_button_list[pos].configure(state="disabled")

    def attendance_percent_button_clicked(self):
        if not self.select_class_executed:
            self.attendance_percent_clicked = True

            for subject in self.subject_variables_list:

                if len(subject.get()) != 0:
                    if subject.get().isalnum():
                        self.total_subjects += 1
                        pos_of_valid_entry = self.subject_variables_list.index(subject)
                        self.valid_entry_chkBox_list.append(pos_of_valid_entry)

                    else:
                        subject.set("---------")
                        pos = self.subject_variables_list.index(
                            subject)  # to get the positions of the dashed entry boxes
                        self.disable_checkButton_list.append(pos)  # adding the positions to a separate list

                else:
                    pos = self.subject_variables_list.index(
                        subject)  # if entry box is empty, the index is added to the list
                    self.disable_checkButton_list.append(pos)
            print(self.total_subjects)  # total subjects in the routine

            if self.total_subjects == 0:
                self.total_subjects_is_zero = True

                if not self.routine_disabled_state:
                    self.attendance_percent_clicked = False
                    msg.showinfo("Attendance Manager", "Empty routine, add subjects to calculate percentage!")
                    self.disable_checkButton_list.clear()

            else:
                self.total_subjects_is_zero = False
                if not self.routine_disabled_state:
                    for item in self.entry_list:
                        item.configure(state="disabled")
                    self.routine_disabled_state = True
                    self.enable_check_box()
                    self.disable_not_required_check_boxes()

                else:
                    self.enable_check_box()
                    self.disable_not_required_check_boxes()

        else:
            msg.showinfo("Attendance Manager", "Click the refresh button to perform consecutive calculations!")

    # count the number of classes attended -- handled by select button
    # also calculates percentage attendance
    def select_classes(self):

        if not self.total_subjects_is_zero:
            if self.select_class_executed_count == 0:

                for chk in self.check_variables_list:
                    if chk.get() == 1:
                        self.checkButton_enabled_count += 1

                if self.checkButton_enabled_count == 0:
                    msg.showinfo("Attendance Manager", "Select the classes by checking the accompanied check box!")

                else:
                    self.select_class_executed = True
                    for pos in self.valid_entry_chkBox_list:
                        self.check_button_list[pos].configure(state="disabled")

                    print("selected", self.checkButton_enabled_count)

                    try:
                        self.percent_attendance = (self.checkButton_enabled_count / self.total_subjects) * 100
                        print(self.percent_attendance)
                        self.percent.set(self.percent_attendance)

                        self.attendance_percent_calculated = True
                    except ZeroDivisionError:
                        msg.showinfo("Attendance Manager", "You have not selected any classes! \nEdit the routine, "
                                                           "and then select the classes attended to calculate your "
                                                           "attendance percent!")
                    self.select_class_executed_count += 1

            else:
                msg.showinfo("Attendance Manager", "Click the refresh button to perform consecutive calculations!")

        else:
            msg.showinfo("Attendance Manager", "Edit the routine to add and select the classes attended!")

    def classes_to_attend(self):

        if not self.ok_button_clicked:
            self.classes_to_attend_clicked = True

            for subject in self.subject_variables_list:
                if len(subject.get()) != 0:
                    if subject.get().isalnum():
                        self.count_routine_to_calculate_classes_to_attend += 1
                        pos_of_valid_entry = self.subject_variables_list.index(subject)
                        self.list_for_classes_to_attend.append(pos_of_valid_entry)
                    else:
                        subject.set("---------")
                        pos_of_entry_to_be_disabled = self.subject_variables_list.index(subject)
                        self.disable_entry_list.append(pos_of_entry_to_be_disabled)
                else:
                    pos_of_entry_to_be_disabled = self.subject_variables_list.index(subject)
                    self.disable_entry_list.append(pos_of_entry_to_be_disabled)

            if self.count_routine_to_calculate_classes_to_attend != 0:
                for value in self.disable_entry_list:
                    self.entry_list[value].configure(state="disabled")

            if self.count_routine_to_calculate_classes_to_attend == 0:
                msg.showinfo("Attendance Manager", "Empty routine, add subjects to calculate the required classes to "
                                                   "attend!")
                self.disable_entry_list.clear()
                self.classes_to_attend_clicked = False

            else:
                msg.showinfo("Attendance Manager", "Enter the required attendance percentage and press ok!")
                self.classes_to_attend_clicked = True

        else:
            msg.showinfo("Attendance Manager", "Click the refresh button to perform consecutive calculations!")

    def ok_clicked(self):

        if not self.ok_button_clicked:
            if not self.classes_to_attend_clicked:
                msg.showinfo("Attendance Manager", "Click on class to attend button, and enter the required attendance "
                                                   "percent!")

            else:
                value = self.attend_class.get()

                if value <= 0.0 or value >= 100:
                    msg.showinfo("Illegal input", "Enter a reasonable attendance percentage!")

                else:

                    self.count_classes_to_attend = math.ceil(
                        (value / 100) * self.count_routine_to_calculate_classes_to_attend)

                    self.ok_button_clicked = True

                    while self.highlighted_subject_count < self.count_classes_to_attend:
                        item = random.choice(self.list_for_classes_to_attend)

                        if self.highlight_entry_list.__contains__(item):
                            self.list_for_classes_to_attend.remove(item)

                        else:
                            self.highlight_entry_list.append(item)
                            self.highlighted_subject_count += 1

                    for index in self.highlight_entry_list:
                        self.entry_list[index].configure(bg="light blue")
                    self.attend_class.set(self.count_classes_to_attend)
                    self.classes_to_attend_display.configure(state="disabled")
                    self.classes_to_attend_clicked = False

        else:
            msg.showinfo("Consecutive calculations", "Click the refresh button to perform consecutive calculations!")

    def save_button_clicked(self):
        list23 = []

        months_31 = ["January", "March", "May", "July", "August", "October", "December"]
        day_list = [self.day_1, self.day_2, self.day_3, self.day_4, self.day_5, self.day_6]
        month_list = [self.month_1, self.month_2, self.month_3, self.month_4, self.month_5, self.month_6]

    def refresh_clicked(self):

        if not self.attendance_percent_clicked or not self.classes_to_attend_clicked:

            self.attendance_percent_clicked = False
            self.attendance_percent_calculated = False
            self.select_class_executed = False
            self.total_subjects_is_zero = True
            self.routine_disabled_state = False
            self.ok_button_clicked = False
            self.total_subjects = 0
            self.select_class_executed_count = 0
            self.checkButton_enabled_count = 0
            self.disable_checkButton_list.clear()

        if not self.attendance_percent_clicked:
            for item in self.entry_list:
                item.configure(state="normal")

            for chk in self.check_variables_list:
                chk.set(0)
                self.check_disabled_state = True

            self.percent.set(0)

        print("current value", self.classes_to_attend, "\n")

        if not self.classes_to_attend_clicked:
            for entry in self.entry_list:
                entry.configure(bg="beige")

            self.disable_entry_list.clear()
            self.highlight_entry_list.clear()
            self.list_for_classes_to_attend.clear()
            self.count_classes_to_attend = 0
            self.highlighted_subject_count = 0
            self.count_routine_to_calculate_classes_to_attend = 0
            self.attend_class.set(0)
            self.classes_to_attend_display.configure(state="normal")

        self.refresh_button_clicked = True


if __name__ == '__main__':
    obj_weekly = Weekly()
    obj_weekly.win_root.mainloop()

