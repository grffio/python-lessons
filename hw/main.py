import task_1
import task_2
import task_3
import task_4
import task_5

task_1_input = "special string"
task_2_input = [1, 2, 3, 4, None, 'test', True, (1, 2, 3)]
task_3_input = "123;122.5;0.5;0.0;123.5"
task_4_input = "12abcdef56"
task_5_input = {'a': 1, 'b': 2}

task_1_result = task_1.char_counter(task_1_input)
task_2_result = task_2.pop_div2(task_2_input)
task_3_result = task_3.max_num_parser(task_3_input)
task_4_result = task_4.masquerade(task_4_input)
task_5_result = task_5.swap_dict(task_5_input)

print(f"Task 1 result: {task_1_result}")
print(f"Task 2 result: {task_2_result}")
print(f"Task 3 result: {task_3_result}")
print(f"Task 4 result: {task_4_result}")
print(f"Task 5 result: {task_5_result}")
