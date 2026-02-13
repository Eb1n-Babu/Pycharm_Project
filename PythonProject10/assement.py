from numpy.f2py.auxfuncs import flatlist

d = [1,23,4,[4,45,6,6],5,[4,5,6,[5,6,6],[5,667,7]]]


def flatten(x):
    y = []
    for element in x:
        if isinstance(element, list):
            y.extend(flatten(element))
        else:
            y.append(element)
    return y

print(flatten(d))


sample_dict = {
    "user": {
        "id": 101,
        "name": "Ebin",
        "contact": {
            "email": "ebin@example.com",
            "phone": "9876543210"
        }
    },
    "job": {
        "title": "Python Developer",
        "location": {
            "city": "Kochi",
            "country": "India"
        }
    },
    "skills": {
        "backend": ["Python", "Django", "FastAPI"],
        "frontend": ["React", "JavaScript"]
    }
}

def flatten_dict(x):
    y = {}
    for key, value in x.items():
        if isinstance(value, dict):
            for subkey , subvalue in value.items():
                y[key+"."+subkey] = subvalue
            else:
                y[key] = value
    return y

print(flatten_dict(sample_dict))


def flatten_dictionary(x):
    y = {}
    for key , value in x.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                y[key+"."+subkey] = value
            else:
                y[key] = value
    return y
print(flatten_dictionary(sample_dict))

sample_dict = {
    "user": {
        "id": 101,
        "name": "Ebin",
        "contact": {
            "email": "ebin@example.com",
            "phone": "9876543210"
        }
    },
    "job": {
        "title": "Python Developer",
        "location": {
            "city": "Kochi",
            "country": "India"
        }
    },
    "skills": {
        "backend": ["Python", "Django", "FastAPI"],
        "frontend": ["React", "JavaScript"]
    }
}

def dict_flatten(x):
    y = {}
    for key, value in x.items():
        if isinstance(value, dict):
            for subkey,subvalue in value.items():
                y[key+"."+subkey] = subvalue
            else:
                y[key] = value
    return y
print(dict_flatten(sample_dict))

