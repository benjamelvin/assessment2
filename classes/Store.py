
from classes.customer import Customer
from classes.inventory import Inventory

class Store():
    def __init__(self, name):
        self.name = name
        self.customers = Customer.all_customers()
        self.inventory = Inventory.all_inventory()
        
    def list_current_inventory(self):
        for index in self.inventory:
            movie_title = index['title']
            available_copies = index['copies_available']
            print(f'Movie Title: {movie_title} \n\tAvailable Copies: {available_copies}')

    def view_customers(self):
        for index in self.customers:
            customer_id = index['id']
            customer_first_name = index['first_name']
            customer_last_name = index['last_name']
            print(f'customer id and name: {customer_id}, {customer_first_name} {customer_last_name}')

    def list_of_rented_videos(self, user_id):
        vid_list = []
        new_list = ''
        length = len(self.customers)
        if int(user_id) > length:
            print('User does not exist in the database.')
        for index in self.customers:
            if user_id == index['id']:
                vid_list.append(index['current_video_rentals'])
                new_list = ', '.join(vid_list)
                new_list = new_list.replace('/', ', ')
                if len(new_list) == 0 or new_list == None:
                    return print('No movies currently rented')
        return print(f'Currently this customer has the following items rented: \n{new_list}')

    def add_new_customer(self):
        new_customer = {}
        updated_list = self.customers
        length_list = []
        new_id = 0
        for item in updated_list:
            length_list.append(item)
        new_id = len(length_list) + 1
        new_customer['id'] = str(new_id)
        account_type = input('Select account type:\n"sx" = standard account: max 1 rental out at a time\n"px" = premium account: max 3 rentals out at a time\n"sf"= standard family account: max 1 rental out at a time AND can not rent any "R" rated movies\n"pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies\n')
        if account_type == 'sx' or account_type == 'px' or account_type == 'sf' or account_type == 'pf':
             new_customer['account_type'] = account_type
        else:
            print('Invalid response!!')
            return Store.add_new_customer(self) 
        first_name = input('Enter your first name: \n')
        new_customer['first_name'] = first_name
        last_name = input('Enter Your last name: \n')
        new_customer['last_name'] = last_name
        new_customer['current_video_rentals'] = ''
        self.customers.append(new_customer)
        print(self.customers)
        return print(new_customer)

    def rent_video_to_customer(self,user_movie, user_id):
        length = len(self.customers)
        if int(user_id) > length:
            return print('User does not exist in the database.')
        the_customer_acct = ''
        value_to_subtract = 0
        the_movie = ''
        vid_id = 0
        amount_in_stock = 0
        movies_currently_rented = []
        string_movies = ''
        count = 0
        for index in self.customers:
            if user_id == index['id']:
                the_customer_acct = index['account_type']
                movies_currently_rented.append(index['current_video_rentals'])
        string_movies = ', '.join(movies_currently_rented)
        string_movies = string_movies.replace('/', ', ')
        if len(string_movies) == 0:
            count += 0
        if len(string_movies) > 0:
            count += (len(string_movies.split(', ')))
        if the_customer_acct == 'sx' or the_customer_acct == 'sf':
            if count >= 1:
                return print('It seems your at your accounts maximum rental allowance.')
        elif the_customer_acct == 'px' or the_customer_acct == 'pf':
            if count >= 3:
                return print('It seems your at your accounts maximum rental allowance.')
        for j in self.inventory:
            if user_movie == j['title']:
                vid_id = j['id'] 
                vid_id = int(vid_id) - 1
                the_movie = j['rating']
                amount_in_stock = j['copies_available']
                amount_in_stock = int(amount_in_stock)
                value_to_subtract = amount_in_stock - 1
        if the_customer_acct == 'sf' or the_customer_acct == 'pf':
            if the_movie == 'R':
                return print("You're not allowed to rent that movie!")
        if amount_in_stock < 1:
            return print('Sorry we are currently out of stock')
        self.inventory[vid_id]['copies_available'] = str(value_to_subtract)
        user_id = int(user_id) - 1
        if count == 0:
            self.customers[user_id]['current_video_rentals'] = self.customers[user_id]['current_video_rentals'] + f'{user_movie}'
        else:
            self.customers[user_id]['current_video_rentals'] = self.customers[user_id]['current_video_rentals'] + f'/{user_movie}'
        print(self.customers)
        return print('Enjoy your Movie! Inventory has been updated.')
    
    def return_video(self, user_id, user_movie):
        vid_list = []
        new_list = ''
        movie_index = 0
        amount_in_stock = 0
        value_to_add = 0
        user_index = int(user_id) - 1
        for index in self.customers:
            if user_id == index['id']:
                vid_list.append(index['current_video_rentals'])
                new_list = ', '.join(vid_list)
                new_list = new_list.replace('/', ', ')
                vid_list = new_list.split(', ')
        for movie in vid_list:
            if movie == user_movie:
                vid_list.remove(user_movie)
                new_list = '/'.join(vid_list)
        for j in self.inventory:
            if user_movie == j['title']:
                movie_index = j['id']
                movie_index = int(movie_index)-1
                amount_in_stock = j['copies_available']
                amount_in_stock = int(amount_in_stock)
                value_to_add = amount_in_stock + 1
        self.inventory[movie_index]['copies_available'] = value_to_add
        self.customers[user_index]['current_video_rentals'] = new_list
        print(self.customers)
        print(self.inventory)
        return print('Your Movie has been returned and restocked in inventory.')
            
       
      
     
     




        

