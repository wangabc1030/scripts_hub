def n_tab(n):
    return '\t' * n


def append_n_tab_to_lines(n, lines: str):
    return '\n'.join([n_tab(n) + l for l in lines.split('\n')])


# switch (variable_name) {
#     <case expressions here>
#     default:
#         break;
# }
def switch(variable_name, case_content):
    return f'switch ({variable_name}) {{\n' \
           + f'{append_n_tab_to_lines(1, case_content)}\n' \
           + n_tab(1) + 'default:\n' \
           + n_tab(2) + 'break;\n' \
           + '}\n'


# case "xxx":
#     <C-code here>
#     break;
def case(variable_value, case_content):
    return f'case "{variable_value}":\n' \
           + f'{append_n_tab_to_lines(1, case_content)}\n' \
           + n_tab(1) + 'break;\n'


def case_by_list(ca: list) -> str:
    return ''.join([case(c, f'printf("This is {c}!\\n")') for c in ca])


def constructor(data: dict):
    if len(data) == 1:
        k, v = next(iter(data.items()))
        if type(v) is list:
            return switch(k, case_by_list(v))
        elif type(v) is dict:
            return switch(k, constructor(v))
    else:
        ret = ''
        for k, v in data.items():
            ret += case(k, constructor(v))
        return ret


# Example: ################################################################
data_sample = {
    'country':
        {
            'CHINA':
                {
                    'province': ['Beijing', 'Jiangsu', 'Suzhou'],
                },

            'USA':
                {
                    'province': ['Pennsylvania', 'Texas'],
                }
        },
}

# '\t' count for indentation
glob_tab_cnt = 1
print(append_n_tab_to_lines(glob_tab_cnt, constructor(data_sample)))
#
#
# Output:
# D:\Applications\miniconda3\envs\py39\python.exe E:/Projects/PycharmProjects/z/main.py
# 	switch (country) {
# 		case "CHINA":
# 			switch (province) {
# 				case "Beijing":
# 					printf("This is Beijing!\n")
# 					break;
# 				case "Jiangsu":
# 					printf("This is Jiangsu!\n")
# 					break;
# 				case "Suzhou":
# 					printf("This is Suzhou!\n")
# 					break;
#
# 				default:
# 					break;
# 			}
#
# 			break;
# 		case "USA":
# 			switch (province) {
# 				case "Pennsylvania":
# 					printf("This is Pennsylvania!\n")
# 					break;
# 				case "Texas":
# 					printf("This is Texas!\n")
# 					break;
#
# 				default:
# 					break;
# 			}
#
# 			break;
#
# 		default:
# 			break;
# 	}
#
# Process finished with exit code 0
##########################################################################
