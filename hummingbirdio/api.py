from aioauth_client import TwitterClient
import asyncio
import async_timeout
import aiohttp
from aiofiles import open
from codecs import open as syncopen
from aiohttp import web
from urllib.parse import parse_qsl

from .calls import HummingBirdCalls, HummingBirdStreamCalls

try:
    import simplejson as json
except ImportError:
    import json


class TwitterClient(TwitterClient):
    async def _request(self, method, url, loop=None, timeout=None, stream_queue=False, **kwargs):
        """Make a request through AIOHTTP."""
        try:
            print(f'{method} {url} {kwargs}')
            async with async_timeout.timeout(timeout):
                async with aiohttp.ClientSession(loop=loop) as session:
                    async with session.request(method, url, **kwargs) as response:
                        print(kwargs)
                        if response.status / 100 > 2:
                            raise web.HTTPBadRequest(
                                reason='HTTP status code: %s' % response.status)

                        # Checks if stream_queue has a 'put' method, if yes then it assumes it's a queue
                        if callable(getattr(stream_queue, 'put', None)):
                            chunks = []
                            while True:
                                await asyncio.sleep(0.00001)
                                chunk = await response.content.read(1)
                                if chunk:
                                    chunks.append(chunk.decode('utf-8'))
                                    chunks = ["".join(chunks)]
                                    if len(chunks[0].splitlines()) >= 2:
                                        chunks[0] = chunks[0].splitlines()
                                        await stream_queue.put(json.loads(chunks[0].pop(0)))
                                        chunks = sum(chunks, [])
                                else:
                                    raise Exception('Stream ended')
                        elif stream_queue:
                            raise Exception('Stream queue must be a queue')
                        else:
                            if 'json' in response.headers.get('CONTENT-TYPE'):
                                data = await response.json()
                            else:
                                data = await response.text()
                                data = dict(parse_qsl(data))

                            return data
        except asyncio.TimeoutError:
            raise web.HTTPBadRequest(reason='HTTP timeout')


class HummingBird(HummingBirdCalls):
    def __init__(self, consumer_key, consumer_secret, oauth_token=None, oauth_token_secret=None):
        super().__init__(self)
        self.stream = HummingBirdStreamCalls(self)
        self.session = TwitterClient(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            oauth_token=oauth_token,
            oauth_token_secret=oauth_token_secret,
        )

    async def request(self, twiturl, method='GET', stream_queue=False, params=None):
        # Make values into strings for convenience
        for k, v in params.items():
            if not type(v) == str and not type(v) == dict:
                params[k] = str(v)

        if twiturl[:8] == 'https://' or twiturl[:7] == 'http://':
            self.session.base_url = ''
        else:
            self.session.base_url = 'https://api.twitter.com/1.1/'

        return await self.session.request(method, url=twiturl, stream_queue=stream_queue, params=params)


async def auth(app_key, app_secret, verify=False):
    """
    Basic OAuth1 for just one app and one user.
    :param app_key: Consumer Key (API Key)
    :param app_secret: Consumer Secret (API Secret)
    :param verify: Whether or not to verify your credentials. Leave disabled to do auth faster.
    :return: The authorized session for you to use.
    """
    unauthed = HummingBird(
        consumer_key=app_key,
        consumer_secret=app_secret,
    )
    request_token, request_token_secret, _ = await unauthed.session.get_request_token()

    try:
        async with open('hummingbird_credentials.json', 'r') as f:
            credentials = json.loads(await f.read())
        oauth_token = credentials['oauth_token']
        oauth_token_secret = credentials['oauth_token_secret']
        authed_session = HummingBird(
            consumer_key=app_key,
            consumer_secret=app_secret,
            oauth_token=oauth_token,
            oauth_token_secret=oauth_token_secret,
        )
        if verify:
            await authed_session.verify_credentials()
    except (IOError, aiohttp.web_exceptions.HTTPBadRequest):
        authorize_url = unauthed.session.get_authorize_url(request_token)
        print("Open {} in a browser".format(authorize_url))
        oauth_verifier = str(input("PIN code: "))
        oauth_token, oauth_token_secret, _ = await unauthed.session.get_access_token(oauth_verifier)

        credentials = {'oauth_token': oauth_token, 'oauth_token_secret': oauth_token_secret}
        async with open('hummingbird_credentials.json', 'w+') as f:
            await f.write(json.dumps(credentials))

        authed_session = HummingBird(
            consumer_key=app_key,
            consumer_secret=app_secret,
            oauth_token=oauth_token,
            oauth_token_secret=oauth_token_secret,
        )
        if verify:
            await authed_session.verify_credentials()
    return authed_session
