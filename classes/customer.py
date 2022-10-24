import csv
class Customer:

    def __init__(self, **kwargs):
        pass
    @classmethod
    def all_customers(cls):
        holder = []
        with open('./data/customers.csv') as customers_file:
            reader = csv.DictReader(customers_file)
            for row in reader:
                holder.append(row)
            return holder    


    
 
            
   


customer = Customer()
