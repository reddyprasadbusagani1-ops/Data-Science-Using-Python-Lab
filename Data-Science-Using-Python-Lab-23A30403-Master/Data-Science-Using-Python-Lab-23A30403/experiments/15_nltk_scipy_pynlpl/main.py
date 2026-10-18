"""
Experiment 15: NLTK, SciPy, and PyNLPl
Course Code: 23A30403 - Data Science Using Python Lab
Note: PyNLPl is an optional package handled gracefully.
"""
import numpy as np
from scipy import stats

def main():
    print("=== Experiment 15: Text Analysis with SciPy & Optional PyNLPl ===")
    
    text = "Data Science relies heavily on statistics, linear algebra, and machine learning."
    tokens = text.lower().replace('.', '').replace(',', '').split()
    lengths = [len(w) for w in tokens]
    
    print(f"Tokens: {tokens}")
    print(f"Word Lengths: {lengths}")
    
    mean_len = np.mean(lengths)
    median_len = np.median(lengths)
    mode_res = stats.mode(lengths, keepdims=False)
    
    print(f"\nSciPy Statistical Metrics for Word Lengths:")
    print(f" - Mean Length: {mean_len:.2f}")
    print(f" - Median Length: {median_len:.2f}")
    print(f" - Mode Length: {mode_res.mode} (Count: {mode_res.count})")
    
    try:
        import pynlpl
        print(f"\nPyNLPl module detected! Version: {getattr(pynlpl, '__version__', 'Installed')}")
    except ImportError:
        print("\nNote: PyNLPl library is not installed (Optional dependency).")
        print("To install PyNLPl: pip install pynlpl")

if __name__ == "__main__":
    main()
