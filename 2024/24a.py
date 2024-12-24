from aocd import data, submit
import asyncio

data, operations = data.split("\n\n")
data = {x.split(": ")[0]: bool(int(x.split(": ")[1])) for x in data.splitlines()}
operations = [x.split(" ") for x in operations.splitlines()]
condition = asyncio.Condition()

operations_map = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x != y
}

async def calc(x, y, op, z):
    async with condition:
        await condition.wait_for(lambda: x in data and y in data)
    async with condition:
        data[z] = operations_map[op](data[x], data[y])
        condition.notify_all()

async def main():
    tasks = []
    for x, op, y, _, z in operations:
        tasks.append(calc(x, y, op, z))
    await asyncio.gather(*tasks)

    i = 0
    result = 0
    while f"z{i:02}" in data:
        result += data[f"z{i:02}"] << i
        i += 1

    print(result)
    submit(result)


asyncio.run(main())