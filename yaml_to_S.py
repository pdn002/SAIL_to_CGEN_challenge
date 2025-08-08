import sys
import yaml

def s_expr(yaml_expr):

    # Represent mapping as (key value)
    if isinstance(yaml_expr, dict):
        sub_s_expr = []
        for key, val in yaml_expr.items():
            sub_s_expr.append(f'({key} {s_expr(val)})')
        return ' '.join(sub_s_expr)

    # Represent Sequences as value_1 value_2 Value_3 ...
    elif isinstance(yaml_expr, list):
        sub_s_expr = []
        for val in yaml_expr:
            sub_s_expr.append(s_expr(val))
        return f'({' '.join(sub_s_expr)})'
    
    # Represent string as "string"
    elif isinstance(yaml_expr, str):
        return f'\"{yaml_expr}\"'
    
    # For numbers, booleans, and None
    else:
        return str(yaml_expr)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise Exception('Must have exactly one filname as command line argument')
    with open(sys.argv[1], 'r') as f:
        yaml_expr = yaml.safe_load(f)
    print(s_expr(yaml_expr))