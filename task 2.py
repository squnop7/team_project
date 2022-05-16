#2 Камень, ножницы, бумага


#Импортирую choice, чтобы реализовать выбор бота
from random import choice


#функци меню (запуск/ помощь/ выключение меню)
#*Всё описано в самой функции меню*
def menu():
    answer = 2
    while answer not in [0, 1]:
        print('Камень ножницы бумага')
        print('Введите :', '\n', \
          '1 - для запуска игры', '\n', \
          '2 - для помощи', '\n', \
          '0 - для выхода из игры')
        
        answer = int(input('Введите число (0-2) >>> '))
        print()
        
        if answer == 2:
            print('Правила :', '\n'
                  '1)Во время игры игроку желательно', '\n'
                  'отворачиваться от ввода оппонента', '\n'
                  '2)Ножницы режут бумагу,', '\n'
                  'бумага заворачивает камень,', '\n'
                  'камень ломает ножницы', '\n'
                  '3)Для ввода используйте англ. язык', '\n',
                  'а именно заглавные буквы : K(Kамень) N(Nожницы) B(Bумага)', '\n')

        
        if answer == 0:
            return False
        
        elif answer == 1:
            return True

        elif answer != 2:
            print('---Ошибка ввода---')
            return False


#Функция основного хода игры
def GameAction(Rounds):
        #Rule определяет игру с ботом или с человеком
        Rule = 3
        while Rule not in [0, 1]:
            Rule = int(input('Введите 0, чтобы играть с ботом, или 1, с человеком >>> '))

        #Игра с человеками  
        if Rule == 1:
            #Ввод имен игроков
            P1 = str(input('Введите имя 1-го игрока >>> '))
            P2 = str(input('Введите имя 2-го игрока >>> '))

            #P(1/2)WIns - кол-во побед игрока
            P1Wins = 0
            P2Wins = 0

            #Номер конкретного раунда
            RoundCount = 0
            while RoundCount != Rounds:

                #Переменная игрового выбора за ход конкретного игрока
                P1Choice = 0
                P2Choice = 0

                print('|' + 38 * '-' + '|')
                
                print('Раунд', RoundCount + 1)

                #Выбор игроков за ход
                while P1Choice not in ['K', 'N', 'B']:
                    print('Ход игрока', P1, '(K,N,B) >>> ')
                    P1Choice = str(input('>>> '))
                    #Проверка выбора хода на правильность
                    if P1Choice not in ['K', 'N', 'B']:
                        print('Вводите только буквы: K-камень N-ножницы B-бумага')
                    else:
                        #Этот print прячет ход предыдущего игрока
                        print(40 * '\n')
                while P2Choice not in ['K', 'N', 'B']:
                    print('Ход игрока', P2, '(K,N,B) >>> ')
                    P2Choice = str(input('>>> '))
                    #Проверка выбора хода на правильность
                    if P2Choice not in ['K', 'N', 'B']:
                        print('Вводите только буквы: K-камень N-ножницы B-бумага')
                    else:
                        #Этот print прячет ход предыдущего игрока
                        print(40 * '\n')
                    
                if P1Choice == P2Choice:
                    ###ВАЖНО!!!
                    ###Я решил засчитывать ничью за раунд, как победу для обоих,
                    ###чтобы партия не затягивалась надолго
                    P1Wins += 1
                    P2Wins += 1
                    print('Ничья', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')

                #Модуль сравнения разных ходов
                if P1Choice == 'K' and P2Choice == 'N':
                    P1Wins += 1
                    print('Игрок', P1, 'выиграл раунд (Камень/Ножницы)', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')
                if P1Choice == 'K' and P2Choice == 'B':
                    P2Wins += 1
                    print('Игрок', P2, 'выиграл раунд (Камень/Бумага)', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')
                if P1Choice == 'N' and P2Choice == 'K':
                    P2Wins += 1
                    print('Игрок', P2, 'выиграл раунд (Ножницы/Камень)', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')
                if P1Choice == 'N' and P2Choice == 'B':
                    P1Wins += 1
                    print('Игрок', P1, 'выиграл раунд (Ножницы/бумага)', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')
                if P1Choice == 'B' and P2Choice == 'N':
                    P2Wins += 1
                    print('Игрок', P2, 'выиграл раунд (Бумага/Ножницы)', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')
                if P1Choice == 'B' and P2Choice == 'K':
                    P1Wins += 1
                    print('Игрок', P1, 'выиграл раунд (Бумага/Камень)', '\n', \
                          '(', P1Wins, ':', P2Wins, ')')
                #Переход на следующий раунд
                RoundCount += 1

            #Завершение игры/ подведение итогов
            if P1Wins == Rounds or P2Wins == Rounds:
                if P1Wins == P2Wins:
                    print('Ничья !', '\n', \
                          'Ваш счёт -', '(', P1Wins, ':', P2Wins, ')')
                elif P1Wins > P2Wins:
                    print('Победил игрок', P1, 'со счётом -', '(', P1Wins, ':', P2Wins, ')')
                else:
                    print('Победил игрок', P2, 'со счётом -', '(', P2Wins, ':', P1Wins, ')')

                print('|' + 38 * '-' + '|')

        #Игра с ботом (описание всего модуля аналогично
        #с тем, что было в случае двух игроков)
        if Rule == 0:
            
            PWins = 0
            BotWins = 0
            
            RoundCount = 0
            while RoundCount != Rounds:
                
                PChoice = 0
                BotChoice = 0

                print('|' + 38 * '-' + '|')
                
                print('Раунд', RoundCount + 1)
                
                while PChoice not in ['K', 'N', 'B']:
                    PChoice = str(input('Ход игрока (K,N,B) >>> '))
                BotChoice = choice(['K', 'N', 'B'])

                if PChoice == BotChoice:  
                    PWins += 1
                    BotWins += 1
                    print('Ничья', '\n', \
                          '(', PWins, ':', BotWins, ')')

                if PChoice == 'K' and BotChoice == 'N':
                    PWins += 1
                    print('Игрок выиграл раунд (Камень/Ножницы)', '\n', \
                          '(', PWins, ':', BotWins, ')')
                if PChoice == 'K' and BotChoice == 'B':
                    BotWins += 1
                    print('Бот выиграл раунд (Камень/Бумага)', '\n', \
                          '(', PWins, ':', BotWins, ')')
                if PChoice == 'N' and BotChoice == 'K':
                    BotWins += 1
                    print('Бот выиграл раунд (Ножницы/Камень)', '\n', \
                          '(', PWins, ':', BotWins, ')')
                if PChoice == 'N' and BotChoice == 'B':
                    PWins += 1
                    print('Игрок выиграл раунд (Ножницы/бумага)', '\n', \
                          '(', PWins, ':', BotWins, ')')
                if PChoice == 'B' and BotChoice == 'N':
                    BotWins += 1
                    print('Бот выиграл раунд (Бумага/Ножницы)', '\n', \
                          '(', PWins, ':', BotWins, ')')
                if PChoice == 'B' and BotChoice == 'K':
                    PWins += 1
                    print('Игрок выиграл раунд (Бумага/Камень)', '\n', \
                          '(', PWins, ':', BotWins, ')')

                RoundCount += 1

            if PWins == Rounds or BotWins == Rounds:
                if PWins == BotWins:
                    print('Ничья !', '\n', \
                          'Ваш счёт -', '(', PWins, ':', BotWins, ')')
                elif PWins > BotWins:
                    print('Победил игрок со счётом -', '(', PWins, ':', BotWins, ')')
                else:
                    print('Победил бот со счётом -', '(', BotWins, ':', PWins, ')')

                print('|' + 38 * '-' + '|')

#Общая функция игры (Меню/ игра/ завершение игры)
def Game():
    #Повторитель игры
    GameTrigger = 1
    #Включатель игры (через меню)
    trigger = menu()
    
    while GameTrigger == 1:
        if trigger == False:
            GameTrigger = 0
            #Конец работы означает, что игра не была запущена
            print('---Конец работы---')
        else:
            #Провекрка верности заданного кол-ва раундов (> 0)
            rounds = 0
            while rounds == 0:
                rounds = int(input('Введите кол-во раундов >>> '))
                if rounds <= 0:
                    print('Кол-во раундов - только натуральное большие нуля')
            GameAction(rounds)

        #Модуль повторного запуска/ завершения игры
        if trigger != False:
            GameTrigger = int(input('Играем ещё ? (0 - нет, 1 - да) >>> '))

        if GameTrigger != 1:
            print('---Конец игры---')

       
Game()

#Программа включает в себя такие выводы как:
#---Ошибка ввода---
#---Конец работы---
#---Конец игры---
#для возможности определить ошибку

