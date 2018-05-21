'''
There are number of bulbs in a row with switches for each.
When a switch is turned ON, all the switches on the right toggle their state
This function below counts the total number of switches to be turned ON for a given set of initial state of
bulbs(0-OFF, 1-ON) such that all the bulbs are ON.
'''


def count_switch_changes(switch_states):
    count=0
    templist = []
    for i in range(len(switch_states)):
        if not switch_states[i]:
            switch_states = templist+[0 if switch_states[j] else 1 for j in range(i, len(switch_states))]
            count+=1
            if all(switch_states):
                break
        templist.append(1)
        #print(switch_states,ct)
    return(count)