def get_diff_tree(data1, data2):

    def iter_(current_data1, current_data2):

        keys = sorted(current_data1.keys() | current_data2.keys())
        result = []
        for key in keys:
            if key not in current_data1:
                result.append({
                    'key': key,
                    'operation': 'added',
                    'new_value': current_data2[key],
                })

            elif key not in current_data2:
                result.append({
                    'key': key,
                    'operation': 'removed',
                    'old_value': current_data1[key],
                })
            elif current_data1[key] == current_data2[key]:
                result.append({
                    'key': key,
                    'operation': 'unchanged',
                    'old_value': current_data1[key],
                })
            elif isinstance(current_data1[key], dict) is True and isinstance(
                    current_data2[key], dict) is True:
                children = iter_(current_data1[key], current_data2[key])
                result.append({
                    'key': key,
                    'operation': 'nested',
                    'new_value': children,
                })
            else:
                result.append({
                    'key': key,
                    'operation': 'changed',
                    'old_value': current_data1[key],
                    'new_value': current_data2[key],
                })

        return result

    return iter_(data1, data2)
