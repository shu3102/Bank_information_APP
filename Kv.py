screen_helper = """

ScreenManager:
    MainScreen:
    MenuScreen:
    Button1Screen:
    Button2Screen:
    Button3Screen:
    Button4Screen:
    Button5Screen:
    Button6Screen:
    Button7Screen:
    Button8Screen:
    FileScreen:
    ExampleScreen:
    ATMScreen:
    
<MDLabel@Label>:
    size_hint:1,None

<ExampleScreen>:
    name:'example'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'title'
        ScrollView:
            size_hint: 1,1
            GridLayout:
                size_hint: 1,None
                height: self.minimum_height
                cols: 1
                MDLabel:
                    text: 'Example 1'
                GridLayout:
                    size_hint: 1,None
                    height: self.minimum_height
                    cols: 1
                    rows: 7
                                    
                    MDLabel:
                        text: 'How to use ATM' 
                        halign: "center"
                    MDLabel:
                        text: '  ATMs can be intimidating for first-timers.but once you get the hang of the theyre incredibly quick and convenient'
                        halign: "center"
                        
                    MDLabel:
                        text: 'Filler3'
                        halign: "center"
                    MDLabel:
                        text: 'Filler4'
                        halign: "center"
                    MDLabel: 
                        text: 'Filler5'
                        halign: "center"
                    MyLabel:
                        text: 'Filler6'
                        halign: "center"
                    MyLabel:
                        text: 'Filler7'
                        halign: "center"
            
        Button: 
            text: 'Home'
            size_hint: 1, .1
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Settings'
            size_hint: 1, .1
            on_press: root.manager.current = 'settings'


<MainScreen>
    name: 'main'
    MDGridLayout:
        cols: 1
        orientation: 'vertical'
        MDToolbar:
            title: 'All About Bank'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()],["magnify", lambda x:print("hay")]]
            
            elevation:10
        MDFloatLayout:
            orientation: 'vertical'
            Image: 
                source: 'bank1.jpg'
                size: self.texture_size
                allow_stretch: True
            MDRectangleFlatButton:
                text: 'start'
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                elevation_normal: 12
                on_press: root.manager.current = 'menu'



<MenuScreen>:
    name: 'menu'
    MDGridLayout:
        cols: 1
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: print("Callback")],["magnify", lambda x:print("hay")]]
            elevation:10
        ScrollView:
            MDGridLayout:
                cols: 1
                padding: 30
                spacing: 20
                size_hint: 1, 1.5

                MDRectangleFlatButton:
                    text: 'Bank Accounts'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'Button1'

                MDRectangleFlatButton:
                    text: 'ATM'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'atm'
                MDRectangleFlatButton:
                    text: 'Online Banking'
                    size_hint:(0.8,0.07)
                    on_press: root.manager.current = 'Button3'
                MDRectangleFlatButton:
                    text: 'Interest rate'
                    size_hint:(0.8,0.07)
                    on_press: root.manager.current = 'Button4'
                MDRectangleFlatButton:
                    text: 'Transactions'
                    size_hint:(0.8,0.07)
                    on_press: root.manager.current = 'Button5'
                MDRectangleFlatButton:
                    text: 'Schemes'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'Button6'
                MDRectangleFlatButton:
                    text: 'How to open Account'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'Button7'
                MDRectangleFlatButton:
                    text: 'How to close Account'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'Button8'
                MDRectangleFlatButton:
                    text: 'Button9'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'Button7'
                MDRectangleFlatButton:
                    text: 'Loan'
                    size_hint: (0.8,0.07)
                    on_press: root.manager.current = 'Button8'

<Button1Screen>:
    name: 'Button1'
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button1"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            padding : '20sp'
            MDLabel:
                text: root.showtext()
                text_size: self.width, None
                halign: 'left'
                valign: 'top'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.05}
                on_press: root.manager.current = 'menu'

<Button2Screen>:
    name: 'Button2'
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button2"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            
            MDLabel:
                text: root.showtext()
                text_size: self.width, None
                halign: 'left'
                valign: 'top'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.1}
                on_press: root.manager.current = 'menu'
<Button3Screen>:
    name: 'Button3'
   
    
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button3 screen"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Profile'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: root.manager.current = 'menu'
                
    
<Button4Screen>:
    name: 'Button4'
    MDLabel:
        text: "MDLabel"
        halign: "center"
    
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button3 screen"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Profile'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: root.manager.current = 'menu'
<Button5Screen>:
    name: 'Button5'
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button5 screen"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Profile'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: root.manager.current = 'menu'
<Button6Screen>:
    name: 'Button6'
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button6 screen"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Profile'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: root.manager.current = 'menu'
<Button7Screen>:
    name: 'Button7'
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button7 screen"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Profile'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: root.manager.current = 'example'
<Button8Screen>:
    name: 'Button8'
    MDGridLayout:
        cols: 1
        MDToolbar:
            title: "Button8 screen"
            elevation: 10
            left_action_items: [["menu", lambda x: x]]
        FloatLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'Profile'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Back'
                pos_hint: {'center_x':0.5,'center_y':0.3}
                on_press: root.manager.current = 'menu'



<ATMScreen>:
    name:'atm'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'title'
        ScrollView:
            size_hint: 1,1
            GridLayout:
                size_hint: 1,None
                height: self.minimum_height
                cols: 1
                MDLabel:
                    text: 'What Is an Automated Teller Machine (ATM)?'
                    halign: 'center'
                GridLayout:
                    size_hint: 1,None
                    height: self.minimum_height
                    cols: 1
                    rows: 7
                                    
                    MDLabel:
                        text: '->An automated teller machine (ATM) is an electronic banking outlet that allows customers to complete basic transactions without the aid of a branch representative or teller. Anyone with a credit card or debit card can access cash at most ATMs.' 
                        #halign: "center"
                    MDLabel:
                        text: '->ATMs can be intimidating for first-timers.but once you get the hang of the theyre incredibly quick and '
                        #halign: "center"
                        
                    MDLabel:
                        text: '->ATMs are , allowing consumers to perform quick self-service transactions such as deposits, cash withdrawals, bill payments, and transfers between accounts. Fees are commonly charged for cash withdrawals by the bank where the account is located, by the operator of the ATM, or by both. Some or all of these fees can be avoided by using an ATM operated directly by the bank that holds.'
                        #halign: "center"
                    MDLabel:
                        text: '  ->ATMs are known in different parts of the world as automated bank machines (ABM) or cash machines'
                        #halign: "center"
                    MDLabel: 
                        text: ' ATMs are known in different parts of the world as automated bank machines (ABM) or cash machines'
                        #halign: "center"
                    MDLabel:
                        text: 'Filler6'
                        #halign: "center"
                    MDLabel:
                        text: 'Filler7'
                        #halign: "center"
            
        Button: 
            text: 'Back'
            size_hint: 1, .1
            on_press: root.manager.current = 'menu'
        


"""

screen_Helper = """
Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top" : 1}
        elevation : 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        

    NavigationLayout:
        ScreenManager:

            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"
                
                                
                Image:
                    id: avatar
                    size_hint: None, None
                    size: "56dp", "56dp"
                    source: "bank1.jpg"
                                
                MDLabel:
                    text: "Shubham "
                    font_style: "Button"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "shubham123som@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]
                
                ScrollView:
                    DrawerList:
                        id: md_list
                        MDList:
                            OneLineIconListItem:
                                text: 'My Files'
                                IconLeftWidget:
                                    icon: "folder"
                                    
                            OneLineIconListItem:
                                text: 'Shared With Me'
                                IconLeftWidget:
                                    icon: "account-multiple"
                                    
                            OneLineIconListItem:
                                text: 'Starred'
                                IconLeftWidget:
                                    icon: "star"
                                    
                            OneLineIconListItem:
                                text: 'Resent'
                                IconLeftWidget:
                                    icon: "history"
                                    
                            OneLineIconListItem:
                                text: 'Shared  with'
                                IconLeftWidget:
                                    icon: "checkbox-marked"
                                
                            OneLineIconListItem:
                                text: 'Upload'
                                IconLeftWidget:
                                    icon: "upload"
                                #on_press: 
                                    #root.nav_drawer.set_state("close")
                                    #root.screen_manager.current = "upload"
                                
                            OneLineIconListItem:
                                text: 'Upload'
                                IconLeftWidget:
                                    icon: "upload"
                                #on_press: 
                                    #root.nav_drawer.set_state("close")
                                    #root.screen_manager.current = "upload"
                                
    
    MDLabel:
        haline:'centre'

"""




