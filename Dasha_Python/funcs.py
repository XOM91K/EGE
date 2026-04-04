# # print(max(5, 3))
# def hello():
#     print('ПРИВЕТПРИВЕТПРИВЕТ')
#
# hello()
# hello()
# s = 'Привет'
# s.count('П')
def find_secret(st):
    start_ind = st.index('#')
    finish_ind = st.index('@')
    return st[start_ind + 1:finish_ind]
print(find_secret('one#fishtwo'))