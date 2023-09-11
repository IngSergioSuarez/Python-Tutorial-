
Log = input(" Ingrese el log: ") # the code receive the string with the logs.

first_Filter_Logs = Log[16:] # We eliminate the first 16 chatraceteres of the logs  "D"SP:<sy><sy><sx>" thati indicates is sending by the Dispatch

second_Filter_Logs = first_Filter_Logs.split("<cr>") # The second filter create a list of values, and separate by the characters "<cr>"

for x in second_Filter_Logs:

    if x.startswith('T') == True:
        print (x[:4] + "-----" + x[4:]) 

    else: 
        print(x[:3] + "-----" + x[3:])

        
    



