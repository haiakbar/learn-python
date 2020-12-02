def arithmetic_arranger(problems, show_result=False):
    
    #initialize result format
    first_line_res = []
    second_line_res = []
    dashed_line_res = []
    result_line_res = []
        
    #Problem limiter
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    #iterate problems
    for i in range(len(problems)):
        separated = problems[i].split()
        
        if separated[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        operand = separated[1]
        length = max([len(separated[0]), len(separated[2])]) + 2
        first, second = separated[0], separated[2] 
        
        try:
            int(first)
            int(second)
        except:
            return 'Error: Numbers must only contain digits.'
    
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_line = ' '*(length-len(first)) + first
        second_line = operand + ' '*(length-len(second)-1) + second
        dashed_line = '-'*length
        
        first_line_res.append(first_line)
        second_line_res.append(second_line)
        dashed_line_res.append(dashed_line)
        
        if show_result:
            if operand == '+':
                result = int(first) + int(second)
            else:
                result = int(first) - int(second)
            
            result_line = ' '*(length-len(str(result))) + str(result)
            result_line_res.append(result_line)
        
    first_line_joined = '    '.join(first_line_res)
    second_line_joined = '    '.join(second_line_res)
    dashed_line_joined = '    '.join(dashed_line_res)
    
    if not show_result:
        arranged_problems = first_line_joined+'\n'+second_line_joined+'\n'+dashed_line_joined
    else:
        result_line_joined = '    '.join(result_line_res)
        arranged_problems = first_line_joined+'\n'+second_line_joined+'\n'+dashed_line_joined+'\n'+result_line_joined
        
    return arranged_problems
