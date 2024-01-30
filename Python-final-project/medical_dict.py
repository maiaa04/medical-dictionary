import pandas as pd


def load_dictionary(file_path):
    """Loads .csv file and converts it to a dictionary.

    file_path: path of the .csv file

    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
    """

    df = pd.read_csv(file_path, header=None, names=['Term', 'Definition'])
    dictionary = df.set_index('Term')['Definition'].to_dict()
    return dictionary


def search(dictionary, term):
    """Searches for a given term in the dictionary and prints term-definition pair.

    It looks for other definitions containing the term as well.
    """

    term_lower = term.lower()
    term_upper = term.upper()
    other_terms = []
    if term in dictionary.keys():
        other_terms.append(term)
    for key in dictionary:
        if term in key:
            if key not in other_terms:
                other_terms.append(key)
        if term_lower in key:
            if key not in other_terms:
                other_terms.append(key)
        if term_upper in key:
            if key not in other_terms:
                other_terms.append(key)
    for key, value in dictionary.items():
        if term in value or term_lower in value or term_upper in value:
            if key not in other_terms:
                other_terms.append(key)
    return other_terms


if __name__ == "__main__":
    term = 'labour'.capitalize()
    file_path = 'definitions_python_project.csv'
    dictionary = load_dictionary(file_path)
    print(search(dictionary, term))
