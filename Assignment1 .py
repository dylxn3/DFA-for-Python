import sys

def process_input_file(input_file):
    file = open(input_file, "r")
    lines = file.readlines()

    #state that the dfa would be in
    states = ["start", "statement", "single_line_comment", "multi_line_comment", "single_line_string", "multi_line_string"]
    state = states[0]
    not_statement = ['#', '\\']

    newLines = []

    #0 = beginning of quote --- single line quote
    beg_flag = 0

    #0 = first line of multiline comment, 
    first_line =0

    in_multi_string =0

    for line in lines:
        line.lstrip()
        newString = ""
        # print(line)

        if line[0] not in not_statement and state!=states[3] and state!= states[5]: 
            state = states[1]
        

        if line[0] == '#':
            continue

    
        
        # print(line[0:3] + "Hit")
    #for the following 2 if statements, 1: if i see the beginning of a multi line comment change states and flag
        if (line[0:3] == '"""' or line[0:3] == "'''") and first_line ==0 and state!=states[5]: 
            state = states[3]
            continue
            
        
    #if the end of a multiline comment it reached, switch state back to start and reset flag and skip this line
        if first_line==1 and (line[0:3] == '"""' or line[0:3] == "'''") and state!=state[5]:
            state = states[0]
            first_line =0
            newString+="\n"   
            continue



        if (line[0:3] == '"""' or line[0:3] == "'''") and state == states[5] and in_multi_string==0:
            in_multi_string = 1
            newLines.append(line)
            continue

        if (line[0:3] == '"""' or line[0:3] == "'''") and state == states[5] and in_multi_string == 1:
            newLines.append(line)
            state= states[0]
            in_multi_string = 0
            continue


        for index, char in enumerate(line):
            #if in multiline comment state, just skip writing this 
            if state == states[3]:
                first_line =1
                continue

            if state == states[1]:

                if (char == "'" or char == '"') and beg_flag ==0 :
                    beg_flag =1
                    newString+=char
                    continue
                if beg_flag == 1 and (char == "'" or char == '"'):
                    state = states[1]
                    beg_flag = 0

                if char=="#" and beg_flag == 0:
                    state =states[0]
                    break

                if char == '\\':
                    state = states[5]
                    next_char= line[index+1]
                    if next_char == '\n':
                        newString+=(char+'\n')
                        break                    


            if state == states[5]:
                in_multi_string == 1
                    
            newString+=char
        
        newString+= "\n"
        newLines.append(newString)
                

    with open('input_file_rm.py', 'w') as file:
        for newLine in newLines:
            file.write(newLine)

if __name__ == "__main__":
    
    input_file = sys.argv[1]
    process_input_file(input_file)
