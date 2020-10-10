def ask_yes_no(questions):
    response=None
    while response not in ('y', 'n'):
        response=input(question+' (y/n)?').lower
    
def ask_number(question, low, high):
    response=None
    while response not in range(low, high+1):
        response=int(input(question))
    return response

if __name__=='__main__':
    print('Вы запустили модуль games, а не импортивали его.')
    input('\n\nНажмите Enter, что бы выйти.')