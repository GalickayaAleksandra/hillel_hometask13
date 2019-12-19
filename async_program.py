import asyncio
import os
from functools import reduce
from read_file import read_file, write_file


async def function_process(dirs, name_file):
    result = 0
    road_file = dirs + "/" + name_file
    str_file = read_file(road_file)
    action = str_file[0].replace("\n", "")
    list_number = str_file[1].split()
    list_float_number = [float(k) for k in list_number]
    if action == '1':
        sum_number = reduce(lambda x, res: x + res, list_float_number)
        result = sum_number
    if action == '2':
        mul_number = reduce(lambda x, y: x * y, list_float_number)
        result = mul_number
    if action == '3':
        double_list = [x * x for x in list_float_number]
        sum_double = reduce(lambda x, res: x + res, double_list)
        result = sum_double
    return result


async def main(direct, fln):
    tasks = []
    for i in fln:
        task_func_process = asyncio.ensure_future(function_process(direct, i))
        tasks.append(task_func_process)

    return await asyncio.gather(*tasks)


directory = "./in.dat"
files = os.listdir(directory)
loop = asyncio.get_event_loop()
all_results = sum(loop.run_until_complete(main(directory, files)))
write_file("./out.dat", str(all_results))
print(all_results)
