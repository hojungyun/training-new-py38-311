import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(funcName)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


async def async_do_something(no: int, sleep_time: int):
    logger.info(f"[{no}] async_do_something started. {sleep_time=}")
    await asyncio.sleep(sleep_time)
    logger.info(f"[{no}] done. {sleep_time=}")


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(async_do_something(1, 2))
        tg.create_task(async_do_something(2, 1))
        tg.create_task(async_do_something(3, 1))
        tg.create_task(async_do_something(4, 2))


if __name__ == "__main__":
    asyncio.run(main())
