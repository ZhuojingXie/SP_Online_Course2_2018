"""
    mongodb example
"""

import pprint
import src.login_database as ld
import src.utilities as ut

log = ut.configure_logger('default', '../logs/mongodb_script.log')


def run_example(furniture_items):
    """
    mongodb data manipulation
    """

    with ld.login_mongodb_cloud() as client:
        log.info('Step 1: We are going to use a database called dev')
        log.info('But if it doesnt exist mongodb creates it')
        db = client['dev']

        log.info('And in that database use a collection called furniture')
        log.info('If it doesnt exist mongodb creates it')

        furniture = db['furniture']

        log.info('Step 2: Now we add data from the dictionary above')
        furniture.insert_many(furniture_items)

        log.info('Step 3: Find the products with a color of Red')
        query = {'color': 'Red'}
        results = furniture.find(query)


        log.info('Step 4: Print the red products')
        print('Red products')
        for x in results:
            pprint.pprint(x)

        log.info('Step 5: Find the products with a color of Red and product type couch')
        query = {'color': 'Red', 'product type': 'Couch'}
        results = furniture.find(query)

        log.info('Step 4: Print the red couches')
        print('Couch and Red product')
        for x in results:
            pprint.pprint(x)

        """log.info('Step 5: Delete the blue couch (actually deletes all blue couches)')
        furniture.remove({"product": {"$eq": "Blue couch"}})

        log.info('Step 6: Check it is deleted with a query and print')
        query = {'product': 'Blue couch'}
        results = furniture.find_one(query)
        print('The blue couch is deleted, print should show none:')
        pprint.pprint(results)

        log.info(
            'Step 7: Find multiple documents, iterate though the results and print')

        cursor = furniture.find({'monthly_rental_cost': {'$gte': 15.00}}).sort('monthly_rental_cost', 1)
        print('Results of search')
        log.info('Notice how we parse out the data from the document')

        for doc in cursor:
            print(f"Cost: {doc['monthly_rental_cost']} product name: {doc['product']} Stock: {doc['in_stock_quantity']}")"""

        log.info('Step 8: Delete the collection so we can start over')
        db.drop_collection('furniture')
