epsilon = 10 ** (-5)


def equation(root: float) -> float:
    return root ** 3 - 3 * root ** 2 - 14 * root - 8


def equation1(root: float) -> float:
    return 3 * root * 2 - 6 * root - 14


def equation2(root: float) -> float:
    return 6 * root - 6


def find_root_newton(a: float, b: float) -> float:
    print('-' * 20 + 'Newton Method' + '-' * 31)
    x_middle = (a + b) / 2
    next_x = x_middle - equation(x_middle) / equation1(x_middle)

    for i in range(1, 100):
        x_middle = next_x
        next_x = x_middle - equation(x_middle) / equation1(x_middle)
        if abs(next_x - x_middle) <= epsilon:
            print('Found root: at {} iteration root: {:.6f}'.format(i, next_x))
            break

    print('-' * 64)
    return next_x


def find_root_simple_iterations(a: float, b: float) -> float:
    print('-' * 20 + 'Simple Iterations Method' + '-' * 20)
    t = -2 / (equation1(a) + equation1(b))
    x_middle = (a + b) / 2
    next_x = x_middle + t * equation(x_middle)
    for i in range(1, 100):
        x_middle = next_x
        next_x = x_middle + t * equation(x_middle)
        if abs(x_middle - next_x) <= epsilon:
            print('Found root: at {} iteration root: {:.6f}'.format(i, next_x))
            break
    print('-' * 64)
    return next_x


if __name__ == '__main__':
    find_root_simple_iterations(-3, -1)
    find_root_simple_iterations(-1, 0)

    find_root_newton(-3, -1)
    find_root_newton(-1, 0)
