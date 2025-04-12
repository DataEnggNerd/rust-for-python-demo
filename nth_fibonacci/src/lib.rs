use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn fibonacci(n: u64) -> PyResult<u64> {
    if n <= 1 {
        return Ok(n);
    }

    let mut a = 0;
    let mut b = 1;

    for _ in 2..=n {
        let temp = a + b;
        a = b;
        b = temp;
    }

    Ok(b)
}

/// A Python module implemented in Rust.
#[pymodule]
fn nth_fibonacci(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fibonacci, m)?)?;
    Ok(())
}
