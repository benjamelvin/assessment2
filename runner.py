# Write your solution here!
from classes.Store import Store

store = Store('THE LAST BLOCKBUSTER') 
while True:
    mode = input("\n== Welcome to Code Platoon Video! ==\nOptions:\n1. View store video inventory\n2. View Store Customers\n3. View customers rented videos\n4. Add new customer\n5. Rent video\n6. Return video\n7. Exit\n")

    if mode == '1':

        store.list_current_inventory()
    if mode == '2':
        store.view_customers()
    if mode == '3':
        user_id = input('Enter user id: ')
        store.list_of_rented_videos(user_id)
    if mode == '4':
        store.add_new_customer()
    if mode == '5':
        user_movie = input('What movie are you renting? ')
        user_id = input('Enter user id: ')
        store.rent_video_to_customer(user_movie, user_id)
    if mode == '6':
        user_id = input('Enter user id: ')
        user_movie = user_movie = input('What movie are you returning? ')
        store.return_video(user_id, user_movie)
    if mode == '7':
        quit()
        