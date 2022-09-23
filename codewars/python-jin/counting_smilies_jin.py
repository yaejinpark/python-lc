# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
def count_smileys(arr):
    smiles = [':)',':D',':-)',':~)',':-D',':~D', ';)',';D',';-)',';~)',';-D',';~D']
    count = 0
    for face in arr:
        count += 1 if face in smiles else 0
    return count #the number of valid smiley faces in array/list

# regex version - useful for studying regex later on
# from re import findall
# def count_smileys(arr):
#     return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))