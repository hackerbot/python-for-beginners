def LogFile():
    from OwnCode.ch10lab_LogMessageFile import LogMessageFile
    print(LogMessageFile)

def LogDb():
    from OwnCode.ch11lab_LogMessageDbSQL import LogMessageDbSQL
    print(LogMessageDbSQL)
    
def select():
    selection = int(input('Would you like to read and edit a file or database?\nPress 1 to run LogFile()\nPress 2 to run LogDb()\nMake your selection:\n'))
    while selection != 1 or 2:
        selection = int(input('Please enter your selection again:\n'))
        if selection == 1:
            LogFile()
            selection2 = int(input('Would you like to edit database?\nPress 1 = Yes\nPress 2 = No\n'))
            if selection2 == 1:
                LogDb()
                print('Congratulations you have ran both classes and you are good to go! :)')
                break
            elif selection2 == 2:
                print('You are good to go! :)')
                break
        elif selection == 2:
            LogDb()
            selection2 = int(input('Would you like to edit database?\nPress 1 = Yes\nPress 2 = No\n'))
            if selection2 == 1:
                LogFile()
                print('Congratulations you have ran both classes and you are good to go! :)')
                break
            elif selection2 == 2:
                print('You are good to go! :)')
                break
                
select()