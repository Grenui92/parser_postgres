from models import Authors, Quote
import json
import aiofiles
from connect import session


async def load_authors_from_file():
    async with aiofiles.open('json_files/authors.json', mode='r') as file:
        res = await file.read()
        data = json.loads(res)


    for record in data:
        author = Authors(fullname=record['fullname'],
                        born_date=record['born_date'],
                        born_location=record['born_location'],
                        description=record['description'])
        session.add(author)
        session.commit()



async def load_quotes_from_file():
    async with aiofiles.open('json_files/quotes.json', 'r') as file:
        res = await file.read()
        data = json.loads(res)


    for record in data:

        if record['author'] == 'Alexandre Dumas fils':
            #Я про цей випадок пита в слак
            record['author'] = 'Alexandre Dumas-fils'

        author_id = (session.query(Authors.author_id)
                  .filter(Authors.fullname.contains(record['author']))
                  .first())
        try:
            quote = Quote(tags=record['tags'],
                           author=author_id[0],
                           quote=record['quote'])
            session.add(quote)
            session.commit()

        except AttributeError:
            print(f'I cant find author "{record["author"]}"')



if __name__ == '__main__':

    load_authors_from_file()