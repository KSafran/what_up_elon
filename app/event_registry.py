import os
import eventregistry as er

ER_KEY = os.getenv('ER_KEY',
                   'keys/event_reg_key.txt')

def authenticate():
    with open(ER_KEY, 'r') as key:
        auth_key = key.read().splitlines()[0]
    return er.EventRegistry(auth_key)

def get_elon_headlines():
    event_reg = authenticate()
    concept = er.QueryArticlesIter(keywords = "Elon Musk")
    return [news['title'] for news in
            concept.execQuery(event_reg, sortBy = "socialScore", maxItems = 10)]

if __name__ == '__main__':
    news = get_elon_headlines()
