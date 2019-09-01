class CustomError(Exception):
    pass

def pole_notation_calc():
    try:
        calc_list = input('Введите выражение: \n').split(' ')
        operand_values = ['+', '-', '*', ':', '/']
        operand_error = f'{calc_list[0]} некорректный операнд!'
        assert calc_list[0] in operand_values, print(operand_error)
        if len(calc_list) > 3:
            raise CustomError
        if calc_list[0] == '+':
            result = (int(calc_list[1]) + int(calc_list[2]))
        elif calc_list[0] == '-':
            result = (int(calc_list[1]) - int(calc_list[2]))
        elif calc_list[0] == '*':
            result = (int(calc_list[1]) * int(calc_list[2]))
        elif calc_list[0] == ':' or calc_list[0] == '/':
            result = (int(calc_list[1]) / int(calc_list[2]))
    except ZeroDivisionError as e:
        print('На ноль делить нельзя!')
        return type(e)
    except ValueError as e:
        print('Буквы и знаки калькулятор не обрабатывает!')
        return type(e)
    except AssertionError as e:
        return type(e)
    except CustomError as e:
        return 'Вводите не более двух чисел!'
        return type(e)
    except Exception as e:
        return type(e)
    else:
        return result

print(pole_notation_calc())