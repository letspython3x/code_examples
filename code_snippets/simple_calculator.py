import argparse


def parse_cmdline():
    parser = argparse.ArgumentParser()
    parser.add_argument('operand1', help='', type=int)
    parser.add_argument('operand2', help='', type=int)
    operation = parser.add_mutually_exclusive_group()
    operation.add_argument('--add', help="To Perform Addition", action="store_true")
    operation.add_argument('--div', help="To Perform division", action="store_true")
    operation.add_argument('--mul', help="To Perform multiplication", action="store_true")
    operation.add_argument('--sub', help="To Perform Substraction", action="store_true")
    args = parser.parse_args()
    return args


class Calculator(object):
    @staticmethod
    def add(operand1, operand2):
        return operand1 + operand2

    @staticmethod
    def substract(operand1, operand2):
        return operand1 - operand2

    @staticmethod
    def multiply(operand1, operand2):
        return operand1 * operand2

    @staticmethod
    def divide(dividend, divisor):
        result = dividend / divisor
        return result

    @staticmethod
    def divide2(dividend, divisor):
        try:
            result = dividend / divisor
            return result
        except ZeroDivisionError:
            print("Divisor should not be zero (0)")
        except:
            print("Invalid operation %s / %s" % (dividend, divisor))

    @staticmethod
    def check_and_return_operation_if_valid(op):
        if op.add:
            return Calculator.add
        elif op.div:
            return Calculator.divide
        elif op.mul:
            return Calculator.multiply
        elif op.sub:
            return Calculator.substract
        else:
            print("Invalid Operation with %s" % op)

    def perform_operation(self, args):
        operation = self.check_and_return_operation_if_valid(args)
        if operation:
            result = operation(args.operand1, args.operand2)
            return result


def main():
    args = parse_cmdline()
    cal = Calculator()
    result = cal.perform_operation(args)
    print("Result: %s" % result)


if __name__ == "__main__":
    main()
