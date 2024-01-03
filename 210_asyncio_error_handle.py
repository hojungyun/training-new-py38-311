import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(funcName)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


async def do_something(no: int, sleep_time: int):
    try:
        logger.info(f"[{no}] do_something started. {sleep_time=}")
        await asyncio.sleep(sleep_time)
        if no == 2:
            raise ValueError(f"ValueError from {no=}, {sleep_time=}")
        if no == 3:
            raise TypeError(f"TypeError from {no=}, {sleep_time=}")
        logger.info(f"[{no}] done. {sleep_time=}")
    except asyncio.CancelledError:
        logger.warning(f"[{no}] canceled. {sleep_time=}")


async def do_w_gather():
    try:
        await asyncio.gather(
            do_something(1, 1),
            do_something(2, 2),
            do_something(3, 2),
            do_something(4, 5),
            do_something(5, 6),
        )
    except Exception as e:
        logger.exception(e)


async def do_w_taskgroup():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(do_something(1, 1))
            tg.create_task(do_something(2, 2))
            tg.create_task(do_something(3, 2))
            tg.create_task(do_something(4, 5))
            tg.create_task(do_something(5, 6))
    except* ValueError as eg:
        logger.exception(eg)
    except* TypeError as eg:
        logger.exception(eg)


async def main():

    # Test with gather
    # await do_w_gather()

    # Test with task group
    await do_w_taskgroup()

    logger.info("Post-processing..")
    await asyncio.sleep(5)
    logger.info("DONE")

if __name__ == "__main__":
    asyncio.run(main())
