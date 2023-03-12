#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined_names = [name for name in dir(hidden_4) if not name.startswith("_")]
    for name in defined_names:
        print(name)
