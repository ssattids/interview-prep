class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        # the stack will hold a tuple and it's duration
        my_stack = []
        n_count = [0]*n # initialize the array to be zeros

        for i in range(0, len(logs)):
            fid, op_type, time = logs[i].split(":")
            fid, time = int(fid), int(time)
            # add the current function to the stack
            if op_type == 'start':
                if my_stack == []:
                    my_stack.append((fid, 0))
                else:
                    # get the previous function in the stack
                    prev_fid, duration = my_stack.pop()
                    if prev_op_type == 'start':
                        duration += time-prev_time
                    else:
                        duration += time-prev_time-1
                    # update previous function in the stack
                    my_stack.append((prev_fid, duration))
                    # add new function stack
                    my_stack.append((fid, 0))
            # remove the current function from the stack
            elif op_type == 'end':
                prev_fid, duration = my_stack.pop()
                if prev_op_type == 'start':
                    duration += time-prev_time+1
                else:
                    duration += time-prev_time
                n_count[prev_fid] += duration
            else:
                raise Exception('Invalid op type')
            
            prev_op_type = op_type
            prev_time = time

        return n_count