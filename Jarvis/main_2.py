from bs4 import BeautifulSoup
import asyncio
import aiohttp


async def gather_data():

    headers = {"Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    url = 'https://2gis.ru/ufa/search/%D0%92%D0%BA%D1%83%D1%81%D0%BD%D0%BE%20%E2%80%94%20%D0%B8%20%D1%82%D0%BE%D1%87%D0%BA%D0%B0%2C%20%D0%B1%D1%8B%D1%81%D1%82%D1%80%D0%BE%D0%B5%20%D0%BF%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B5/firm/70000001006794970/55.992071%2C54.746479/tab/reviews'



    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), 'lxml')
        cards = soup.find_all('div', class_='_klarpw')
        print(cards)


async def main():
    await gather_data()


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())



