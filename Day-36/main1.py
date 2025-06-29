import builtins
exceptions = [name for name in dir(builtins) if "Error" in name or "Exception" in name]
print(exceptions)
