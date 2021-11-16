import psycopg2
import requests
import random
pg_details = {'host': 'localhost', 'user':'postgres', 'password': 'varlamov', 'dbname':'postgres'}
def run_query(query, mode='w'):
    connection = psycopg2.connect(**pg_details)
    cursor = connection.cursor()
    cursor.execute(query)
    if mode == 'ra':
        results = cursor.fetchall()
    if mode == 'r1':
        results = cursor.fetchone()
    connection.commit()
    connection.close()
    if 'r' in mode :
        return results
    print('db update successfully')

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
random_10 = random.sample(data, k=10)
# random.choice(list) choose a single random object from list
# random.choices(list, k=num), choose num random objects (not necissarily unique )
# random.sample(list, k=num), choose num random UNIQUE objects from list

for country_data in random_10:
    query = f"INSERT INTO countries (name, capital, flag, subregion, population) VALUES ('{country_data['name']['common']}', '{str(country_data['capital'][0])}','{country_data['flag']}','{country_data.get('subregion', 'no subregion')}','{country_data['population']}') "
    run_query(query)