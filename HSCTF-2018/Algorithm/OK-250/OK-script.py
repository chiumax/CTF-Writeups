import sys
sys.setrecursionlimit(1500)
def ok(top):
    '''
Initial procedure. I used this to visualize the first couple replies / iterations of the messages.
'''
    iteration = 0 # counts how many replies have been made
    count = 0 # counts how many sets of consecutive O's whose length is at least 2
    temp_count = 0 # counts how many O's there are before reaching a K while iterating through a string
    string = 'K' # Since the first iteration doesn't count, I'm setting the string at K. And also because I need something in the string for it to work.
    string_temp = '' # Temporarily stores the edited string after one iteration / reply.
    #I did this because it is very complicated to loop through a list or string and edit it at the same time during the loop

    while iteration != top:
        for letter in string: # one iteration / reply
            if letter =='K':
                string_temp+= 'OK'
            else:
                string_temp +='KO'
                
        iteration +=1
        string = string_temp
        string_temp = ''

    for x in string: #counts how many sets of consecutive O's whose length is at least 2
        if x == 'O':
            temp_count +=1
        else:
            if temp_count >= 2:
                count +=1
            temp_count = 0
    return(string,count)

def ok_recursive(before,num,itera):
    itera -= 1
    if itera > 0:
        return ok_recursive(num,(before*2)+num,itera)
    return num


print(ok_recursive(0,1,999) )# Challenge answer

'''
TEST RUNS:
ex. ok_recursive(init_sequence,next_num,iter)
ex. ok(iter)
print (ok_recursive(0,1,4))
print(ok(5))
BOTH will print out the same number of sets of consecutive O's whose length is at least 2
This is because the ok() procedure starts iteration from 1 and the ok_recursive() starts from 0 (it counts the first message as a reply / iteration)
'''
