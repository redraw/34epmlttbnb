from sanic import Sanic
from sanic.response import json
import aiohttp

app = Sanic()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('request: ', url)
            return await response.json()


@app.route('/api/ig')
async def index(request):
    content = {}

    if 'hashtag' in request.args:
        url = 'https://www.instagram.com/explore/tags'
        content = await fetch(f'{url}/{request.args.get("hashtag")}/?__a=1')

    return json(content, headers={
        'Cache-Control': 's-maxage=300',
        'Access-Control-Allow-Origin': '*'
    })
