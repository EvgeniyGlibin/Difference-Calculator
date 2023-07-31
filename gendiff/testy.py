import itertools
from types import NoneType
import json


file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }


file2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


file3 = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": "",
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value",
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45,
    }
  }
}

file4 = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5",
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much",
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str",
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45,
      }
    },
    "fee": 100500,
  }
}


def generate_diff(data1, data2):

    def iter_(current_data1, current_data2):

        keys = sorted(current_data1.keys() | current_data2.keys())
        result = {}
        for key in keys:
            if key not in current_data1:
                result[f'+ {key}'] = current_data2[key]
            elif key not in current_data2:
                result[f'- {key}'] = current_data1[key]
            elif current_data1[key] == current_data2[key]:
                result[f'  {key}'] = current_data1[key]
            elif isinstance(current_data1[key], dict) is True and isinstance(
                    current_data2[key], dict) is True:
                children = iter_(current_data1[key], current_data2[key])
                result[f'  {key}'] = children
            else:
                result[f'- {key}'] = current_data1[key]
                result[f'+ {key}'] = current_data2[key]

        return result

    x = iter_(data1, data2)
    return x

def stringify(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if isinstance(val, NoneType | bool):
                val = json.dumps(val)
            if str(key)[0] in "+- ":
                deep_indent = replacer * (deep_indent_size - 2)
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def get_plain_formater(value):
    lines = []
    keys = list(value.keys())
    count = 0
    for i in range(len(keys)): #лучше через ваил
        # print(keys[i])
        if str(keys[i]).startswith('+ '):
            lines.append(f'Property {str(keys[i])} added')
            
        elif str(keys[i]).startswith('- '):
            print(keys[i])
            
            if str(keys[i])[2:] == str(keys[i + 1])[2:]:
                print('Пришло')
                lines.append(f'Property {str(keys[i])} изменилось значение')
                continue
            else:
                lines.append(f'Property {str(keys[i])} удалилось')
        
    result = itertools.chain(lines)
    return '\n'.join(result)
                
                
        

                
    
    

diff = generate_diff(file1, file2)
print(diff)
print(get_plain_formater(diff))