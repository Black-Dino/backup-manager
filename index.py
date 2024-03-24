class BackUpManager:
    def __init__(self):
        self.app_list = [];
        self.get_app()
        self.menu = ["app list","search","setting","about"]
    
    def create_app(self):
        title = input('pls enter your app title: ')

        with open('app','a') as app:
            app.write(title + '\n')

    def create_card(self,data):
        pass
    
    def get_app(self):
        with open('app','r') as apps:
            for app in apps:
                self.app_list.append(app)

    def show_app(self):
        for app in self.app_list:
            print(app)

    def show_card(self):
        pass
    
    def show_menu(self):
        for index,item in enumerate(self.menu):
            print(index + 1,item)
            
        self.handle_select_menu_item()

    def handle_select_menu_item(self):
        option = int(input('select: '))

        if option == 1:
            self.show_app()

             
    def main(self):
        while 1:
            if len(self.app_list) == 0:
                self.create_app()
            else:
                self.show_menu()
    

print("welcome...")
app = BackUpManager()
app.main()
    