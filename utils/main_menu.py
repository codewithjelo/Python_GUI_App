import customtkinter
from customtkinter import *
import os
from PIL import Image

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('PCFIND - Main Screen')
        # -------------------------------------- STYLING and IMAGES ---------------------------------------- #
        self.logo_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/PC_FIND.png"),
            size=(280, 95))
        self.top_banner_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/top_banner"),
            size=(665, 105))

        # ITEM IMAGE ----------------------------------------------------------------------- #
        self.default_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/defualt_image.jpg"),
            size=(350, 434))

        self.gpu_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/gpu.png"),
            size=(350, 334))

        self.cpu_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/cpu.png"),
            size=(350, 334))

        self.ram_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/ram.png"),
            size=(350, 334))

        self.mobo_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/mobo.png"),
            size=(350, 334))

        self.power_supply_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/psu.png"),
            size=(350, 334))

        self.hdd_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/hdd.png"),
            size=(350, 334))

        self.ssd_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/ssd.png"),
            size=(350, 334))

        self.cooler_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/cooler.png"),
            size=(350, 334))

        self.fan_image = customtkinter.CTkImage(
            Image.open("C:/Users/janna/IdeaProjects/Python_GUI_App/img/items/fan.png"),
            size=(350, 334))

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
                                                  font=('Montserrat', 12))
        self.gpu_button.grid(row=0, column=1, padx=(45, 10))

        self.cpu_button = customtkinter.CTkButton(self.cpu_frame, text='SELECT', font=('Montserrat', 12))
        self.cpu_button.grid(row=0, column=1, padx=(45, 10))

        self.ram_button = customtkinter.CTkButton(self.ram_frame, text='SELECT', font=('Montserrat', 12))
        self.ram_button.grid(row=0, column=1, padx=(32, 10))

        self.mobo_button = customtkinter.CTkButton(self.mobo_frame, hover_color='#1A5B3F', text='SELECT',
                                                   font=('Montserrat', 12))
        self.mobo_button.grid(row=0, column=1, padx=(25, 10))

        self.power_supply_button = customtkinter.CTkButton(self.power_supply_frame, hover_color='#1A5B3F',
                                                           text='SELECT', font=('Montserrat', 12))
        self.power_supply_button.grid(row=0, column=1, padx=(46, 10))

        self.hdd_button = customtkinter.CTkButton(self.hdd_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12))
        self.hdd_button.grid(row=0, column=1, padx=(40, 10))

        self.ssd_button = customtkinter.CTkButton(self.ssd_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12))
        self.ssd_button.grid(row=0, column=1, padx=10)

        self.cooler_button = customtkinter.CTkButton(self.cooler_frame, hover_color='#1A5B3F', text='SELECT',
                                                     font=('Montserrat', 12))
        self.cooler_button.grid(row=0, column=1, padx=(38, 10))

        self.fan_button = customtkinter.CTkButton(self.fan_frame, hover_color='#1A5B3F', text='SELECT',
                                                  font=('Montserrat', 12))
        self.fan_button.grid(row=0, column=1, padx=(38, 10))

        # END REGION
        self.order_title_label = customtkinter.CTkLabel(self.order_frame, text='ORDER', font=('Montserrat', 14, 'bold'),
                                                        fg_color='#2FA572', corner_radius=5)
        self.order_title_label.grid(row=0, column=0, sticky='EW')
        self.order_title_label.configure(anchor='center')

        self.order_id_label = customtkinter.CTkLabel(self.order_frame, text='ORDER ID: ', font=('Courier New', 12))
        self.order_id_label.grid(row=1, column=0, sticky='EW', pady=1)
        self.order_id_label.configure(anchor='center')

        self.order_transaction_label = customtkinter.CTkLabel(self.order_frame, text='', fg_color='white')
        self.order_transaction_label.grid(row=2, column=0, sticky='NSEW')

        self.order_total_label = customtkinter.CTkLabel(self.order_frame, text='TOTAL: PHP 0', fg_color='#1D1E23',
                                                        font=('Courier New', 12))
        self.order_total_label.grid(row=3, column=0, sticky='EW')

        self.order_button = customtkinter.CTkButton(self.order_frame, text='CONFIRM ORDER', corner_radius=5,
                                                    font=('Montserrat', 12, 'bold'))
        self.order_button.grid(row=4, column=0, sticky='EW')

        # REGION DISPLAY SECTION
        self.display_label = customtkinter.CTkLabel(self.display_frame, text='', image=self.default_image)
        self.display_label.grid(row=0, column=0, sticky='NSEW', columnspan=2)

        self.add_order_button = customtkinter.CTkButton(self.display_frame, text='+', font=('Montserrat', 14, 'bold'))
        self.add_order_button.grid(row=1, column=0, padx=2, pady=4, sticky='NSEW')
        self.add_order_button.configure(anchor='center')

        self.remove_order_button = customtkinter.CTkButton(self.display_frame, text='-',
                                                           font=('Montserrat', 14, 'bold'))
        self.remove_order_button.grid(row=1, column=1, padx=2, pady=4, sticky='NSEW')
        self.remove_order_button.configure(anchor='center')

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
