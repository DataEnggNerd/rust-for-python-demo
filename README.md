## Rust for Python - an introduction

This repository contains code which is used for demonstrating the performance gain from Rust tooling.

## Demonstration steps

1. Create fibinacci code with Python without recursion. Add `timeit` to get the time taken for python to execute the same code for 1000 iterations on finding nth fibonacci number.
2. Using [uv](https://docs.astral.sh/uv/), create a virtual environment and add `maturin`.
3. `maturin new nth_fibonacci` will create a folder named `nth_fibonacci` with essential files for the rust package.
4. Add rust code for finding the nth fibonacci number with same approach used in Python code in `nth_fibonacci/src/lib.rs`
5. Develop the rust code as a python package with `maturin develop` and `maturin build`.
6. Now import the `nth_fibonacci` module in `main.py` and add timeit for testing.

## Results

The result shows as below,

```shell
# Iteration 1 - 39% improvement
Time taken by python => 0.001871
Time taken by rust => 0.001126

# Iteration 2 - 44% improvement
Time taken by python => 0.002420
Time taken by rust => 0.001345

# Iteration 3 - 47% improvement
Time taken by python => 0.002437
Time taken by rust => 0.001286
```

Evidently, this shows consistent improvement in performance on using Rust package for the same problem statement.

Presentation slides are available in - https://docs.google.com/presentation/d/1OYanUWzpG3Wr9H9WbyoOTX6vWyWfWmeJrY9BMrXgdj4/edit?usp=sharing
