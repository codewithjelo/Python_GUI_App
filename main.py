import customtkinter
from PIL import Image
import random

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")
prices = {'Galax RTX3050 GPU': 18500,
          'Ryzen 5 5600G CPU': 9000,
          'KFB 16gb 2x8 RAM': 4600,
          'AsrockB450M MOBO': 5600,
          'GBYTE P650B PSU': 3500,
          'Seagate 1TB HDD': 2200,
          'Kingston 500GB SSD': 1600,
          'Deepcool IE COOLER': 400,
          'Rakk Ounos RGB FAN': 160,
          }


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('PCFIND - Main Screen')

        # ----------------------------------------- FUNCTIONS ---------------------------------------------- #
        # REGION ADD TO ORDER BUTTON
        def order_id():
            numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U',
                       'V', 'W', 'X', 'Y', 'Z']
            random_order_id = "KOY_"
            random_letters = ""
            random_digits = ""
            for i in range(0, 3):
                random_letters += random.choice(letters)
                random_digits += str(random.choice(numbers))

            random_order_id += random_letters + random_digits
            return random_order_id

        def confirmation():
            order_confirmation = customtkinter.CTkInputDialog(
                text="Type YES to add item\n(YOU CAN'T REMOVE YOUR ORDER)", title="Order Confirmation")
            if order_confirmation.get_input() == 'YES':
                add()

        def add():
            if self.display_label.cget('text') == 'Galax RTX3050 GPU':
                current_order = self.order_transaction_label.cget('text')
                added_item = self.display_label.cget('text') + '\t  PHP ' + str(
                    prices[self.display_label.cget('text')]) + '. \n'

            elif self.display_label.cget('text') == 'AsrockB450M MOBO' or self.display_label.cget(
                    'text') == 'Kingston 500GB SSD':
                current_order = self.order_transaction_label.cget('text')
                added_item = self.display_label.cget('text') + '\tPHP ' + str(
                    prices[self.display_label.cget('text')]) + '. \n'

            elif self.display_label.cget('text') == 'Deepcool IE COOLER':
                current_order = self.order_transaction_label.cget('text')
                added_item = self.display_label.cget('text') + '              PHP ' + str(
                    prices[self.display_label.cget('text')]) + '. \n'

            elif self.display_label.cget('text') == 'Rakk Ounos RGB FAN':
                current_order = self.order_transaction_label.cget('text')
                added_item = self.display_label.cget('text') + '             PHP ' + str(
                    prices[self.display_label.cget('text')]) + '. \n'

            else:
                current_order = self.order_transaction_label.cget('text')
                added_item = self.display_label.cget('text') + '\t\tPHP ' + str(
                    prices[self.display_label.cget('text')]) + '. \n'

            updated_order = current_order + added_item
            self.order_transaction_label.configure(text=updated_order)

            order_total = self.order_total_label.cget('text').replace('TOTAL: ', '')
            order_total = order_total.replace('PHP', '')
            updated_total = int(order_total) + prices[self.display_label.cget('text')]
            self.order_total_label.configure(text='TOTAL: ' + 'PHP ' + str(updated_total))

        # REGION DISPLAY FUNCTION
        def display_gpu():
            self.display_label.configure(
                image=self.gpu_image,
                text='Galax RTX3050 GPU',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_cpu():
            self.display_label.configure(
                image=self.cpu_image,
                text='Ryzen 5 5600G CPU',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_ram():
            self.display_label.configure(
                image=self.ram_image,
                text='KFB 16gb 2x8 RAM',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_mobo():
            self.display_label.configure(
                image=self.mobo_image,
                text='AsrockB450M MOBO',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_psu():
            self.display_label.configure(
                image=self.power_supply_image,
                text='GBYTE P650B PSU',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_hdd():
            self.display_label.configure(
                image=self.hdd_image,
                text='Seagate 1TB HDD',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_ssd():
            self.display_label.configure(
                image=self.ssd_image,
                text='Kingston 500GB SSD',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_cooler():
            self.display_label.configure(
                image=self.cooler_image,
                text='Deepcool IE COOLER',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def display_fan():
            self.display_label.configure(
                image=self.fan_image,
                text='Rakk Ounos RGB FAN',
                font=('Montserrat', 14, 'bold'),
                width=21,
                compound='bottom'
            )

        def order():
            self.order_total_label.configure(text="TOTAL : PHP 0")
            self.order_id_label.configure(text="ORDER ID: " + order_id())
            self.order_transaction_label.configure(text='')

        # END REGION

        # -------------------------------------- STYLING and IMAGES ---------------------------------------- #
        self.logo_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/PC_FIND.png"),
            size=(280, 95))
        self.top_banner_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/top_banner"),
            size=(825, 115))

        # ITEM IMAGE ----------------------------------------------------------------------- #
        self.default_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/defualt_image.jpg"),
            size=(350, 434))

        self.gpu_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/gpu.png"),
            size=(350, 416))

        self.cpu_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/cpu.png"),
            size=(350, 416))

        self.ram_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/ram.png"),
            size=(350, 416))

        self.mobo_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/mobo.png"),
            size=(350, 416))

        self.power_supply_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/psu.png"),
            size=(350, 416))

        self.hdd_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/hdd.png"),
            size=(350, 416))

        self.ssd_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/ssd.png"),
            size=(350, 416))

        self.cooler_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/cooler.png"),
            size=(350, 416))

        self.fan_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/fan.png"),
            size=(350, 416))

        # -------------------------------------------- WIDGETS --------------------------------------------- #
        # REGION FRAMES
        # SECTION FRAMES
        self.main_frame = customtkinter.CTkFrame(self, width=800, height=580, bg_color='#1D1E23', fg_color='#1D1E23',
                                                 corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="NSEW")

        self.top_banner_frame = customtkinter.CTkFrame(self.main_frame, bg_color='#1D1E23', fg_color='#1D1E23',
                                                       corner_radius=0)
        self.top_banner_frame.grid(row=0, column=0, sticky='NSEW', columnspan=3)

        self.menu_frame = customtkinter.CTkFrame(self.main_frame, bg_color='#1D1E23', fg_color='#1D1E23',
                                                 corner_radius=0)
        self.menu_frame.grid(row=1, column=0, padx=3, pady=3, sticky='NSEW')

        self.display_frame = customtkinter.CTkFrame(self.main_frame, fg_color='#1D1E23', corner_radius=0)
        self.display_frame.grid(row=1, column=1, padx=3, pady=3, sticky='NSEW')

        self.order_frame = customtkinter.CTkFrame(self.main_frame, fg_color='#1D1E23', corner_radius=0)
        self.order_frame.grid(row=1, column=2, padx=3, pady=3, sticky='NSEW')

        # REGION TOP BANNER SECTION
        self.logo_label = customtkinter.CTkLabel(self.top_banner_frame, text='', image=self.logo_image,
                                                 bg_color='#1D1E23')
        self.logo_label.grid(row=0, column=0, stick='W')

        self.top_banner_label = customtkinter.CTkLabel(self.top_banner_frame, text='', image=self.top_banner_image,
                                                       bg_color='#1D1E23')
        self.top_banner_label.grid(row=0, column=1, stick='W')

        # PCPARTS FRAMES ------------------------------------------------------------------------------------- #
        self.gpu_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                fg_color='#1D1E23')
        self.gpu_frame.grid(row=1, column=0, sticky='NSEW')

        self.cpu_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                fg_color='#1D1E23')
        self.cpu_frame.grid(row=2, column=0, sticky='NSEW')

        self.ram_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                fg_color='#1D1E23')
        self.ram_frame.grid(row=3, column=0, sticky='NSEW')

        self.mobo_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                 fg_color='#1D1E23')
        self.mobo_frame.grid(row=4, column=0, sticky='NSEW')

        self.power_supply_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                         fg_color='#1D1E23')
        self.power_supply_frame.grid(row=5, column=0, sticky='NSEW')

        self.hdd_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                fg_color='#1D1E23')
        self.hdd_frame.grid(row=6, column=0, sticky='NSEW')

        self.ssd_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                fg_color='#1D1E23')
        self.ssd_frame.grid(row=7, column=0, sticky='NSEW')

        self.cooler_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                   fg_color='#1D1E23')
        self.cooler_frame.grid(row=8, column=0, sticky='NSEW')

        self.fan_frame = customtkinter.CTkFrame(self.menu_frame, bg_color='#1D1E23', corner_radius=0,
                                                fg_color='#1D1E23')
        self.fan_frame.grid(row=9, column=0, sticky='NSEW')

        # END REGION
        # ITEM LIST REGION ----------------------------------------------------------------------------------- #
        self.item_list_label = customtkinter.CTkLabel(self.menu_frame, text='ITEM LIST', fg_color='#2FA572',
                                                      corner_radius=5)
        self.item_list_label.grid(row=0, column=0, sticky='WE')
        self.item_list_label.configure(anchor='center', font=('Montserrat', 14, 'bold'))

        # PC PART REGION ------------------------------------------------------------------------------------- #
        self.gpu_label = customtkinter.CTkLabel(self.gpu_frame,
                                                text='  Galax RTX 3050 1-Click OC 8gb\n   128bit- NVIDIA G-Sync',
                                                width=21,
                                                font=('Courier New', 12))
        self.gpu_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.cpu_label = customtkinter.CTkLabel(self.cpu_frame,
                                                text='      AMD Ryzen 5 5600G 3.9GHz \n   w/ Raedon Vega 7', width=21,
                                                font=('Courier New', 12))
        self.cpu_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.ram_label = customtkinter.CTkLabel(self.ram_frame,
                                                text='   Kingston Fury Beast 16gb 2x8\n   3200MT/s Ddr4 RGB Memory Black',
                                                width=21,
                                                font=('Courier New', 12))
        self.ram_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.mobo_label = customtkinter.CTkLabel(self.mobo_frame,
                                                 text='  Asrock B450M Steel Legend Socket\nAm4 Ddr4 MOBO', width=21,
                                                 font=('Courier New', 12))
        self.mobo_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.power_supply_label = customtkinter.CTkLabel(self.power_supply_frame,
                                                         text='   GIGABYTE P650B 650W 80 Plus\n    Bronze 120mm Silent HYB Fan',
                                                         width=21,
                                                         font=('Courier New', 12))
        self.power_supply_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.hdd_label = customtkinter.CTkLabel(self.hdd_frame,
                                                text='     Seagate 1TB Hard-disk Drive',
                                                width=21,
                                                font=('Courier New', 12))
        self.hdd_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.ssd_label = customtkinter.CTkLabel(self.ssd_frame,
                                                text='Kingston NV1 PCIe M.2 3.0 NVME 500GB\nInternal Solid-state Drive',
                                                width=21,
                                                font=('Courier New', 12))
        self.ssd_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.cooler_label = customtkinter.CTkLabel(self.cooler_frame,
                                                   text='  Deepcool Ice Edge Mini FS v2.0\nCPU Air Cooler',
                                                   width=21,
                                                   font=('Courier New', 12))
        self.cooler_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        self.fan_label = customtkinter.CTkLabel(self.fan_frame,
                                                text='  Rakk Ounos X 120mm Eclipse RGB\n Led Fan Chassis Fan',
                                                width=21,
                                                font=('Courier New', 12))
        self.fan_label.grid(row=0, column=0, padx=10, pady=10, sticky='W')

        # BUTTONS
        self.gpu_button = customtkinter.CTkButton(self.gpu_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12), command=display_gpu)
        self.gpu_button.grid(row=0, column=1, padx=(45, 10))

        self.cpu_button = customtkinter.CTkButton(self.cpu_frame, text='SELECT', font=('Montserrat', 12),
                                                  command=display_cpu)
        self.cpu_button.grid(row=0, column=1, padx=(45, 10))

        self.ram_button = customtkinter.CTkButton(self.ram_frame, text='SELECT', font=('Montserrat', 12),
                                                  command=display_ram)
        self.ram_button.grid(row=0, column=1, padx=(32, 10))

        self.mobo_button = customtkinter.CTkButton(self.mobo_frame, hover_color='#1A5B3F', text='SELECT',
                                                   font=('Montserrat', 12), command=display_mobo)
        self.mobo_button.grid(row=0, column=1, padx=(25, 10))

        self.power_supply_button = customtkinter.CTkButton(self.power_supply_frame, hover_color='#1A5B3F',
                                                           text='SELECT', font=('Montserrat', 12), command=display_psu)
        self.power_supply_button.grid(row=0, column=1, padx=(46, 10))

        self.hdd_button = customtkinter.CTkButton(self.hdd_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12), command=display_hdd)
        self.hdd_button.grid(row=0, column=1, padx=(40, 10))

        self.ssd_button = customtkinter.CTkButton(self.ssd_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12), command=display_ssd)
        self.ssd_button.grid(row=0, column=1, padx=10)

        self.cooler_button = customtkinter.CTkButton(self.cooler_frame, hover_color='#1A5B3F', text='SELECT',
                                                     font=('Montserrat', 12), command=display_cooler)
        self.cooler_button.grid(row=0, column=1, padx=(38, 10))

        self.fan_button = customtkinter.CTkButton(self.fan_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12), command=display_fan)
        self.fan_button.grid(row=0, column=1, padx=(38, 10))

        # END REGION
        self.order_title_label = customtkinter.CTkLabel(self.order_frame, text='ORDER', font=('Montserrat', 14, 'bold'),
                                                        fg_color='#2FA572', corner_radius=5)
        self.order_title_label.grid(row=0, column=0, sticky='EW')
        self.order_title_label.configure(anchor='center')

        self.order_id_label = customtkinter.CTkLabel(self.order_frame, text='ORDER ID: ' + order_id(),
                                                     font=('Courier New', 12), fg_color='black', corner_radius=5)
        self.order_id_label.grid(row=1, column=0, sticky='EW', pady=1)
        self.order_id_label.configure(anchor='center')

        self.order_transaction_label = customtkinter.CTkLabel(self.order_frame, text='', fg_color='#1D1E23', width=300,
                                                              wraplength=300)
        self.order_transaction_label.grid(row=2, column=0, sticky='NW')

        self.order_total_label = customtkinter.CTkLabel(self.order_frame, text='TOTAL: PHP 0', fg_color='#1D1E23',
                                                        font=('Courier New', 12))
        self.order_total_label.grid(row=3, column=0, sticky='W')

        self.order_button = customtkinter.CTkButton(self.order_frame, text='CONFIRM ORDER', corner_radius=5,
                                                    font=('Montserrat', 12, 'bold'), command=order)
        self.order_button.grid(row=4, column=0, sticky='EW')

        # REGION DISPLAY SECTION
        self.display_label = customtkinter.CTkLabel(self.display_frame, text='', image=self.default_image)
        self.display_label.grid(row=0, column=0, sticky='NSEW', columnspan=2)

        self.add_order_button = customtkinter.CTkButton(self.display_frame, text='+', font=('Montserrat', 14, 'bold'),
                                                        command=confirmation, width=350)
        self.add_order_button.grid(row=1, column=0, padx=2, pady=4, sticky='NSEW')
        self.add_order_button.configure(anchor='center')

        # END REGION

        # ------------------------------------------ GRID CONFIGURATIONS ----------------------------------- #
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure(1, weight=1)
        self.menu_frame.rowconfigure(2, weight=1)
        self.menu_frame.rowconfigure(3, weight=1)
        self.menu_frame.rowconfigure(4, weight=1)
        self.menu_frame.rowconfigure(5, weight=1)
        self.menu_frame.rowconfigure(6, weight=1)
        self.menu_frame.rowconfigure(7, weight=1)
        self.menu_frame.rowconfigure(8, weight=1)
        self.menu_frame.rowconfigure(9, weight=1)
        self.order_frame.columnconfigure(0, weight=1)
        self.order_frame.rowconfigure(2, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
