
def get_type_user(data):
    type = {
        'ADM':'ADM',
        'USR':'USR',
    }
    return type.get(data, None)


def get_model(encoded_sender):
    parts = str(encoded_sender).split('.')
    model = parts[1]
    return model



