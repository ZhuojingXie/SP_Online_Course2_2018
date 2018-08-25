"""
    neo4j example
"""


import utilities
import login_database
import utilities
import random

log = utilities.configure_logger('default', '../logs/neo4j_script.log')


def run_example():

    log.info('Step 1: First, clear the entire database, so we can start over')
    log.info("Running clear_all")

    driver = login_database.login_neo4j_cloud()
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

    log.info("Step 2: Add a few people")

    with driver.session() as session:

        log.info('Adding a few Person nodes')
        log.info('The cyph language is analagous to sql for neo4j')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ('Christopher', 'Evans'),
                            ('Sheldon', 'Cooper'),
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
                first, last)
            session.run(cyph)

        log.info("Step 3: Get all of people in the DB:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        print("People in database:")
        for record in result:
            print(record['first_name'], record['last_name'])

        log.info('Step 4: Create some relationships')
        COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW']
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ('Christopher', 'Evans'),
                            ('Sheldon', 'Cooper'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'%s', last_name:'%s'})
              CREATE (p1)-[favorite:FAVORITE]->(p2:Color {name:'%s'})
              RETURN p1
            """ % (first, last, COLORS[random.randint(0,3)])
            session.run(cypher)

        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ('Christopher', 'Evans'),
                            ('Sheldon', 'Cooper'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'%s', last_name:'%s'})
                    -[:FAVORITE]->(favoriteColor)
              RETURN favoriteColor
              """ % (first, last)
            query = session.run(cypher)
            for search in query:
                for v in search.values():
                    if v:
                        print("{} {}\'s favorite color is: {}".format(first, last, v['name']))
            
