# ------------------------------------------------------------
# Скрипт для решения квадратного уравнения
# Пример запроса: http://127.0.0.1:5000/equation?a=1&b=1&c=-6
#
# email: efimooov.stanislav@gmail.com
# ------------------------------------------------------------

import traceback
from flask import Flask
from flask_restful import Api, request
import math
app = Flask(__name__)
api = Api(app)
app.config['JSON_AS_ASCII'] = False

# функция для нахождения корней уравнения, если дискриминант больше 0
def get_equal(a, b, discr):
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    return round(x1, 2), round(x2, 2)


@app.route('/equation/', methods=['GET'])
def user():
    try:
        args = request.args
        a = args.get('a')
        b = args.get('b')
        c = args.get('c')

        numbers = [a, b, c]
        label = ['a','b', 'c']
        correct, non_correct = [], dict()

        for num in range(len(numbers)):
            try:
                numbers[num] = float(numbers[num])
            except:
                non_correct[label[num]] = numbers[num]

        # Проверка на корректность запроса, все ли там числа
        if len(non_correct) > 0:
            a = dict()
            a['Эти значения не являются числами'] = non_correct
            return a
        else:
            a, b, c = numbers[0], numbers[1], numbers[2]
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                return 'Корней уравнения нет'
            elif discriminant == 0:
                return f'Корень уравнения = {-b/2*a}'
            else:
                x1, x2 = get_equal(a, b, discriminant)
                return f'Корни уравнения: x1 = {x1}, x2 = {x2}'

    except:
        traceback.print_exc()
        return 'Такого запроса нет'

if __name__ == '__main__':
    app.run(debug=True)