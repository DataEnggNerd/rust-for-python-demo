import timeit


def nth_fibonacci(n: int):

    first = 0
    second = 1
    third = 1
    # print(first)
    # print(second)
    if n < 2: return n

    for num in range(2, n):

        third = first + second
        first = second
        second = third
        # print(third)
    return third


if __name__ == "__main__":
    nth_input = 60
    result = nth_fibonacci(nth_input)

    setup_python = "from __main__ import nth_fibonacci"

    python_timing = timeit.timeit(f"nth_fibonacci({nth_input})", setup=setup_python, number=1000)
    print(f"Time taken by python => {python_timing:.6f}")

    setup_rust = "from nth_fibonacci import fibonacci"
    rust_timing = timeit.timeit(f"fibonacci({nth_input})", number=1000, setup=setup_rust)
    print(f"Time taken by rust => {rust_timing:.6f}")
