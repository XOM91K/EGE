from functools import lru_cache


def command_A(n):
    return n - 3 if n >= 3 else None


def command_B(n):
    return n // 3 if n >= 3 else None


def command_C(n):
    return n // 2 if n >= 2 else None


@lru_cache(None)
def count_programs(n):
    if n == 3:
        return 1
    if n < 3:
        return 0

    paths = 0

    # Применяем команды, если возможно
    for command in [command_A, command_B, command_C]:
        new_n = command(n)
        if new_n is not None:
            if 20 in trace_path(n) and 28 not in trace_path(n):
                paths += count_programs(new_n)

    return paths


def trace_path(n):
    """Восстанавливает траекторию вычислений."""
    path = []
    while n >= 3:
        path.append(n)
        if n % 3 == 0:
            n //= 3
        elif n % 2 == 0:
            n //= 2
        else:
            n -= 3
    path.append(n)
    return path


print(count_programs(46))