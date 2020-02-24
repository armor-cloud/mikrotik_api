import asyncio
from aio_api_ros import create_rosapi_connection

async def main():
    # устанавливаем коннект
    mk = await create_rosapi_connection(
        mk_ip='172.17.0.37',
        mk_port=8728,
        mk_user='mt_api',
        mk_psw='ctrhtn'
    )
    # отправляем команду
    mk.talk_word('/ip/address/print')
    # считываем ответ от микротика
    res = await mk.read()
    print(res)
    mk.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()