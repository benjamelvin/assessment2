import csv
class Inventory:

    def __init__(self, **kwargs):
        pass
    @classmethod
    def all_inventory(cls):
        holder = []
        with open('./data/inventory.csv') as inventory_file:
            reader = csv.DictReader(inventory_file)
            for row in reader:
                holder.append(row)
            return holder    


inventory = Inventory()

