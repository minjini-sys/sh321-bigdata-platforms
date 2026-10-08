import importlib, subprocess

def v(mod):
    m = importlib.import_module(mod)
    return getattr(m, "__version__", "n/a")

print("==== Python packages ====")
print("pyspark:", v("pyspark"))
print("pandas :", v("pandas"))
print("numpy  :", v("numpy"))
print("pyarrow:", v("pyarrow"))

print("\n==== Spark ====")
try:
    out = subprocess.check_output(["spark-submit", "--version"], stderr=subprocess.STDOUT, text=True)
    print(out.splitlines()[0])
except Exception as e:
    print("spark-submit not found:", e)

print("\n==== Java ====")
try:
    out = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT, text=True)
    print(out.splitlines()[0])
except Exception as e:
    print("java not found:", e)
