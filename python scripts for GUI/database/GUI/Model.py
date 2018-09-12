#from Database.Query import process_query

def get_parameters(input_list):
    sound = input_list[0]
    gesture = input_list[1]
    p_flag = input_list[2]
    count = input_list[3]
    pcount = input_list[4]
    return generate_query_table(sound, p_flag, count, pcount)


def generate_query_table(sound, p_flag, count, pcount):
    if(sound == 'No Sound'):
        s= 'no_sound'
    elif(sound == 'With Sound'):
        s= 'sound'

    if(p_flag == 1):
        table = 'pcount_'+ str(s)
        query = 'SELECT * FROM ' + table + ' WHERE count>' + str(count) + ' AND p_count>' + str(pcount) + ';'
    else:
        query = 'SELECT * FROM ' + s + ' WHERE count>' + str(count) + ';'

    return process_query(query)