def generate_result(data1, data2):

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

    return iter_(data1, data2)
